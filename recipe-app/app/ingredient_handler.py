def enter_ingredients():
    user_input = input("Enter available ingredients (comma-separated): ")
    ingredients = {item.strip().lower() for item in user_input.split(",")}
    return ingredients
