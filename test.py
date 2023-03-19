
def create_account(number, owner, balance, limit):
     account = {"number": number, "owner": owner, "balance": balance, "limit": limit}
     return account


def deposit(account, value):
     account["balance"] += value


def withdraw(account, value):
     account["balance"] -= value


def bank_statement(account):
     print("Your bank balance is: {}".format(account["balance"]))

# ----------------------------------------
# note que se eu colocar no console que o atributo area = 7 ele não
# altera o atributo __area, ele cria um novo atributo publico chamado area
# class Retangulo:

     def __init__(self, x, y):
         self.__x = x
         self.__y = y
         self.__area = x * y

     def obter_area(self):
         return self.__area