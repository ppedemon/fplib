import pytest
from fplib.curry import curry

@curry
def add3(x, y, z):
    return x + y + z

def test_curry_0():
    assert 6 == add3(1, 2, 3)

def test_curry_1():
    assert 6 == add3(1, 2)(3)

def test_curry_2():
    assert 6 == add3(1)(2, 3)

def test_curry_3():
    assert 6 == add3(1)(2)(3)

def test_too_many_args():
    with pytest.raises(TypeError):
        add3(1, 2, 3, 4)
