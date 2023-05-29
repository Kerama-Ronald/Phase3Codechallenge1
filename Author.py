from Article import Article

class Author:
    def __init__(self, name):
        self.name = name
        self.articles = []

    def add_article(self, magazine, title):
        article = Article(self, magazine, title)
        self.articles.append(article)

    def get_articles(self):
        return self.articles

    def get_magazines(self):
        magazines = []
        for article in self.articles:
            magazines.append(article.get_magazine())
        return list(set(magazines))

author = Author("Robert Greene")

author.add_article("Vogue", "The Power Dynamics in Society")

articles = author.get_articles()
for article in articles:
    print(article.title)

magazines = author.get_magazines()
for magazine in magazines:
    print(magazine)
