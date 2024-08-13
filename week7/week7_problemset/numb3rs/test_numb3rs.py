import pytest
from numb3rs import validate

def test_true():
    assert validate("255.0.3.23") == True

def test_false():
    assert validate("cat") == False
    assert validate("256.23.23.23") == False

def test_first():
    assert validate("3.300.23.23") == False

