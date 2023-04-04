import sys, functools
from datetime import datetime

class Book:
	def __init__(self, name):
		if not (isinstance(name, str) and len(name)):
			sys.exit("Error! Check the name parameter")

		self.name = name
		now = datetime.now()
		self.creation_date = now.strftime("%Y-%m-%d %H:%M:%S")
		self.last_update = now.strftime("%Y-%m-%d %H:%M:%S")
		self.recipe_list = dict.fromkeys(["starter", "lunch", "dessert"], dict())

	def get_recipe_by_name(self, name):
		all_recipes = functools.reduce(lambda a, b: a | b, self.recipe_list.values())
		if name not in all_recipes:
			return print("Error! Recipe doesn't exist")
		return all_recipes[name]

	def get_recipes_by_types(self, recipe_type):
		if recipe_type not in ["starter", "lunch", "dessert"]:
			return print("Error! Wrong recipe type")
		if not len(self.recipe_list[recipe_type].keys()):
			return print("Error! No recipe in recipe_type")
		return list(self.recipe_list[recipe_type].keys())

	def add_recipe(self, recipe):
		if recipe.name in functools.reduce(lambda a, b: a | b, self.recipe_list.values()):
			return print("Error! Already existing recipe")
		self.recipe_list[recipe.recipe_type][recipe.name] = recipe
		self.last_update = datetime.now().strftime("%Y-%m-%d %H:%M:%S")