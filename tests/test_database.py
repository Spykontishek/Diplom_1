import pytest
from unittest.mock import patch, Mock
from database import Database
from ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


@pytest.fixture
def database():
    """Фикстура для создания экземпляра базы данных перед каждым тестом."""
    return Database()


@pytest.mark.parametrize("bun_name, bun_price", [
    ("black bun", 100),
    ("white bun", 200),
    ("red bun", 300),
])
@patch('bun.Bun')
def test_available_buns(mock_bun, database, bun_name, bun_price):
    mock_bun.return_value = Mock(name=bun_name, price=bun_price)
    buns = database.available_buns()
    assert len(buns) == 3


@pytest.mark.parametrize("ingredient_type, name, price", [
    (INGREDIENT_TYPE_SAUCE, "hot sauce", 100),
    (INGREDIENT_TYPE_SAUCE, "sour cream", 200),
    (INGREDIENT_TYPE_SAUCE, "chili sauce", 300),
    (INGREDIENT_TYPE_FILLING, "cutlet", 100),
    (INGREDIENT_TYPE_FILLING, "dinosaur", 200),
    (INGREDIENT_TYPE_FILLING, "sausage", 300),
])
@patch('ingredient.Ingredient')
def test_available_ingredients(mock_ingredient, database, ingredient_type, name, price):
    mock_ingredient.return_value = Mock(type=ingredient_type, name=name, price=price)
    ingredients = database.available_ingredients()
    assert len(ingredients) == 6

