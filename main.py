import time
import logging
from utils.reddit import Reddit
from utils.twitter import Twitter
from threading import Thread

LOGGER = logging.getLogger(__name__)


def main():
    logging.basicConfig(filename='cat-reposter.log', level=logging.INFO,
                        format='%(asctime)s %(threadName)s %(message)s',
                        datefmt='%m/%d/%Y %I:%M:%S %p')
    reddit_runner = RedditRunner()
    twitter_runner = TwitterRunner()
    reddit_runner.start()
    LOGGER.info("RedditRunner started")
    time.sleep(10)
    twitter_runner.start()
    LOGGER.info("TwitterRunner started")
    while True:
        pass


class RedditRunner(Thread):
    def __init__(self, interval=60):
        self.interval = interval
        Thread.__init__(self)
        self.daemon = True
        self.running = True

    def run(self):
        reddit = Reddit()
        while self.running:
            reddit.check_subreddits()
            time.sleep(self.interval)

    def stop(self):
        self.running = False


class TwitterRunner(Thread):
    def __init__(self, interval=60*10):
        self.interval = interval
        Thread.__init__(self)
        self.daemon = True
        self.running = True

    def run(self):
        twitter = Twitter()
        while self.running:
            twitter.post_image_from_db()
            time.sleep(self.interval)

    def stop(self):
        self.running = False


if __name__ == '__main__':
    main()
