from app.recipe_handler import load_recipes, find_recipes
from app.ingredient_handler import enter_ingredients

if __name__ == "__main__":
    file_path = "data/recipes.csv"
    recipes = load_recipes(file_path)

    while True:
        print("\nMenu:")
        print("1. Find Recipes")
        print("2. Exit")
        choice = input("Enter your choice: ")
        
        if choice == "1":
            available_ingredients = enter_ingredients()
            matched_recipes = find_recipes(recipes, available_ingredients)
            if matched_recipes:
                print("Recommended Recipes:")
                for recipe in matched_recipes:
                    print(f"{recipe['id']}- {recipe['name']}")
                print("\nSelect a recipe to view details:")
                selected_recipe = input("Enter recipe number: ")
                recipe_details = next((r for r in matched_recipes if r["id"] == selected_recipe), None)
                if recipe_details:
                    print(f"\nRecipe: {recipe_details['name']}")
                    print(f"Ingredients: {', '.join(recipe_details['ingredients'])}")
                    print(f"Instructions: {recipe_details['instructions']}")
                else:
                    print("Recipe not found.")
            else:
                print("No matching recipes found.")
        elif choice == "2":
            print("Bon apetite!")
            break
        else:
            print("Invalid choice. Please try again.")




