from abc import ABC, abstractmethod
from calendar import c

# Abstract Product
class Book (ABC):
    @abstractmethod
    def __str__ (self):
        pass

# Concrete Products
class KidsBook (Book):
    def __init__(self, name, title, author, category,age_range):
        self.name=name
        self.title=title
        self.author=author
        self.category=category
        self.age_range=age_range
    def __str__ (self):
        return  f"KidsBook(name={self.name}, title={self.title}, author={self.author}, age_range={self.age_range}"

class ScienceFictionBook (Book):
    def __init__(self, name, title, author, category,technology):
        self.name=name
        self.title=title
        self.author=author
        self.category=category
        self.technology=technology
    def __str__ (self):
        return  f"ScienceFictionBook(name={self.name}, title={self.title}, author={self.author}, technology={self.technology}"
class LiteraryBook (Book):
    def __init__(self, name, title, author, category,awards):
        self.name=name
        self.title=title
        self.author=author
        self.category=category
        self.awards=awards
    def __str__ (self):
        return  f"LiteraryBook(name={self.name}, title={self.title}, author={self.author},awards={self.awards}"
class AdventureBook (Book):
    def __init__(self, name, title, author, category,challenges):
        self.name=name
        self.title=title
        self.author=author
        self.category=category
        self.challenges=challenges
    def __str__ (self):
        return  f"KidsBook(name={self.name}, title={self.title}, author={self.author}, challenges={self.challenges}"
class BiographyBook (Book):
    def __init__(self, name, title, author, category,subject):
        self.name=name
        self.title=title
        self.author=author
        self.category=category
        self.subject=subject
    def __str__ (self):
        return  f"KidsBook(name={self.name}, title={self.title}, author={self.author}, subject={self.subject}"
class ComicsBook (Book):
    def __init__(self, name, title, author, category,artist):
        self.name=name
        self.title=title
        self.author=author
        self.category=category
        self.artist=artist
    def __str__ (self):
        return  f"ArtistBook(name={self.name}, title={self.title}, author={self.author}, artist ={self.artist}"

# Abstract factory
class BookCreator(ABC):
    @abstractmethod
    def create_book (self, name, title, author, category, **kwargs):
        pass

# Concrete factory
class KidsCreator(BookCreator):
    def create_book(self,name, title, author, category,ageRange):
        return KidsBook(name, title, author, category,ageRange)
class ScienceFictionCreator(BookCreator):
    def create_book(self,name, title, author, category,technology):
        return ScienceFictionBook(name, title, author, category,technology)
class LiteraryCreator(BookCreator):
    def create_book(self,name, title, author, category,awards):
        return LiteraryBook(name, title, author, category,awards)
class AdventureCreator(BookCreator):
    def create_book(self,name, title, author, category,challenges):
        return AdventureBook(name, title, author, category,challenges)
class BiographyCreator(BookCreator):
    def create_book(self,name, title, author, category,subject):
        return BiographyBook(name, title, author, category,subject)
class ComicsCreator(BookCreator):
    def create_book(self,name, title, author, category,artist):
        return ComicsBook(name, title, author, category,artist)

# Create Concrete Factory based on category
class BookCreatorFactory:
    @staticmethod
    def create_creator (category):
        creator_class_name=f"{category}Creator"
        try:
            creator_class= globals()[creator_class_name]
        except KeyError:
            raise TypeError(f"Invalid category:{category}")
        print("A", creator_class)
        return creator_class()