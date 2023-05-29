class Article:
    def __init__(self, author, magazine, title):
        self.author = author
        self.magazine = magazine
        self.title = title

    def get_author(self):
        return self.author

    def get_magazine(self):
        return self.magazine
