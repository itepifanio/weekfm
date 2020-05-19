from dotenv import load_dotenv
load_dotenv()
import os
import pylast
import twitter


username = os.getenv('LASTFM_USERNAME')

network = pylast.LastFMNetwork(
    api_key=os.getenv('LASTFM_API_KEY'), 
    api_secret=os.getenv('LASTFM_SHARED_SECRET'),
    username=username, 
    password_hash=pylast.md5(os.getenv('LASTFM_PASSWORD'))
)

api = twitter.Api(
    consumer_key=os.getenv('TWITTER_CONSUMER_API_KEY'),
    consumer_secret=os.getenv('TWITTER_CONSUMER_API_SECRET'),
    access_token_key=os.getenv('TWITTER_ACCESS_TOKEN'),
    access_token_secret=os.getenv('TWITTER_ACCESS_TOKEN_SECRET')
)

