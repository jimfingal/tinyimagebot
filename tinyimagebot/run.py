import logging
from multiprocessing import Process

import redis
from twython import Twython
import config
import stream
import tinyifier

def run_image_processor_from_config(config):
    
    r = redis.from_url(config.redis_url)

    twython = Twython(config.consumer_key, config.consumer_secret,
                    config.access_token, config.access_token_secret)

    # Blocks and processes images
    tinyifier.run(twython, r, config.status_channel)

def run_stream_from_config(config):

    r = redis.from_url(config.redis_url)
    listener = stream.RedisPublishListener(r, config.status_channel)

    # Blocks and processes stream
    stream.run(config.consumer_key, 
        config.consumer_secret, 
        config.access_token, 
        config.access_token_secret, 
        listener)


if __name__ == "__main__":

    log_fmt = "%(levelname)-6s %(processName)s %(filename)-12s:%(lineno)-4d at %(asctime)s: %(message)s"
    logging.basicConfig(level=logging.INFO, format=log_fmt)

    stream_proc = Process(target=run_stream_from_config, args=(config,))
    image_proc = Process(target=run_image_processor_from_config, args=(config,))

    stream_proc.start()
    image_proc.start()

    stream_proc.join()
    image_proc.join()