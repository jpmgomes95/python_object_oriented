
class Account:

    def __init__(self, number, owner, balance, limit):
        print("building object...{}".format(self))
        self.__number = number
        self.__owner = owner
        self.__balance = balance
        self.__limit = limit

    def bankBalance(self):
        print("To Mr./Ms. {} \nYour bank balance is: {}".format(self.__owner, self.__balance))

    def deposit(self, value):
        self.__balance = self.__balance + value

    def withdraw(self, value):
        self.__balance = self.__balance - value

    def transfer(self, value, destiny):
        self.withdraw(value)
        destiny.deposit(value)