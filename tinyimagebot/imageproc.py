from PIL import Image
from cStringIO import StringIO
import requests
import logging
import random

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


def get_image_size(status):

    for hashtag in status.hashtags:
        size = size_map.get(hashtag)
        if size:
            return size

    return size_map.get('tiny')
