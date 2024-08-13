from um import count
import pytest

def test_middle():
    assert count("um thanks yummy") == 1

def test_um():
    assert count("um, thanks um.....") == 2

def test_end():
    assert count("yummy, um") == 1

def test_case():
    assert count("UM") == 1

