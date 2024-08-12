import pytest
from ingredient import Ingredient


def test_get_price():
    ingredient = Ingredient("SAUSE", "ketchup", 3.5)
    assert ingredient.get_price() == 3.5

def test_get_name():
    ingredient = Ingredient("SAUSE", "Ketchup", 3.5)
    assert ingredient.get_name() == "Ketchup"

def test_get_type():
    ingredient = Ingredient("SAUSE", "Ketchup", 3.5)
    assert ingredient.get_type() == "SAUSE"

