import praw
import os
import time
from dotenv import load_dotenv
from utils.flat_file_database import FlatFileDB
from utils.image import is_cat
from utils.cat_subreddit_list import CAT_SUBREDDIT_LIST

load_dotenv()


class Reddit:
    def __init__(self):
        self.user = praw.Reddit(
            client_id=os.getenv("REDDIT_CLIENT_ID"),
            client_secret=os.getenv("REDDIT_CLIENT_SECRET"),
            password=os.getenv("REDDIT_PASSWORD"),
            user_agent=os.getenv("REDDIT_USERNAME"),
            username=os.getenv("REDDIT_USERNAME")
        )
        self.user.read_only = True

    def _get_top_10_submissions(self, subreddit, db):
        for submission in self.user.subreddit(subreddit).top(limit=10, time_filter="day"):
            print("url: ", submission.url)
            print("subreddit: ", subreddit)
            if self._is_image_submission(submission) and is_cat(submission.url):
                db.insert_post(submission)

    def check_subreddits(self):
        db = FlatFileDB()
        for subreddit in CAT_SUBREDDIT_LIST:
            self._get_top_10_submissions(subreddit, db)

    @staticmethod
    def _is_image_submission(submission):
        return all([not submission.is_self, submission.is_reddit_media_domain,
                    submission.domain == 'i.redd.it'])
