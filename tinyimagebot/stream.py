import config
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream


def debug_status(status):

    print "Tweet ID: %s" % status.get('id')
    print "Sender ID: %s" % status.get('sender_id_str')
    print "Sender Name: %s" % status.get('sender_screen_name')
    print "Txt: %s" % status.get('text')
    print "IRT: %s" % status.get('in_reply_to_status_id_str')

    user_mentions = status.get('user_mentions')
    print "User Mentions: %s" % user_mentions
    # u'user_mentions': [{u'id': 2929029785, u'indices': [0, 13], u'id_str': u'2929029785', u'screen_name': u'tinyimagebot', u'name': u'Tiny Image Bot'}], u'hashtags': [], u'urls': []},

    # If I am in user mentions

    hashtags = status.get('hashtags')
    # ex  u'hashtags': [{u'indices': [0, 14], u'text': u'extremelytiny'}],
    print "Hashtags: %s" % hashtags

    media = status.get('media')
    print "Media: %s" % media

    if media:
        print "url: %s" % media[0]['media_url_https']


class TinyImageListener(StreamListener):

    def on_status(self, status):
        """Called when a new status arrives"""
        print "TWEET"
        debug_status(status._json)
        return True

    def on_direct_message(self, status):
        """Called when a new direct message arrives"""
        print "DM"
        print  debug_status(status._json['direct_message'])

        return True

    def on_error(self, status_code):
        """Called when a non-200 status code is returned"""
        print status_code
        return False

    def on_timeout(self):
        """Called when stream connection times out"""
        print 'Stream Timed out'
        return

    def on_disconnect(self, notice):
        """Called when twitter sends a disconnect notice

        Disconnect codes are listed here:
        https://dev.twitter.com/docs/streaming-apis/messages#Disconnect_messages_disconnect
        """
        print notice
        return
    
    def on_warning(self, notice):
        """Called when a disconnection warning message arrives"""
        print 'Warning received: %s' % notice
        return


def run():

    listener = TinyImageListener()
    auth = OAuthHandler(config.consumer_key, config.consumer_secret)
    auth.set_access_token(config.access_token, config.access_token_secret)
    print auth
    stream = Stream(auth, listener)
    stream.userstream(_with='user')


if __name__ == "__main__":
    run()