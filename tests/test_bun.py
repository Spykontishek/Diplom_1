import pytest
from bun import Bun


def test_get_name():
    bun = Bun("Bulka", 5.5)
    assert bun.get_name() == "Bulka"

def test_get_price():
    bun = Bun("Bulka", 5.5)
    assert bun.get_price() == 5.5

