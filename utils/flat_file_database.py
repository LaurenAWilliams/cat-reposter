from tinydb import TinyDB, Query
import threading


class FlatFileDB:
    def __init__(self):
        self.db = TinyDB('utils/files/db.json')
        self._lock = threading.Lock()

    def insert_post(self, submission):
        while self._lock:
            if not self._post_exists(submission):
                self.db.insert(
                    {'id': submission.id, 'url': submission.url, 'author': submission.author.name, 'posted': False})

    def _post_exists(self, submission):
        post = Query()
        return len(self.db.search(post.id == submission.id)) != 0

    def get_post(self):
        while self._lock:
            post = Query()
            popped = self.db.search(post.posted == False)
            self.db.update({'posted': True}, popped[0].get('id') == post.id)
            return popped[0]
