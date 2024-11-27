from app.recipe_handler import load_recipes
from app.ingredient_handler import enter_ingredients

ingredients = enter_ingredients()
print(ingredients)

# RECIPE_FILE = "data/recipes.csv"
# recipe_list = load_recipes(RECIPE_FILE)
# print(recipe_list)


