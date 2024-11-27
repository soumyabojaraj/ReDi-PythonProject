import csv

def load_recipes(file_path):
    """Load recipes from a CSV file."""
    recipes = []
    try:
        with open(file_path, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                recipes.append({
                    "name": row["Recipe_name"],
                    "ingredients": set(row["Ingredients"].split(", ")),
                    "instructions": row["Procedure"]
                })
    except FileNotFoundError:
        print(f"Error: {file_path} not found.")
    return recipes

