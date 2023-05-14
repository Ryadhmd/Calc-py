import pytest
from calc import *

def test_add():
    assert add(2, 3) == 5
    assert add(0, 0) == 0
    assert add(-1, 1) == 0

def test_subtract():
    assert subtract(2, 3) == -1
    assert subtract(0, 0) == 0
    assert subtract(-1, 1) == -2

def test_multiply():
    assert multiply(2, 3) == 6
    assert multiply(0, 0) == 0
    assert multiply(-1, 1) == -1

def test_divide():
    assert divide(6, 3) == 2
    assert divide(0, 5) == 0
    assert divide(-1, 1) == -1
    with pytest.raises(ValueError):
        divide(5, 0)

def test_power():
    assert power(2, 3) == 8
    assert power(0, 0) == 1
    assert power(-1, 2) == 1

def test_square_root():
    assert square_root(9) == 3
    assert square_root(0) == 0
    with pytest.raises(ValueError):
        square_root(-1)

def test_sin():
    assert math.isclose(sin(math.pi/2), 1, rel_tol=1e-9)

def test_cos():
    assert math.isclose(cos(0), 1, rel_tol=1e-9)

def test_tan():
    assert math.isclose(tan(math.pi/4), 1, rel_tol=1e-9)

def test_log():
    assert math.isclose(log(math.e), 1, rel_tol=1e-9)
    with pytest.raises(ValueError):
        log(0)
        log(-1)

