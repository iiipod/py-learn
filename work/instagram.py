from instagram.client import InstagramAPI

access_token = "ps1"
client_secret = "password"

api = InstagramAPI(access_token=access_token, client_secret=client_secret)
recent_media, next_ = api.user_recent_media(user_id="userid", count=10)

for media in recent_media:
    print media.caption.text
