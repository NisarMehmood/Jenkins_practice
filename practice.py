#create a ATM class
class ATM:
    def __init__(self, balance):
        self.balance = balance

    def withdraw(self):
        self.balance = 0

    def deposit(self, amount):
        self.balance += amount
