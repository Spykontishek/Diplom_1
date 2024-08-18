import pytest
from ingredient import Ingredient

class TestIngredient:
    def test_get_price(self):
        ingredient = Ingredient("SAUSE", "ketchup", 3.5)
        assert ingredient.get_price() == 3.5

    def test_get_name(self):
        ingredient = Ingredient("SAUSE", "Ketchup", 3.5)
        assert ingredient.get_name() == "Ketchup"

    def test_get_type(self):
        ingredient = Ingredient("SAUSE", "Ketchup", 3.5)
        assert ingredient.get_type() == "SAUSE"

