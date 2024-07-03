import pytest
import math

def test_check_floor(input_value):
    assert input_value == math.floor(10.324544)

def test_check_equal(input_value):
    assert 7 == input_value