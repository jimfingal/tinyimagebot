from PIL import Image
from StringIO import StringIO
import requests
import logging
import time
import config
import json

from models import SimpleTweet

size_map = {
    'tiny': ('tiny', 50),
    'verytiny': ('verytiny', 20),
    'extremelytiny': ('extremelytiny', 10),
    'miniscule': ('miniscule', 1)
}

def get_image_from_url(url):
    r = requests.get(url)
    img = Image.open(StringIO(r.content))
    return img

def resize_image(img, width):
    wpercent = (width / float(img.size[0]))
    height = int((float(img.size[1]) * float(wpercent)))
    img2 = img.resize((width, height), Image.NEAREST)
    return img2

def get_image_output(img):
    image_io = StringIO.StringIO()
    img.save(image_io, format='JPEG')
    image_io.seek(0)  # seeks back to beginning of file for output
    return image_io

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

    img_out = get_image_output(resized)
    message = get_message(status)

    return img_out


def run(twitter, pubsub, status_channel):

    logging.info("Subscribing to channel: %s" % status_channel)
    pubsub.subscribe(status_channel)

    logging.info("Starting to listen to messages")
    for message in pubsub.listen():
        logging.info("Received message. Loading into status.")
        status = SimpleTweet(json.loads(message['data']))

        if should_process_image(status):
            logging.info("Processing image!")
            process_image(status)

        else:
            logging.info("Not processing image")

        time.sleep(5)