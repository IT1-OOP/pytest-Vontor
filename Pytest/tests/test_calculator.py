import pytest
from src import calculator

def test_add():
    assert calculator.add(5, 3) == 8

def test_addwrong():
    assert calculator.add_wrong(5, 3) == 8

def test_subtract():
    assert calculator.subtract(10, 4) == 6

def test_multiply():
    assert calculator.multiply(6, 7) == 42

def test_multiplywrong():
    assert calculator.multiply_wrong(6, 7) == 42

def test_divide():
    assert calculator.divide(9, 3) == 3

def test_divide_by_zero():
    with pytest.raises(ValueError, match="Cannot divide by zero!"):
        calculator.divide(10, 0)
