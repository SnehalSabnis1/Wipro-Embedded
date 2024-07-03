import pytest
import math

def test_check_floor(input_value):
    assert input_value == math.floor(8.32454)

def test_check_equal(input_value):
    assert 5 == input_value