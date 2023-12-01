from abc import ABC, abstractmethod
from ast import Str
from datetime import datetime, timedelta

# [Decorator Pattern]
# Abstract component class
class LateFee(ABC):
    @abstractmethod
    def calculate_fee(self, due_date:Str,return_date:Str)-> float:
        pass

# [Decorator Pattern]
# Concrete Component class
class FixedLateFee(LateFee):
    def calculate_fee(self,due_date:Str,return_date:Str) -> float:
        due_date =datetime.strptime(due_date,"%Y-%m-%d")
        return_date =datetime.strptime(return_date,"%Y-%m-%d")
        days_late=(return_date - due_date).days
        if days_late >0:
            return days_late * 0.5
        return 0

# [Decorator Pattern]
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
    
# [Decorator Pattern]
# This function applied decorator pattern to caluculate late fee:
# Decorate the LateFee class
# if book is bestseller, apply BestSellerDecorator
# if visitor is member, apply MembershipDecorator
def calculate_fee (borrow_date:Str, return_date:Str, is_member:bool, is_bestseller:bool) -> int:
    due_date =datetime.strptime(borrow_date,"%Y-%m-%d")+timedelta(days=15)
    due_date_str=due_date.strftime("%Y-%m-%d")
    fee= FixedLateFee()
    if is_bestseller:
        fee=BestSellerDecorator(fee)
    if is_member:
        fee=MembershipDecorator(fee)
    return fee.calculate_fee(due_date_str,return_date)


