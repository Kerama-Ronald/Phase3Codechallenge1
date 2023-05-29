class Magazine:
    def __init__(self, name, category):
        self.name = name
        self.category = category
        self.articles = []

    def add_article(self, author, title):
        article = Article(author, self, title)
        self.articles.append(article)

    def get_articles(self):
        return self.articles

    