import logging
from models import SimpleTweet
import imageproc
import json
import config
import os
import time
import arrow


# TODO: check how many images in an exchange. Limit after certain point.
def run(twython, r, status_channel, wait_time=90):

    logging.info("Subscribing to channel: %s" % status_channel)
    pubsub = r.pubsub(ignore_subscribe_messages=True)
    pubsub.subscribe(status_channel)

    logging.info("Starting to listen to messages")
    for message in pubsub.listen():

        logging.info("Received message. Loading into status.")
        status = SimpleTweet(json.loads(message['data']))
        logging.info("Examining message with text: %s" % status.text)
        
        if should_process_image(status):
            logging.info("Passed muster, processing image!")

            if user_not_rate_limited(r, status):
                try:
                    process_status(twython, status)
                except Exception as e:
                    logging.exception(e)
            else:
                logging.info("We have been rate limited for user %s, putting back in queue." \
                    % status.sender_screen_name)
                r.publish(status_channel, json.dumps(message['data']))

            logging.info("Sleeping for %s seconds" % wait_time)
            time.sleep(wait_time)
        else:
            logging.info("Didn't pass muster, not processing image.")


def should_process_image(status):
    return status.sender_screen_name != config.app_screen_name and \
            status.media is not None


def user_not_rate_limited(r, status, limit=15, limit_expiration=21600):
    """ Maintains a cache so we can only handle a maximum of N exchanges with a user per day.
        Returns True if we can proceed, false if we are rate limited. """
    user_from = status.sender_screen_name

    key = get_rate_key(user_from)

    counter = r.get(key)

    # If we don't have a key, increment it and expire the key in a day
    logging.info("User rate limit key == %s / %s" % (counter, limit))

    if counter is None:
        logging.info("First message in a while from user, expiring key in %s seconds" % limit_expiration)

        with r.pipeline() as pipe:
            pipe.incr(key)
            pipe.expire(key, limit_expiration)
            pipe.execute()
        return True

    # If we're over the limit, rate limit thigns
    elif int(counter) > limit:
        return False

    # Otherwise, increment and proceed
    else:
        r.incr(key)
        return True

def get_rate_key(username):
    now = arrow.get()
    month = now.month
    day = now.day

    key = "%s%s%s" % (username, month, day)
    return key

def process_status(twython, status):

    # Download Image
    img = imageproc.get_image_from_url(status.media)

    size_name, size = imageproc.get_image_size(status)
    current_size = img.size[0]

    # If it's really really tiny, stop trying to process
    if current_size <= 6:
        post_done_update(twython, status)
    else:

        # Resize and post image
        if current_size <= size:
            size = current_size / 2
            logging.info("Already small, making smaller: %s :: %s" % (current_size, size))

        logging.info("Size: %s" % size)
        resized = imageproc.resize_image(img, size)

        img_path = imageproc.save_and_get_image_path(resized)

        message = get_message(status)

        logging.info("Sending image with message: %s" % message)
        post_update(twython, img_path, message, status.tweet_id)
        logging.info("Success. Deleting temporary file.")
        os.remove(img_path)



def post_done_update(twython, status):
    user_from = status.sender_screen_name
    message = ".@" + user_from + \
        " Wow, that image is already really tiny. I think our work here is done."
    twython.update_status(
        status=message,
        in_reply_to_status_id=status.tweet_id)


def get_message(status):

    user_from = status.sender_screen_name
    base_message = ". @" + user_from + " Your tiny image is ready"

    size_name, size = imageproc.get_image_size(status)
    hashtag_message = "#" + size_name

    message = base_message + ": " + hashtag_message
    return message


def post_update(twython, img_path, message, reply_id):

    with open(img_path, 'r') as image_file:
        logging.info("Uploading Image: %s" % img_path)

        upload_response = twython.upload_media(media=image_file)
        logging.info("Uploaded as media ID %s. Updating status." % upload_response)

        # TODO: These don't return anything
        # media_rate_limit = twython.get_lastfunction_header('X-MediaRateLimit-Limit')
        # media_rate_remaining  = twython.get_lastfunction_header('X-MediaRateLimit-Remaining')
        # media_rate_reset  = twython.get_lastfunction_header('X-MediaRateLimit-Reset')
        #
        # logging.info("Media rate limits: %s :: %s :: %s" % (
        #    media_rate_limit, 
        #    media_rate_remaining,
        #    media_rate_reset
        # ))

        media_id = upload_response['media_id']

        time.sleep(10)
        twython.update_status(
            status=message,
            in_reply_to_status_id=reply_id,
            media_ids=[media_id])

