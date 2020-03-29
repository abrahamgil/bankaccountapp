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

account=Account("balance.txt")
print(account.balance)
account.withdraw(100)
print(account.balance)
account.commit()
