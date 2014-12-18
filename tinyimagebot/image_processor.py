from PIL import Image
from StringIO import StringIO
import requests
import logging
import time
import config
import json

from models import SimpleTweet

small_size = 50
tiny_size = 20
very_tiny_size = 10
extremely_tiny_size = 1

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

    if 'tiny' in status.hashtags:
        return tiny_size
    elif 'verytiny' in status.hashtags:
        return very_tiny_size
    elif 'extremelytiny' in status.hashtags:
        return extremely_tiny_size
    else:
        return small_size


def process_image(status):

    logging.info("Processing URL: %s" % status.media)
    logging.info("With hashtags: %s" % status.hashtags)
    img = get_image_from_url(status.media)
    size = get_image_size(status)

    logging.info("Size: %s" % size)
    resized = resize_image(img, size)

    # TODO -- tweet it
    resized.save('tmp.jpg')


def run(pubsub, status_channel):

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