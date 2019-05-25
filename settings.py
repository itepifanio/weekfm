from dotenv import load_dotenv
load_dotenv()
import os
import pylast

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

