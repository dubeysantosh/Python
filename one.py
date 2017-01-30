class Account:
    def __init__(self, acctNumber, balance):
        self.acctNumber = acctNumber
        self.balance = balance

    def __str__(self):
        return "Account number: " + str(self.acctNumber)  + "\n" +\
            "Balance: " + str(self.balance)

class Checking(Account):
    def __init__(self, acctNumber , balance, fee):
        Account.__init__(self, acctNumber, balance)
        self.fee = fee

    def __str__(self):
        retStr = "Account Type : Checking \n";
        retStr += Account.__str__(self)
        return retStr

    def getFee(self):
        return self.fee

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self,amount):
         if amount > self.balance:
             print("Insuffiecnt funds")
         else:
             self.balance = self.balance - amount -self.fee

class Savings:
    def __init__(self, acctNumber, balance ):
        Account.__init__(acctNumber, balance);

    def __str__(self):
        retStr = "Account type : Savings \n/"
        retStr += Account.__str__(self)
        return retStr

    def deposit(self, amount):
        self.balance += amount

    def  withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds.")
        else:
            self.balance = self.balance - amount


ca = Checking("123", 500, .50)
print(ca)

ca.withdraw(100)

print(ca)

ca.deposit(200)
print(ca)

sa = Savings("456", 1000)
print (sa)
sa.withdraw(250)
sa.deposit(125)
print(sa)



