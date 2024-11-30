from app.ingredient import enter_ingredients

def test_enter_ingredients(monkeypatch):    
    monkeypatch.setattr('builtins.input', lambda _: "egg, milk, bread")
    ingredients = enter_ingredients()
    assert ingredients == {"egg", "milk", "bread"}
