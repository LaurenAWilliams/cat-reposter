from tinydb import TinyDB, Query

class FlatFileDB:
    def __init__(self):
        self.db = TinyDB('utils/files/db.json')

    def insert_post(self, submission):
        if not self._post_exists(submission):
            self.db.insert({'id': submission.id, 'url': submission.url, 'author': submission.author.name})

    def _post_exists(self, submission):
        post = Query()
        return len(self.db.search(post.id == submission.id)) != 0

    def pop_post(self):
        popped = self.db.all().pop(0) if self.db.all() else None
        post = Query()
        self.db.remove(popped.get('id') == post.id)
        return popped
