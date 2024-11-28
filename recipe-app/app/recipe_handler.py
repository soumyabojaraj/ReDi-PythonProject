import csv

def load_recipes(file_path):
    recipes = []
    try:
        with open(file_path, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                recipes.append({
                    "id":row["Id"],
                    "name": row["Recipe_name"],
                    "ingredients": set(row["Ingredients"].lower().split(", ")),
                    "instructions": row["Procedure"]
                })
    except FileNotFoundError:
        print(f"Error: {file_path} not found.")
    return recipes

def find_recipes(recipes, available_ingredients):
    matched_recipes = []
    for recipe in recipes:
        if recipe["ingredients"].issuperset(available_ingredients):
            matched_recipes.append(recipe)
    return matched_recipes