class BalanceException(Exception):
    pass

class BankAccount:
    def __init__(self,initial_Balance,Account_Holder_Name):
        self.balance = initial_Balance
        self.name = Account_Holder_Name
        print(f"\nAccount '{self.name}' created. \nbalance =  ${self.balance:.2f}")

    def get_Balance(self):
        print(f"\nAccount '{self.name}' \nBalance = ${self.balance:.2f}")

    def amount_Deposit(self,amount):
        self.balance += amount
        print("\nDeposit Complete")
        self.get_Balance()

    def viable_Transaction(self,amount):
        if self.balance >= amount:
            return
        else:
            raise BalanceException(
                f"\nSorry account '{self.name}' only has a balance of ${self.balance:.2f}"
            )
        
    def amount_withdraw(self,amount):
        try:
            self.viable_Transaction(amount)
            self.balance = self.balance - amount
            print("\nWithdraw Complete")
            self.get_Balance()
        except BalanceException as error:
            print(f"\nWithdraw intrupted : {error}")

    def amount_Transfer(self,amount,account):
        try:
            print("\n***************\n\nBeginning Transfer...🚀")
            self.viable_Transaction(amount)
            self.amount_withdraw(amount)
            account.amount_Deposit(amount)
            print("\nTrasfer Complete! ✅\n\n***************")
        except BalanceException as error:
            print(f"\nTransfer intrupted:❌ ${error}")



class interestRewards_BankAccount(BankAccount):
    def amount_Deposit(self, amount):
        self.balance = self.balance +(amount * 1.05) 
        print("\nDeposit Complete")
        self.get_Balance()

class Savings_BankAccount(interestRewards_BankAccount):
    def __init__(self, initial_Balance, Account_Holder_Name):
        super().__init__(initial_Balance, Account_Holder_Name)
        self.fee = 5

    def amount_withdraw(self, amount):
        try:
            self.viable_Transaction(amount + self.fee)
            self.balance = self.balance - (amount + self.fee)
            print("\nWithdraw Complete")
            self.get_Balance()
        except BalanceException as error:
            print(f"\nWithdraw intrupted : {error}")
        
            
        