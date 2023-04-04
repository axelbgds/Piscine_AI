from book import Book
from recipe import Recipe

recipe1 = Recipe("test", 2, 25, ["lol"], "", "dessert")
recipe2 = Recipe("booo", 5, 25, ["moza", "rella"], "bodofsdf", "starter")

test = Book("yo")
test.get_recipe_by_name("hahaha")
test.add_recipe(recipe2)
print(test.get_recipes_by_types("lunch"))
print(test.get_recipes_by_types("starter"))
print(test.get_recipe_by_name("booo"))