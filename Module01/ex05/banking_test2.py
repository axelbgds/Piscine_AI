from the_bank import Account, Bank

bank = Bank()
account1 = Account("client", value=1500)
account2 = Account("booba")
account3 = Account("zinzin")

bank.add(account1)
bank.add(account2)
bank.fix_account(account1.name)
bank.fix_account(account2.name)
print(bank.transfer(account1, account2, 15))
