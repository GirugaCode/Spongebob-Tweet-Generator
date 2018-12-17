import os
import dotenv
from requests_oauthlib import OAuth1Session

# use this for production; set vars in heroku dashboard
from os import environ
CONSUMER_KEY = environ['TWITTER_CONSUMER_KEY']
CONSUMER_SECRET = environ['TWITTER_CONSUMER_SECRET']
ACCESS_KEY = environ['TWITTER_ACCESS_TOKEN']
ACCESS_SECRET = environ['TWITTER_ACCESS_TOKEN_SECRET']

dotenv.load_dotenv('.env')

consumer_key = os.environ.get('TWITTER_CONSUMER_KEY')
consumer_secret = os.environ.get('TWITTER_CONSUMER_SECRET')
access_token = os.environ.get('TWITTER_ACCESS_TOKEN')
access_token_secret = os.environ.get('TWITTER_ACCESS_TOKEN_SECRET')

session = OAuth1Session(consumer_key,
                        client_secret=consumer_secret,
                        resource_owner_key=access_token,
                        resource_owner_secret=access_token_secret)


# The URL endpoint to update a status (i.e. tweet)
url = 'https://api.twitter.com/1.1/statuses/update.json'

def tweet(status):
    resp = session.post(url, { 'status': status })
    return resp.text
