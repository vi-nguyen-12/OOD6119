from Library import Library
from Book import Book

# Admin class implementing the Observer pattern
class Admin(Observer):
    def __init__(self, name, email):
        self.__name = name
        self.__email = email
        self.__subscribers = []  # List to store subscribers (observers)
        self.library = Library() # Instance of the Library class as the subject

    def addBook(self, book):
        self.library.books.append(book)

    def removeBook(self, book):
        self.library.books.remove(book)

    def updateBook(self, book):
        index = 0
        while index < len(books):
            if self.library.books[index].title == book.title:
                self.library.books[index] = book
            index += 1

    def registerSubscription(self, subscriber):
        if subscriber not in self.__subscribers:
            self.__subscribers.append(subscriber) # Adding a subscriber to the list

    def unregisterSubscription(self, subscriber):
        self.__subscribers.remove(subscriber) # Removing a subscriber from the list

    def notifySubscriber(self, message):
        for subscriber in self.__subscribers:
            subscriber.update(message) # Notifying all subscribers by calling the update method

    def update(self, message):
        print(f"{self.__name} received notification: {message}") # Handling the update from the subject

