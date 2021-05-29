from test import deposit


class Account:

    def __init__(self, number, owner, balance, limit):
        print("building object...{}".format(self))
        self.number = number
        self.owner = owner
        self.balance = balance
        self.limit = limit

    def bankStatement(self):
        print("To Mr./Ms. {} \nYour bank balance is: {}".format(self.owner, self.balance))

    def deposit(self, value):
        self.balance = self.balance + value

    def withdraw(self, value):
        self.balance = self.balance - value



