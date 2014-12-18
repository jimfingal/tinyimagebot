import os

redis_url = 'redis://localhost:6379'

app_name = "TINY"

consumer_key = os.environ.get(app_name + '_CONSUMER_KEY')
consumer_secret = os.environ.get(app_name + '_CONSUMER_SECRET')
access_token = os.environ.get(app_name + '_ACCESS_TOKEN')
access_token_secret = os.environ.get(app_name + '_ACCESS_TOKEN_SECRET')

app_screen_name  = os.environ.get(app_name + '_SCREEN_NAME')


_pubsub_base = "twitter"
_channel_separator = "."

status_channel = _pubsub_base + _channel_separator + "status"
