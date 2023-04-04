import sys

class Recipe:
	def __init__(self, name, cooking_lvl, cooking_time, ingredients, description, recipe_type):
		if not (isinstance(name, str) and len(name)):
			sys.exit("Error! Check name parameter")
		if not (isinstance(cooking_lvl, int) and 1 <= cooking_lvl <= 5):
			sys.exit("Error! Check cooking_lvl parameter")
		if not (isinstance(cooking_time, int) and cooking_time >= 0):
			sys.exit("Error! Check cooking_time parameter")
		if not (isinstance(ingredients, list) and len(ingredients) and all(isinstance(elem, str) for elem in ingredients)):
			sys.exit("Error! Check ingredients parameter")
		if not isinstance(description, str):
			sys.exit("Error! Check description parameter")
		if not recipe_type in ["starter", "lunch", "dessert"]: 
			sys.exit("Error! Check type parameter")

		self.name = name
		self.cooking_lvl = cooking_lvl
		self.cooking_time = cooking_time
		self.ingredients = ingredients
		self.description = description
		self.recipe_type = recipe_type

	def __str__(self):
		return "\n".join(["<Recipe Info>",
			"Name: " + self.name, \
			"Recipe Type: " + self.recipe_type, \
			"Cooking Level: " + str(self.cooking_lvl), \
			"Estimated time: " + str(self.cooking_time) + "mins", \
			"Ingredients: " + str(self.ingredients)[1:-1].replace("'", ""), \
			"Description: " + self.description])