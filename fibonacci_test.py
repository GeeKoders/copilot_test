import pytest
from fibonacci import fibonacci

def test_fibonacci_base_cases():
    assert fibonacci(0) == 0
    assert fibonacci(1) == 1

def test_fibonacci_small_numbers():
    assert fibonacci(2) == 1
    assert fibonacci(3) == 2
    assert fibonacci(4) == 3
    assert fibonacci(5) == 5
    assert fibonacci(6) == 8

def test_fibonacci_negative_and_zero():
    assert fibonacci(-1) == 0
    assert fibonacci(-10) == 0
    assert fibonacci(0) == 0

def test_fibonacci_larger_numbers():
    assert fibonacci(10) == 55
    assert fibonacci(15) == 610

def test_fibonacci_type_error():
    with pytest.raises(TypeError):
        fibonacci("5")
    with pytest.raises(TypeError):
        fibonacci(5.5)