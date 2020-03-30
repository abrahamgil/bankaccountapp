#classes used in OOP

class Account:
    #method
    def __init__(self, filepath): #constructor
        self.tempfilepath=filepath #object instance  to be used everywhere in class
        with open(filepath,'r') as file:
            self.balance=int(file.read())

    def withdraw(self, amount):
        self.balance=self.balance - amount

    def deposit(self, amount):
        self.balance=self.balance + amount
  
    def commit(self):
        with open(self.tempfilepath, 'w') as file:
            file.write(str(self.balance))


class Checking(Account):
    """This class generates checking account objects"""
    type="checking" #class variable

    def __init__(self, filepath, fee):
        Account.__init__(self, filepath)
        self.fee=fee

    def transfer(self, amount): #method
        self.balance=self.balance - amount - self.fee

jack_checking=Checking("jack.txt", 1)
jack_checking.transfer(100)
print(jack_checking.balance)
jack_checking.commit()
print(jack_checking.type)

john_checking=Checking("john.txt", 1)
john_checking.transfer(100)
print(john_checking.balance)
john_checking.commit()
print(john_checking.type)

print(john_checking.__doc__)