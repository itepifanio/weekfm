import settings as app
import requests

user = app.network.get_user(app.username)
weekly_artists_played = user.get_weekly_artist_charts()[0:5]

tweet = ""

s = "{} ({}), "

for i in range(0,5):
    if(i == 4):
        s = "{} ({})"

    tweet += s.format(
        weekly_artists_played[i].item.name, 
        weekly_artists_played[i].weight
    )
    

tweet += " #weekfm"

app.api.PostUpdate(tweet)    

