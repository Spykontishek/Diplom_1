import pytest
from unittest.mock import patch, Mock
from database import Database
from ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


class TestDataBase:
    @pytest.fixture
    def database(self):
        return Database()

    @pytest.mark.parametrize("bun_name, bun_price", [
        ("black bun", 100),
        ("white bun", 200),
        ("red bun", 300),
    ])
    @patch('bun.Bun')
    def test_available_buns(self, mock_bun, database, bun_name, bun_price):
        # Создаем экземпляр мок-бун
        mock_bun_instance = Mock(name=bun_name, price=bun_price)
        mock_bun.return_value = mock_bun_instance

        # Настраиваем метод available_buns для возврата списка мок-бунов
        database.available_buns = Mock(return_value=[mock_bun_instance] * 3)

        buns = database.available_buns()
        assert len(buns) == 3
        assert all(bun.price == bun_price for bun in buns)

    @pytest.mark.parametrize("ingredient_type, name, price", [
        (INGREDIENT_TYPE_SAUCE, "hot sauce", 100),
        (INGREDIENT_TYPE_SAUCE, "sour cream", 200),
        (INGREDIENT_TYPE_SAUCE, "chili sauce", 300),
        (INGREDIENT_TYPE_FILLING, "cutlet", 100),
        (INGREDIENT_TYPE_FILLING, "dinosaur", 200),
        (INGREDIENT_TYPE_FILLING, "sausage", 300),
    ])
    @patch('ingredient.Ingredient')
    def test_available_ingredients(self, mock_ingredient, database, ingredient_type, name, price):
        # Создаем экземпляр мок-ингредиента
        mock_ingredient_instance = Mock(type=ingredient_type, name=name, price=price)

        # Настраиваем метод available_ingredients для возврата списка мок-ингредиентов
        database.available_ingredients = Mock(return_value=[
            Mock(type=INGREDIENT_TYPE_SAUCE, name="hot sauce", price=100),
            Mock(type=INGREDIENT_TYPE_SAUCE, name="sour cream", price=200),
            Mock(type=INGREDIENT_TYPE_SAUCE, name="chili sauce", price=300),
            Mock(type=INGREDIENT_TYPE_FILLING, name="cutlet", price=100),
            Mock(type=INGREDIENT_TYPE_FILLING, name="dinosaur", price=200),
            Mock(type=INGREDIENT_TYPE_FILLING, name="sausage", price=300),
        ])

        ingredients = database.available_ingredients()
        assert len(ingredients) == 6
        assert all(ingredient.price in [100, 200, 300] for ingredient in ingredients)

