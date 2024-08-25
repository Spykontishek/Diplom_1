import pytest
from bun import Bun

class TestBun:
    def test_get_name(self):
        bun = Bun("Bulka", 5.5)
        assert bun.get_name() == "Bulka"

    def test_get_price(self):
        bun = Bun("Bulka", 5.5)
        assert bun.get_price() == 5.5

