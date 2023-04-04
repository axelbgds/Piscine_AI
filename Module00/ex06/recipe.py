import sys

cookbook = {"Sandwich" : {
	"ingredients": ["ham", "bread", "tomatoes"],
	"meal": "lunch",
	"prep_time": 10
}, "Cake": {
	"ingredients": ["flour", "sugar", "eggs"],
	"meal": "dessert",
	"prep_time": 60
}, "Salade": {
	"ingredients": ["avocado", "arugula", "tomatoes", "spinach"],
	"meal": "lunch",
	"prep_time": 15
}}

def printRecipeNames():
	print("Available recipes:", ', '.join(str(key) for key in cookbook.keys()))

def printAllRecipe():
	print("Available recipes with detail:\n -", '\n - '.join(str(key) + "\n   "
		+ ('\n   '.join(str(x) + ': ' + str(y) for x, y in value.items()))
 		for key, value in cookbook.items()))

def getRecipeDetail(recipe):
	if recipe in cookbook.keys():
		print("Ingredients list: {}\nTo be eaten for {}.\nTakes {} minutes of cooking.".format(
			cookbook[recipe]["ingredients"], cookbook[recipe]["meal"], cookbook[recipe]["prep_time"]
		))
	else:
		print("Recipe not in the cookbook!")

def deleteRecipe(recipe):
	if recipe in cookbook.keys():
		cookbook.pop(recipe)
		print("Recipe successfully removed from the cookbook")
	else:
		print("Recipe doesn't exist in the cookbook")

def addRecipe():
	ingredients = []

	while True:
		name = input(">>> Enter a name: ")
		if name:
			break
	while True:
		ingre = input(">>> Enter ingredients: " if not len(ingredients) else "")
		if not ingre and len(ingredients):
			break
		if ingre:
			ingredients.append(ingre)
	while True:
		meal = input(">>> Enter a meal type: ")
		if meal:
			break
	while True:
		prep_time = input(">>> Enter a preparation time: ")
		if prep_time and prep_time.isdigit():
			break

	cookbook[name] = {
		"ingredients": ingredients, 
		"meal": meal, 
		"prep_time": prep_time
	}

if __name__ == "__main__":
	print('''Welcome to the Python Cookbook !
	List of available option:
	1: Add a recipe
	2: Delete a recipe
	3: Print a recipe
	4: Print the cookbook
	5: Quit''')

	while True:
		option = input('Please select an option: \n')
		if option == '1':
			addRecipe()
		elif option == '2':
			recipe = input("Please enter the name of the recipe you want to delete\n>>> ")
			deleteRecipe(recipe)
		elif option == '3':
			recipe = input("Please enter a recipe name to get its detail\n>>> ")
			getRecipeDetail(recipe)
		elif option == '4':
			printRecipeNames()
		elif option == '5':
			sys.exit("Bye bye~")
		print()

printAllRecipe()