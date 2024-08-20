class Article:
    articles = []

    def __init__(self, title: str, authors: list, keywords: list, abstract: str,
                 file_size: int, status='Pending review', cover='') -> None:
        self.__title = title
        self.__authors = authors
        self.__keywords = keywords
        self.__abstract = abstract
        self.__file_size = file_size
        self.__reviewers = []
        self.__status = status
        self.__comments = []
        self.__cover = cover

        Article.articles.append(self)

    # Decorators
    @property
    def title(self) -> str:
        return self.__title

    @title.setter
    def title(self, title: str) -> None:
        self.__title = title

    @property
    def authors(self) -> list:
        return self.__authors

    @authors.setter
    def authors(self, authors: list) -> None:
        self.__authors = authors

    @property
    def keywords(self) -> str:
        return self.__keywords

    @keywords.setter
    def keywords(self, keywords: str) -> None:
        self.__keywords = keywords

    @property
    def abstract(self) -> str:
        return self.__abstract

    @abstract.setter
    def abstract(self, abstract: str) -> None:
        self.__abstract = abstract

    @property
    def file_size(self) -> int:
        return self.__file_size

    @file_size.setter
    def file_size(self, file_size: int) -> None:
        self.__file_size = file_size

    @property
    def reviewers(self) -> list:
        return self.__reviewers

    @reviewers.setter
    def reviewers(self, reviewers: list) -> None:
        self.__reviewers = reviewers

    @property
    def status(self) -> str:
        return self.__status

    @status.setter
    def status(self, status: str) -> None:
        self.__status = status

    @property
    def comments(self) -> list:
        return self.__comments

    @comments.setter
    def comments(self, comments: list) -> None:
        self.__comments = comments

    @property
    def cover(self) -> str:
        return self.__cover

    @cover.setter
    def cover(self, cover: str) -> None:
        self.__cover = cover

    # Methods
    def add_comment(self, comment):
        self.__comments.append(comment)

    def update_review_status(self, new_status):
        self.status = new_status

    @classmethod
    def get_all_articles(cls):
        return cls.articles


class Author:
    authors = []

    def __init__(self, first_name: str, last_name: str, email: str, orcid):
        self.__first_name = first_name
        self.__last_name = last_name
        self.__email = email
        self.__orcid = orcid
        Author.authors.append(self)

    @property
    def first_name(self) -> str:
        return self.__first_name

    @first_name.setter
    def first_name(self, first_name: str) -> None:
        self.__first_name = first_name

    @property
    def last_name(self) -> str:
        return self.__last_name

    @last_name.setter
    def last_name(self, last_name: str) -> None:
        self.__last_name = last_name

    @property
    def email(self) -> str:
        return self.__email

    @email.setter
    def email(self, email: str) -> None:
        self.__email = email

    @property
    def orcid(self) -> int:
        return self.__orcid

    @classmethod
    def get_all_authors(cls):
        return cls.authors


class Volume:
    volumes = []

    def __init__(self, name: str) -> None:
        self.__name = name
        self.articles = []
        Volume.volumes.append(self)

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str) -> None:
        self.__name = name

    def add_article(self, article: Article):
        self.articles.append(article)

    def article_count(self):
        return len(self.articles)

    @classmethod
    def get_all_volumes(cls):
        return cls.volumes


class ScientificJournal:
    def __init__(self):
        self.volumes = []

    def add_volume(self, volume: Volume) -> None:
        self.volumes.append(volume)

    def get_articles_by_volume(self, volume: Volume) -> list:
        return [article for article in volume.articles if article.status == "Accepted for publication"]

    def get_articles_by_author(self, author: Author):
        for volume in self.volumes:
            return [article for article in volume.articles if author in article.authors]

    def article_count_by_volume(self, volume: Volume) -> int:
        return volume.article_count()

    def count_volumes_without_repetition(self) -> int:
        unique_volumes = 0
        authors = {}
        for volume in self.volumes:
            for article in volume.articles:
                for author in article.authors:
                    if author not in authors:
                        authors[author] = 1
                    else:
                        authors[author] += 1
            if len(authors.values()) == len(set(authors.values())):
                unique_volumes += 1
        return unique_volumes
