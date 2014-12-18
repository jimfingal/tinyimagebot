import os

REDIS_URL = 'redis://localhost:6379'
PUBSUB_CHANNEL = "test_channel"


app_name = "TINY"

consumer_key = os.environ.get(app_name + '_CONSUMER_KEY')
consumer_secret = os.environ.get(app_name + '_CONSUMER_SECRET')
access_token = os.environ.get(app_name + '_ACCESS_TOKEN')
access_token_secret = os.environ.get(app_name + '_ACCESS_TOKEN_SECRET')
