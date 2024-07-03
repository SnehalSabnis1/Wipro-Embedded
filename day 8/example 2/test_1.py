import pytest
import math

def test_check_difference(input_value):
    assert 99-93 == input_value
    #assert  input_value == math.floor(8.32454)

def test_check_square_root(input_value):
    assert input_value == math.sqrt(100)
