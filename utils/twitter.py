import os
import twitter
from utils.flat_file_database import FlatFileDB
from dotenv import load_dotenv

load_dotenv()


class Twitter:
    def __init__(self):
        self.twitter = twitter.Api(
            consumer_key=os.getenv("TWITTER_API_KEY"),
            consumer_secret=os.getenv("TWITTER_API_SECRET_KEY"),
            access_token_key=os.getenv("TWITTER_ACCESS_TOKEN"),
            access_token_secret=os.getenv("TWITTER_ACCESS_TOKEN_SECRET")
        )

    def post_image_from_db(self):
        db = FlatFileDB()
        post = db.get_post()
        if post:
            status = "Reposted from Reddit. Author: %s" % post.get("author")
            self.twitter.PostUpdate(status=status, media=post.get("url"))
