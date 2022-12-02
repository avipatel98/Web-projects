from lib.post import Post


class PostRepository:
    def __init__(self):
        self.store = []

    def all(self):
        return self.store

    def all_by_tag(self, tag):
        return [post for post in self.store if tag in post.tags]

    def create(self, post):
        self.store.append(post)
        post.id = self._generate_next_id()
        return post

    def _generate_next_id(self):
        x = [post.id for post in self.store]
        if x[0] == None:
            return 1
        else:
            return x[-2] + 1

