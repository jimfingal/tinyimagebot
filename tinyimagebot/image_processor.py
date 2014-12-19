from PIL import Image
from cStringIO import StringIO
import requests
import logging
import time
import config
import json
import random
import os

from models import SimpleTweet

size_map = {
    'tiny': ('tiny', 50),
    'verytiny': ('verytiny', 20),
    'extremelytiny': ('extremelytiny', 10),
    'miniscule': ('miniscule', 1)
}

image_buffer_filename = "/tmp/tmpprocessed"

def get_image_from_url(url):
    r = requests.get(url)
    img = Image.open(StringIO(r.content))
    return img

def resize_image(img, width):
    wpercent = (width / float(img.size[0]))
    height = int((float(img.size[1]) * float(wpercent)))
    img2 = img.resize((width, height), Image.NEAREST)
    return img2

def save_and_get_image_path(img):
    rand = random.randint(1, 10000)
    img_path = "%s%s.png" % (image_buffer_filename, rand)
    logging.info("Saving temp file to: %s" % img_path)
    img.save(img_path, format='PNG')
    return img_path

def should_process_image(status):
    return status.sender_screen_name != config.app_screen_name and \
            status.media is not None

def get_image_size(status):

    for hashtag in status.hashtags:
        size = size_map.get(hashtag)
        if size:
            return size

    return size_map.get('tiny')

def get_hashtag_message(status):
    size_name, size = get_image_size(status)
    return "#" + size_name

def get_base_message(status):
    user_from = status.sender_screen_name
    msg = ".@" + user_from + " Your tiny image is ready"
    return msg

def get_message(status):
    base_message = get_base_message(status)
    hashtag_message = get_hashtag_message(status)
    message = base_message + ": " + hashtag_message
    return message

def process_image(status):

    logging.info("Processing URL: %s" % status.media)
    logging.info("With hashtags: %s" % status.hashtags)
    img = get_image_from_url(status.media)
    size_name, size = get_image_size(status)

    logging.info("Size: %s" % size)
    resized = resize_image(img, size)

    img_path = save_and_get_image_path(resized)
    return img_path

def post_update(twython, img_path, message, reply_id):

    with open(img_path, 'r') as image_file:
        logging.info("Uploading Image: %s" % img_path)

        upload_response = twython.upload_media(media=image_file)
        logging.info("Uploaded as media ID %s. Updating status." % upload_response)

        media_rate_limit = twython.get_lastfunction_header('X-MediaRateLimit-Limit')
        media_rate_remaining  = twython.get_lastfunction_header('X-MediaRateLimit-Remaining')
        media_rate_reset  = twython.get_lastfunction_header('X-MediaRateLimit-Reset')

        logging.info("Media rate limits: %s :: %s :: %s" % (
                media_rate_limit, 
                media_rate_remaining,
                media_rate_reset
        ))

        media_id = upload_response['media_id']
        
        time.sleep(10)
        twython.update_status(
            status=message,
            in_reply_to_status_id=reply_id,
            media_ids=[media_id])

def run(twython, pubsub, status_channel):

    logging.info("Subscribing to channel: %s" % status_channel)
    pubsub.subscribe(status_channel)

    logging.info("Starting to listen to messages")
    for message in pubsub.listen():
        logging.info("Received message. Loading into status.")
        status = SimpleTweet(json.loads(message['data']))
        logging.info("Message: %s" % status.text)
        if should_process_image(status):
            logging.info("Processing image!")

            try:
                
                img_path = process_image(status)
                message = get_message(status)

                logging.info("Sending image with message: %s" % message)
                post_update(twython, img_path, message, status.tweet_id)
                logging.info("Success. Deleting temporary file.")
                os.remove(img_path)

            except Exception as e:
                logging.exception(e)
        else:
            logging.info("Not processing image")

        time.sleep(120)