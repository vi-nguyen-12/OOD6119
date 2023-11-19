from abc import ABC, abstractmethod
from ast import Str
from datetime import datetime
from user import Visitor
from book import Book


# Decorator Pattern

# Abstract component class
class LateFee(ABC):
    @abstractmethod
    def calculate_fee(self, due_date:Str,return_date:Str)-> float:
        pass

# Concrete Component class
class FixedLateFee(LateFee):
    def calculate_fee(self,due_date:Str,return_date:Str) -> float:
        due_date =datetime.strptime(due_date,"%Y-%m-%d")
        return_date =datetime.strptime(return_date,"%Y-%m-%d")
        days_late=(return_date - due_date).days
        if days_late >0:
            return days_late * 0.5
        return 0

# Abstract Decorator class
class LateFeeDecorator(LateFee):
    def __init__(self,decorated: LateFee) ->None:
        self.decorated = decorated

class BestSellerDecorator(LateFeeDecorator):
    def calculate_fee(self, due_date: Str, return_date: Str) -> float:
        fee= self.decorated.calculate_fee(due_date,return_date)
        return fee - 0.5 if fee > 0.5 else 0

class MembershipDecorator(LateFeeDecorator):
    def calculate_fee(self, due_date: Str, return_date: Str) -> float:
        fee= self.decorated.calculate_fee(due_date,return_date)
        return fee - 1 if fee > 1 else 0

# This function applied decorator pattern to caluculate late fee
def calculate_fee (book: Book, visitor: Visitor, due_date:Str, return_date:Str):
    fee= FixedLateFee()
    if book.is_bestseller:
        fee=BestSellerDecorator(fee)
    if visitor.is_member:
        fee=MembershipDecorator(fee)
    return fee.calculate_fee(due_date,return_date)


