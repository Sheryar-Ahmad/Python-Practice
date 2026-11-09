class BankAccount:
    def __init__(self, account_holder, initial_balance):
        self.account_holder = account_holder
        self.__balance = initial_balance

    def get_balance(self):
        return self.__balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(self.account_holder + f" successfully deposited Rs. {amount}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(self.account_holder + f" successfully withdrew Rs. {amount}")
        elif amount > self.__balance:
            print("Insufficient funds!")
        else:
            print("Withdrawal amount must be positive.")


account = BankAccount("Zayn", 10000)

print(account.account_holder)
print(f"Current Balance: Rs. {account.get_balance()}")

account.deposit(5000)
account.withdraw(3000)

print(f"Final Balance: Rs. {account.get_balance()}")

account.withdraw(20000)
