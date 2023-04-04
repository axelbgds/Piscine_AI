import time
from random import randint
import os

username = os.getenv('USER')

def log(func):
	func_name = " ".join([word.capitalize() for word in func.__name__.split("_")])
	long_op = True if func_name in ["Make Coffee", "Add Water"] else False
	def wrapper(*args, **kwargs):
		fd = open("machine.log", "a")
		start = time.time()
		func(*args, **kwargs)
		execTime = str(round((time.time() - start) * (1 if long_op else 1000), 3)) + ("s" if long_op else "ms")
		fd.write(f"({username})Running: {func_name:20s}[ exec-time = {execTime}]\n")
		return func(*args, **kwargs)
	return wrapper

class CoffeeMachine():
	water_level = 100

	@log
	def start_machine(self):
		if self.water_level > 20:
			return True
		else:
			print("Please add water!")
			return False

	@log
	def boil_water(self):
		return "boiling..."

	@log
	def make_coffee(self):
		if self.start_machine():
			for _ in range(20):
				time.sleep(0.1)
				self.water_level -= 1
			print(self.boil_water())
			print("Coffee is ready!")

	@log
	def add_water(self, water_level):
		time.sleep(randint(1, 5))
		self.water_level += water_level
		print("Blub blub blub...")

if __name__ == "__main__":
	machine = CoffeeMachine()
	for i in range(0, 5):
		machine.make_coffee()
	machine.make_coffee()
	machine.add_water(70)