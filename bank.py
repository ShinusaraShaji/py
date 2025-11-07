class BankAccount:

    def __init__(self,accno,name,atype,balance):
        self.accno=accno
        self.name=name
        self.atype=atype
        self.balance=balance
    def displayBankAccount(self):
        print("ACCOUNT NUMBER:",self.accno)
        print("NAME:",self.name)
        print("TYPE OF ACCOUNT:",self.atype)
        print("BALANCE:",self.balance)

    def deposit(self,amount):
        self.balance=self.balance+amount
        print("DEPOSITE SUCCESSFULLY...|||")
        print("UPDATED BALANCE:",self.balance)

    def withdraw(self,amount):
        self.balance=self.balance-amount
        print("WITHDRAW SUCCESSFULLY...|||")
        print("UPDATED BALANCE:",self.balance)

accno=input("Enter Account Number:")
name=input("Enter Name")
atype=input("Enter Type of Account:")
balance=float(input("Enter Initial Balance:"))

obj=BankAccount(accno,name,atype,balance)

obj.displayBankAccount()

amt=float(input("Enter amount to deposit:"))
obj.deposit(amt)

amt=float(input("Enter amount to withdraw:"))
obj.withdraw(amt)
