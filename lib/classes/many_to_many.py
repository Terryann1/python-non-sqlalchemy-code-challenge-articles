from collections import Counter, OrderedDict
class Article:
    all = []

    def __init__(self, author, magazine, title):
        self.title = title  # Use the setter for validation
        self.author = author
        self.magazine = magazine
        author._articles.append(self)
        magazine._articles.append(self)
        Article.all.append(self)

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        if not isinstance(value, str):
            raise Exception("Title must be a string")
        if len(value) < 5 or len(value) > 50:
            raise Exception("Title characters must be between 5 and 50")
        if hasattr(self,"_title"):
            raise Exception("title cannot be changed")
        self._title = value

    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, value):
        if not isinstance(value, Author):
            raise Exception("Author must be an instance of Author")
        self._author = value

    @property
    def magazine(self):
        return self._magazine

    @magazine.setter
    def magazine(self, value):
        if not isinstance(value, Magazine):
            raise Exception("Magazine must be an instance of Magazine")
        self._magazine = value
    
class Author:
    def __init__(self, name):
        self.name = name  # Use the setter for validation
        self._articles = []

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise Exception("Name must be a string")
        if len(value)==0:
            raise Exception("Name must be longer than 0")
        if hasattr(self,"_name"):
            raise Exception("name cannot be changed")
        self._name = value

    def articles(self):
        return self._articles

    def magazines(self):
        return list(OrderedDict.fromkeys(article.magazine for article in self._articles))

    def add_article(self, magazine, title):
        if not isinstance(magazine, Magazine):
            raise Exception("Magazine must be an instance of Magazine")
        new_article = Article(self, magazine, title)
        return new_article

    def topic_areas(self):
        return list({magazine.category for magazine in self.magazines()}) if self._articles else None       
    
class Magazine:
    all = []

    def __init__(self, name, category):
        self.name = name  # Use the setter for validation
        self.category = category  # Use the setter for validation
        self._articles = []
        Magazine.all.append(self)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise Exception("Name must be a string")
        if len(value) < 2 or len(value) > 16:
            raise Exception("Name must be between 2 and 16 characters")
        self._name = value

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, value):
        
        if not isinstance(value, str):
            raise Exception("category must be a string")
            
        if len(value) == 0:
            raise Exception("Category must be longer than 0 character")
        self._category = value

    def articles(self):
        return self._articles

    def contributors(self):
        return list({article.author for article in self._articles})

    def article_titles(self):
        return [article.title for article in self._articles] if self._articles else None

    def contributing_authors(self):
        author_counts = Counter(article.author for article in self._articles)
        return [author for author, count in author_counts.items() if count > 2] or None

    @classmethod
    def top_publisher(cls):
        if not cls.all:
            return None
        return max(cls.all, key=lambda magazine: len(magazine.articles()), default=None)      


    
 