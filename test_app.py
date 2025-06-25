from app import add, subtract

def test_add():
    assert add(2, 3) == 5

def test_subtract():
    assert subtract(10, 4) == 6

def test_subtract1():
    assert subtract(10, 4) == 3

def test_fail():
    assert subtract(5, 5) == 0  # This will FAIL on purpose to show red test

def test_fail1():
    assert subtract(5, 5) == 5