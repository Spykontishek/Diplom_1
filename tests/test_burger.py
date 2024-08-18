import pytest
from burger import Burger
from bun import Bun
from ingredient import Ingredient

class TestIngredient:
    def test_set_buns(self):
        burger = Burger()
        bun = Bun("Bulka", 5.5)
        burger.set_buns(bun)
        assert burger.bun == bun

    def test_add_ingredient(self):
        burger = Burger()
        ingredient = Ingredient("SAUSE", "Ketchup", 3.5)
        burger.add_ingredient(ingredient)
        assert burger.ingredients == [ingredient]

    def test_remove_ingredient(self):
        burger = Burger()
        ingredient = Ingredient("SAUSE", "Ketchup", 3.5)
        burger.add_ingredient(ingredient)
        burger.remove_ingredient(0)
        assert burger.ingredients == []

    def test_move_ingredient(self):
        burger = Burger()
        ingredient1 = Ingredient("FILLING", "Cheese", 2.5)
        ingredient2 = Ingredient("Sauce", "Ketchup", 3.5)
        burger.add_ingredient(ingredient1)
        burger.add_ingredient(ingredient2)
        burger.move_ingredient(1, 0)
        assert burger.ingredients == [ingredient2, ingredient1]

    def test_get_price(self):
        burger = Burger()
        bun = Bun("Bulka", 5.5)
        ingredient1 = Ingredient("Filling", "Cheese", 2.5)
        ingredient2 = Ingredient("Sauce", "Ketchup", 3.5)
        burger.set_buns(bun)
        burger.add_ingredient(ingredient1)
        burger.add_ingredient(ingredient2)
        assert burger.get_price() == 17.0

    def test_get_receipt(self):
        burger = Burger()
        bun = Bun("Bulka", 5.5)
        ingredient1 = Ingredient("Filling", "Cheese", 2.5)
        ingredient2 = Ingredient("Sauce", "Ketchup", 3.5)
        burger.set_buns(bun)
        burger.add_ingredient(ingredient1)
        burger.add_ingredient(ingredient2)
        receipt = burger.get_receipt()
        assert receipt == '(==== Bulka ====)\n= filling Cheese =\n= sauce Ketchup =\n(==== Bulka ====)\n\nPrice: 17.0'

