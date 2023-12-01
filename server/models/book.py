from abc import ABC, abstractmethod
import sys
sys.path.append('../')

# Abstract Product
class Book (ABC):
    def __init__(self,  title, author, category,is_bestseller):
        self.title = title
        self.author = author
        self.category = category
        self.is_bestseller = is_bestseller
    @abstractmethod
    def __str__ (self):
        pass
    @abstractmethod
    def save_to_db(self):
        pass

# Concrete Products
class KidsBook (Book):
    def __init__(self, title, author, category, is_bestseller, age_range):
        super().__init__( title, author, category,is_bestseller)
        self.age_range=age_range
    def __str__ (self):
        return  f"KidsBook( title={self.title}, author={self.author}, age_range={self.age_range}"
    def save_to_db(self):
        from main import db_connection
        query="INSERT INTO books (title, author, category, is_bestseller, age_range) VALUES(%s, %s, %s, %s, %s)"
        data=(self.title, self.author, self.category, self.is_bestseller, self.age_range)  
        db_connection.execute_query(query, data)

class ScienceFictionBook (Book):
    def __init__(self,  title, author, category,is_bestseller,technology):
        super().__init__( title, author, category,is_bestseller)
        self.technology=technology
    def __str__ (self):
        return  f"ScienceFictionBook(title={self.title}, author={self.author}, technology={self.technology}"
    def save_to_db(self):
        from main import db_connection
        query="INSERT INTO books (title, author, category, is_bestseller, technology) VALUES(%s, %s, %s, %s, %s)"
        data=(self.title, self.author, self.category, self.is_bestseller, self.technology)  
        db_connection.execute_query(query, data)
class LiteraryBook (Book):
    def __init__(self,  title, author, category,is_bestseller,awards):
        super().__init__( title, author, category,is_bestseller)
        self.awards=awards
    def __str__ (self):
        return  f"LiteraryBook( title={self.title}, author={self.author},awards={self.awards}"
    def save_to_db(self):
        from main import db_connection
        query="INSERT INTO books (title, author, category, is_bestseller, awards) VALUES(%s, %s, %s, %s, %s)"
        data=(self.title, self.author, self.category, self.is_bestseller, self.awards)  
        db_connection.execute_query(query, data)
class AdventureBook (Book):
    def __init__(self,  title, author, category,is_bestseller,challenges):
        super().__init__( title, author, category,is_bestseller)
        self.challenges=challenges
    def __str__ (self):
        return  f"AdventureBook( title={self.title}, author={self.author}, challenges={self.challenges}"
    def save_to_db(self):
        from main import db_connection
        query="INSERT INTO books (title, author, category, is_bestseller, challenges) VALUES(%s, %s, %s, %s, %s)"
        data=(self.title, self.author, self.category, self.is_bestseller, self.challenges)  
        db_connection.execute_query(query, data)
class BiographyBook (Book):
    def __init__(self,  title, author, category,is_bestseller,subject):
        super().__init__(title, author, category, is_bestseller)
        self.subject=subject
    def __str__ (self):
        return  f"BiographyBook(title={self.title}, author={self.author}, subject={self.subject}"
    def save_to_db(self):
        from main import db_connection
        query="INSERT INTO books (title, author, category, is_bestseller, subject) VALUES(%s, %s, %s, %s, %s)"
        data=(self.title, self.author, self.category, self.is_bestseller, self.subject)  
        db_connection.execute_query(query, data)
class ComicsBook (Book):
    def __init__(self, title, author, category,is_bestseller,artist):
        super().__init__( title, author, category,is_bestseller)
        self.artist=artist
    def __str__ (self):
        return  f"ComicsBook(title={self.title}, author={self.author}, artist ={self.artist}"
    def save_to_db(self):
        from main import db_connection
        query="INSERT INTO books (title, author, category, is_bestseller, artist) VALUES(%s, %s, %s, %s, %s)"
        data=(self.title, self.author, self.category, self.is_bestseller, self.artist)  
        db_connection.execute_query(query, data)

# Abstract factory
class BookCreator(ABC):
    @abstractmethod
    def create_book (self, title, author, category, is_bestseller,**kwargs):
        pass

# Concrete factory
class KidsCreator(BookCreator):
    def create_book(self, title, author, category,is_bestseller,ageRange):
        return KidsBook( title, author, category,is_bestseller,ageRange)
class ScienceFictionCreator(BookCreator):
    def create_book(self,title, author, category,is_bestseller,technology):
        return ScienceFictionBook( title, author, category,is_bestseller,technology)
class LiteraryCreator(BookCreator):
    def create_book(self,title, author, category,is_bestseller,awards):
        return LiteraryBook( title, author, category,is_bestseller,awards)
class AdventureCreator(BookCreator):
    def create_book(self, title, author, category,is_bestseller,challenges):
        return AdventureBook( title, author, category,is_bestseller,challenges)
class BiographyCreator(BookCreator):
    def create_book(self, title, author, category,is_bestseller,subject):
        return BiographyBook(title, author, category,is_bestseller,subject)
class ComicsCreator(BookCreator):
    def create_book(self,title, author, category,is_bestseller,artist):
        return ComicsBook(title, author, category,is_bestseller,artist)

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