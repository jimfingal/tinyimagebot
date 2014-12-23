import logging
from models import SimpleTweet
import imageproc
import json
import config
import os
import time

def run(twython, pubsub, status_channel, wait_time=300):

    logging.info("Subscribing to channel: %s" % status_channel)
    pubsub.subscribe(status_channel)

    logging.info("Starting to listen to messages")
    for message in pubsub.listen():

        logging.info("Received message. Loading into status.")
        status = SimpleTweet(json.loads(message['data']))
        logging.info("Examining message with text: %s" % status.text)
        
        if should_process_image(status):
            logging.info("Passed muster, processing image!")

            try:
                process_status(twython, status)
            except Exception as e:
                logging.exception(e)

            logging.info("Sleeping for %s seconds" % wait_time)
            time.sleep(wait_time)
        else:
            logging.info("Didn't pass muster, not processing image.")


def should_process_image(status):
    return status.sender_screen_name != config.app_screen_name and \
            status.media is not None


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

