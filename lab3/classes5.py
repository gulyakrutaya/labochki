
class BankAccount:

    def __init__(self, owner, balance):
        self.owner=owner
        self.balance=balance
    
    def deposit(self, deposit_value):
        self.balance=self.balance+deposit_value
        return str(self.owner)+", after deposit your current balance is "+str(self.balance)

    def withdraw(self, withdraw_value):
        self.balance=self.balance-withdraw_value

        if self.balance<0:
            print("Withdrawals may not exceed the available balance")
            self.balance=self.balance+withdraw_value

        return str(self.owner)+", after withdraw your current balance is "+str(self.balance)


ba1_owner=input("enter the owner of the 1 account: ")
ba1_balance=float(input("enter the balance of 1 account: "))

ba1=BankAccount(ba1_owner, ba1_balance)

ba2_owner=input("enter the owner of the 2 account: ")
ba2_balance=float(input("enter the balance of 2 account: "))

ba2=BankAccount(ba2_owner, ba2_balance)

ba3_owner=input("enter the owner of the 3 account: ")
ba3_balance=float(input("enter the balance of 3 account: "))

ba3=BankAccount(ba3_owner, ba3_balance)


print(ba1.deposit(200))
print(ba1.withdraw(1000))

print(ba2.deposit(3000))
print(ba2.withdraw(500))

print(ba3.deposit(10))
print(ba3.withdraw(0))
