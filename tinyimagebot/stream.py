import json
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import logging

class RawListener(StreamListener):
    ''' Overrides on_data to pass raw json instead of parsing status objects '''

    def on_data(self, raw_data):
        """Called when raw data is received from connection.

        Override this method if you wish to manually handle
        the stream data. Return False to stop stream and close connection.
        """
        data = json.loads(raw_data)
        logging.debug(data)

        if 'in_reply_to_status_id' in data:
            if self.on_status(data) is False:
                return False
        elif 'delete' in data:
            delete = data['delete']['status']
            if self.on_delete(delete['id'], delete['user_id']) is False:
                return False
        elif 'event' in data:
            if self.on_event(data) is False:
                return False
        elif 'direct_message' in data:
            if self.on_direct_message(data['direct_message']) is False:
                return False
        elif 'friends' in data:
            if self.on_friends(data['friends']) is False:
                return False
        elif 'limit' in data:
            if self.on_limit(data['limit']['track']) is False:
                return False
        elif 'disconnect' in data:
            if self.on_disconnect(data['disconnect']) is False:
                return False
        elif 'warning' in data:
            if self.on_warning(data['warning']) is False:
                return False
        else:
            logging.error("Unknown message type: " + str(raw_data))

    def on_error(self, status_code):
        logging.error('Received error with status code: %s' % status_code)
        return False

    def on_timeout(self):
        logging.error('Stream Timed out')
        return

    def on_disconnect(self, notice):
        logging.error('Stream Disconnected: %s' % notice)
        return

    def on_warning(self, notice):
        """Called when a disconnection warning message arrives"""
        logging.warning('Warning received: %s' % notice)
        return

class RedisPublishListener(RawListener):

    def __init__(self, redis, status_channel, *args, **kwargs):
        self.redis = redis
        self.status_channel = status_channel
        logging.info("Publishing to channel: %s" % self.status_channel)
        super(RedisPublishListener, self).__init__(*args, **kwargs)

    def on_status(self, data):
        """Called when a new status arrives"""
        self.redis.publish(self.status_channel, json.dumps(data))
        return True

def run(consumer_key, consumer_secret, access_token, access_token_secret, listener):
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, listener)
    stream.userstream(_with='user')


if __name__ == "__main__":
    from listener import TinyImageListener
    import redis
    import config

    log_fmt = "%(levelname)-6s %(processName)s %(filename)-12s:%(lineno)-4d at %(asctime)s: %(message)s"
    logging.basicConfig(level=logging.INFO, format=log_fmt)

    r = redis.from_url(config.REDIS_URL)
    listener = TinyImageListener(r, config.PUBSUB_CHANNEL)

    run(config.consumer_key, 
        config.consumer_secret, 
        config.access_token, 
        config.access_token_secret, 
        listener)
