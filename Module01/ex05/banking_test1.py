from the_bank import Account, Bank

bank = Bank()
account1 = Account("client", value=1500)
account2 = Account("booba")
account3 = Account("zinzin")

print(account1.value)
bank.add(account1)
print(bank.transfer(account1, account2, 15))
bank.add(account2)
print(bank.transfer(account1, account2, 15))
