import os
import logging
import twitter
from utils.flat_file_database import FlatFileDB
from dotenv import load_dotenv

load_dotenv()

LOGGER = logging.getLogger(__name__)


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
            LOGGER.info("Posting to Twitter: status='%s', url=%s" % (status, post.get('url')))
            try:
                self.twitter.PostUpdate(status=status, media=post.get("url"))
            except twitter.error.TwitterError as error:
                LOGGER.error("Error raised posting to twitter: %s" % error)
