from app.recipe_handler import load_recipes
RECIPE_FILE = "data/recipes.csv"
recipe_list = load_recipes(RECIPE_FILE)
print(recipe_list)