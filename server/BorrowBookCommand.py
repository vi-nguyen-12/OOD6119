from abc import ABC, abstractmethod

# Command interface
class Command(ABC):
    @abstractmethod
    def executte(self):
        pass

# Concrete Command
class BorrowBookCommand(Command):
    def __init__(self, book):
        self.book = book

    def execute(self):
        self.book.borrow()

# Receiver
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.available = True

    def borrow(self):
        if self.available:
            print(f"Borrowing book: {self.title} by {self.author}")
            self.available = False
        else:
            print(f"Sorry, the book {self.title} is not available for borrowing.")

# Client
class User:
    def __init__(self, name):
        self.name = name

    def borrow_book(self, command):
        command.execute()

if __name__ == "__main__":
    # Create a book
    book = Book("The Lord of the Rings", "J.R.R. Talkien")

    # Create a command
    borrow_command = BorrowBookCommand(book)

    # Create a user
    user = User("Aaliyah Thomas")

    # User borrows the book using the command
    user.borrow_book(borrow_command)