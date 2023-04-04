import random

class Account(object):
	ID_COUNT = 1

	def __init__(self, name, **kwargs):
		self.__dict__.update(kwargs)

		self.id = self.ID_COUNT
		Account.ID_COUNT += 1
		self.name = name
		if not hasattr(self, 'value'):
			self.value = 0

		if self.value < 0:
			raise AttributeError("Attribute value cannot be negative.")
		if not isinstance(self.name, str):
			raise AttributeError("Attribute name must be a str object.")

	def transfer(self, amount):
		self.value += amount


class Bank(object):
	def __init__(self):
		self.accounts = []

	def add(self, new_account):
		if isinstance(new_account, Account) == False:
			return False
		self.accounts.append(new_account)
		return True

	@staticmethod
	def is_secure(account):
		attr = account.__dict__.keys()
		if len(attr) % 2 or len(list(filter(lambda x: x[0] == 'b', attr))) > 0 \
			or len(list(filter(lambda x : x.startswith('zip') or x.startswith('addr'), attr))) < 1 \
			or set(['name', 'id', 'value']) - set(attr) == 3 or not isinstance(account.name, str) \
			or not isinstance(account.id, int) or not (isinstance(account.value, int) or isinstance(account.value, float)):
			return False
		return True

	def transfer(self, origin, dest, amount):
		if not set([origin.name, dest.name]).issubset([account.name for account in self.accounts]):
			return False
		originAccount = list(filter(lambda x : x.name == origin.name, self.accounts))[0]
		destAccount = list(filter(lambda x : x.name == dest.name, self.accounts))[0]
		if amount < 0 or originAccount.value < amount \
			or not (Bank.is_secure(originAccount) and Bank.is_secure(destAccount)):
			return False
		if origin == dest:
			return True
		originAccount.transfer(-amount)
		destAccount.transfer(amount)
		return True

	def fix_account(self, name):
		if not name in [account.name for account in self.accounts]:
			return False
		account = list(filter(lambda x : x.name == name, self.accounts))[0]
		if isinstance(account.name, str):
			account.name.lstrip('b')
		else:
			account.name = "default" + str(random.randint(1, 100))

		if not isinstance(account.id, int):
			account.id = Account.ID_COUNT
			Account.ID_COUNT += 1
		if not (isinstance(account.value, int) or isinstance(account.value, float)):
			account.value = 0.0
		if len(list(filter(lambda x : x.startswith('zip') or x.startswith('addr'), account.__dict__.keys()))) < 1:
			account.zip = "06200"
		return True