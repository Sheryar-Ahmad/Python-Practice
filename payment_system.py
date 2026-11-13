from abc import ABC, abstractmethod


class PaymentProcessor(ABC):

    @abstractmethod
    def process_payment(self, amount):
        pass


class BankAccount:

    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount

    def get_balance(self):
        return self.__balance


class CreditCardAccount(BankAccount, PaymentProcessor):

    def __init__(self, owner, balance, credit_limit):
        super().__init__(owner, balance)
        self.credit_limit = credit_limit

    def process_payment(self, amount):
        if amount <= (self.get_balance() + self.credit_limit):
            self.deposit(-amount)
            return True
        return False


class PayPalAccount(BankAccount, PaymentProcessor):

    def __init__(self, owner, balance, email):
        super().__init__(owner, balance)
        self.email = email

    def process_payment(self, amount):
        if amount <= self.get_balance():
            self.deposit(-amount)
            return True
        return False


def make_payment(processor, amount):
    processor.process_payment(amount)


accounts = [
    CreditCardAccount("Alice", 500, 1000),
    PayPalAccount("Bob", 300, "bob@example.com"),
]

for acc in accounts:
    make_payment(acc, 150)
