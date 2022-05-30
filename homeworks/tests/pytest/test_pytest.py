import pytest
from functions_to_test import Calculator


def test_add():
    assert Calculator.add(4, 9) == 13
    assert Calculator.add(4, 5) == 9


def test_subtract():
    assert Calculator.subtract(10, 9) == 1
    assert Calculator.subtract(4, 2) == 2


def test_multiple():
    assert Calculator.multiply(4, 2) == 8
    assert Calculator.multiply(4, 5) == 20


def test_divide():
    with pytest.raises(ValueError):
        Calculator.divide(60, 0)

    assert Calculator.divide(20, 5) == 4
    assert Calculator.divide(10, 5) == 2
