from abc import ABC, abstractmethod


class Article(ABC):
    @abstractmethod
    def render(self):
        pass


class TextArticle(Article):
    def __init__(self, text: str) -> None:
        self.text = text

    def render(self) -> str:
        return self.text


# class ArticleDecorator(Article):
#     def __init__(self, article: Article) -> None:
#         self.article = article
#
#     def render(self) -> str:
#         return self.article.render()


class Limiter():
    def __init__(self, article: Article, limit: int = 30) -> None:
        self.article = article
        self.limit = limit


    def render(self) -> str | None:
        rendered_article = self.article.render()
        if len(rendered_article) > self.limit:
            raise ValueError("Article is too long!")
        return rendered_article


if __name__ == "__main__":
    article = TextArticle("Hello, world!")
    print(Limiter(article).render())

    print(Limiter(article, 5).render())
