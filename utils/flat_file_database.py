from tinydb import TinyDB, Query
import threading
import logging

LOGGER = logging.getLogger(__name__)


class FlatFileDB:
    def __init__(self):
        self.db = TinyDB('utils/files/db.json')
        self._lock = threading.Lock()

    def insert_post(self, submission):
        if not self._post_exists(submission):
            self.db.insert(
                {'id': submission.id, 'url': submission.url, 'author': submission.author.name, 'posted': False})
            LOGGER.info("Submission id=%s inserted into db" % submission.id)

    def _post_exists(self, submission):
        post = Query()
        return len(self.db.search(post.id == submission.id)) != 0

    def get_post(self):
        post = Query()
        popped = self.db.search(post.posted == False)
        if popped:
            self.db.update({'posted': True}, popped[0].get('id') == post.id)
            LOGGER.info("Submission id=%s retrieved from db" % popped[0].get('id'))
            return popped[0]
