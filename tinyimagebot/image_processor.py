from PIL import Image
from StringIO import StringIO
import requests

import config
import redis
import logging
import time


SMALL = 50
TINY = 20
VERY_TINY = 10
EXTREMELY_TINY = 1


def get_image_from_url(url):
    r = requests.get("https://pbs.twimg.com/media/B5HG0gWIgAAcyn2.png")
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


def run():

    r = redis.from_url(config.REDIS_URL)
    p = r.pubsub(ignore_subscribe_messages=True)

    logging.info("Subscribing to channel: %s" % config.PUBSUB_CHANNEL)
    p.subscribe(config.PUBSUB_CHANNEL)

    logging.info("Starting to listen to messages")
    for message in p.listen():
        print "Message: ", message
        print 'MY HANDLER: ', message['data']
        time.sleep(5)