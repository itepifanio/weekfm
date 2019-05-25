import settings as app
import requests

user = app.network.get_user(app.username)
weekly_artists_played = user.get_weekly_artist_charts()[0:5]

for i in range(0,5):
    print('{} - ({}),'.format(
        weekly_artists_played[i].item.name, 
        weekly_artists_played[i].weight)
    )

