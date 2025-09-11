class BankAccount:
    def __init__(self,balance=0):
        self.__balance=balance
    def deposit(self,amount):
        if amount>0:
            self.__balance+=amount
            print(f"deposited: ₹{amount}")
        else:
            print("deposit amount must be positive")
    def withdraw(self,amount):
        if 0<=amount<=self.__balance:
            self.__balance-=amount
            print(f"withdrawn: ₹{amount}")
        else:
            print("insufficient balance or invalid amount")
    def get_balance(self):
        return self.__balance
account=BankAccount()
account.deposit(5000)
account.withdraw(2000)
print("current Balance: ₹",account.get_balance())