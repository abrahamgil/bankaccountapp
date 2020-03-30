#classes used in OOP

class Account:
    #method
    def __init__(self, filepath):
        self.tempfilepath=filepath #instance variable to be used everywhere in class
        with open(filepath,'r') as file:
            self.balance=int(file.read()) #attribute

    def withdraw(self, amount):
        self.balance=self.balance - amount

    def deposit(self, amount):
        self.balance=self.balance + amount
  
    def commit(self):
        with open(self.tempfilepath, 'w') as file:
            file.write(str(self.balance))

#inherits the Account class
class Checking(Account):

    def __init__(self, filepath, fee):
        Account.__init__(self, filepath)
        self.fee=fee

    def transfer(self, amount):
        self.balance=self.balance - amount - self.fee

checking=Checking("balance.txt", 1)
checking.transfer(110)
print(checking.balance)
checking.commit()
    