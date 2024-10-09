from oop_bank import * 

Ashik = BankAccount(1000,"Ashik")
Prasanna = BankAccount(2000,"Prasanna")
# Prasanna.get_Balance()
# Ashik.get_Balance()
# Ashik.amount_Deposit(100)
# Ashik.amount_withdraw(200)

Ashik.amount_Transfer(200,Prasanna)


Nizanth = interestRewards_BankAccount(1000,"Nizzanth")
Nizanth.get_Balance()
Nizanth.amount_Deposit(2000)

Praveen = Savings_BankAccount(100,"Praveen")
Praveen.get_Balance()
Praveen.amount_withdraw(5)
Praveen.amount_Transfer(5,Ashik)

