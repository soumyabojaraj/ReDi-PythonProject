from app.recipe_handler import load_recipes, find_recipes
from app.ingredient_handler import enter_ingredients
RECIPE_FILE = "data/recipes.csv"

if __name__ == "__main__":
    # ask user to enter available ingredients
    user_ingredients = enter_ingredients()
    # load the recipes data (from csv file)
    recipes = load_recipes(RECIPE_FILE)

    matched_recipes = find_recipes(recipes,user_ingredients)
    print(len(matched_recipes))


