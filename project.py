
from bank import *

Ashik = BankAccount(1000,"Ashik")
Mohammed= BankAccount(1000,"Mohammed")

Ashik.get_balance()
Mohammed.get_balance()

Ashik.deposit(200)

Ashik.deposit(1300)

Ashik.withdraw(600)

Ashik.transaction(1000,Mohammed)

Tamil = Interestacc(5000 , "Tamil")
Tamil.get_balance()
Tamil.deposit(100)

Arasan =  Savingacc(10000 , "Arasan")
Arasan.get_balance()
Arasan.transaction(10 , Ashik)





