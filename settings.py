from dotenv import load_dotenv
load_dotenv()
import os
import pylast
import twitter

API_KEY=os.getenv('API_KEY')
API_SECRET=os.getenv('SHARED_SECRET')

username = os.getenv('USERNAME')
password_hash = pylast.md5(os.getenv('PASSWORD'))

network = pylast.LastFMNetwork(
    api_key=API_KEY, 
    api_secret=API_SECRET,
    username=username, 
    password_hash=password_hash
)

api = twitter.Api(
    consumer_key=os.getenv('TWEET_CONSUMER_API_KEY'),
    consumer_secret=os.getenv('TWEET_CONSUMER_API_SECRET'),
    access_token_key=os.getenv('TWEET_ACCESS_TOKEN'),
    access_token_secret=os.getenv('TWEET_ACCESS_TOKEN_SECRET')
)

