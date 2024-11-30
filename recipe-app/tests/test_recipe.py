import pytest
from app.recipe import load_recipes, find_recipes


def test_load_recipes():
    csv_file = "data/recipes.csv"
    recipes = load_recipes(csv_file)
    assert len(recipes) == 5
    assert recipes[0]["name"] == "Beans curry"

def test_find_recipes():
    csv_file = "data/recipes.csv"
    recipes = load_recipes(csv_file)
    available_ingredients = { "potato" }

    matched_recipes = find_recipes(recipes,available_ingredients)

    assert len(matched_recipes) == 2
    assert matched_recipes[0]["ingredients"] == {'beans', 'oil', 'potato', 'spices', 'tomato'}

