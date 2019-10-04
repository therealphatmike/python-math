from basic_operations import factorial

def test_factorial_zero():
    assert factorial(0) == 1

def test_factorial_one():
    assert factorial(1) == 1

def test_factorial_fourteen():
    assert factorial(14) == 87178291200