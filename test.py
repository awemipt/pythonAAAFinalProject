import finalproject
import pytest
def test_pizza_eq_1():
    assert (finalproject.Pizza() == finalproject.Pizza()) == True


def test_pizza_eq_2():
    assert (finalproject.Pizza() == finalproject.Pizza('Hawaiian')) == False

def test_pizza_eq_3():
    assert (finalproject.Pizza() == 1) != NotImplemented

