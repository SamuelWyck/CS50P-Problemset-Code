from fuel import gauge, convert
import pytest


def test_convertValueError():
    with pytest.raises(ValueError):
        convert("3/2")
    #assert convert("3/2") == "no"

def test_convert():
    assert convert("1/2") == 50

def test_convertzero():
    #assert convert("1/0") == "no"
    with pytest.raises(ZeroDivisionError):
        convert("3/0")

def test_gauge_F():
    assert gauge(99) == "F"

def test_gauge_E():
    assert gauge(1) == "E"

def test_gauge():
    assert gauge(50) == "50%"
