import time
from utils.reddit import Reddit
from threading import Thread

def main():
    pass

class RedditRunner:
    def __init__(self, interval=10):
        self.interval = interval
        thread = Thread(target = self.run, args=())
        thread.daemon = True
        thread.start()

    def run(self):
        reddit = Reddit()
        while True:
            reddit.check_subreddits()
            time.sleep(self.interval)


if __name__ == '__main__':
    main()
