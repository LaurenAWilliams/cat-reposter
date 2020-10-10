import time
from utils.reddit import Reddit
from utils.twitter import Twitter
from threading import Thread


def main():
    reddit_runner = RedditRunner()
    twitter_runner = TwitterRunner()
    reddit_runner.start()
    time.sleep(10)
    twitter_runner.start()
    while True:
        pass


class RedditRunner(Thread):
    def __init__(self, interval=60*10):
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
