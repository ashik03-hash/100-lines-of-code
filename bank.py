class BalanceException(Exception):
    pass

class BankAccount:
    def __init__(self,initial_amount,acc_name):
        self.balance = initial_amount
        self.name = acc_name
        print(f"Account '{self.name}' Created. \n Balance = ${self.balance}")

    def get_balance(self):

        print(f"\n Account {self.name} Balance = {self.balance:.2f}")

    def deposit(self,amount):

        self.balance = self.balance + amount
        print("\n Deposit completed")

        self.get_balance()

    def viable_transaction(self,amount):

        if self.balance >= amount:
            return
        else:
            raise BalanceException(f"\n sorry account '{self.name}' only has a balance of {self.balance}")

    def withdraw(self,amount):

        try:
            self.viable_transaction(amount)
            self.balance = self.balance - amount
            print("\n withdrawal is completed")
            self.get_balance()
        
        except BalanceException as error:

            print(f"\n withdrawal interrupted: {error}")

    def transaction(self,amount,account):

        try:
            print("\n Transaction Begins")
            self.viable_transaction(amount)
            self.withdraw(amount)
            account.deposit(amount)
            print("\n Transaction is completed successfully.")
        
        except BalanceException as error:

            print(f"\n Transaction declined:{error} ")

class Interestacc(BankAccount):

    def deposit(self,amount):
        self.balance = self.balance + (amount * 1.05)
        print("\n deposit completed")
        self.get_balance()

class Savingacc(Interestacc):

    def __init__(self,initial_amount,acc_name):
        super().__init__(initial_amount,acc_name)
        self.fee = 5

    def withdraw(self,amount):
        try:
            self.viable_transaction(amount + self.fee)
            self.balance = self.balance - (amount + self.fee )
            print("\n withdrawal completed")
            self.get_balance()
        except  BalanceException as error:

            print(f"\n withdraw interupted: {error}")
