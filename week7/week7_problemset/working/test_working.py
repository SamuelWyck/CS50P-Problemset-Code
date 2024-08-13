import pytest
from working import convert

def test_invalid():
    with pytest.raises(ValueError):
        convert("12:60 AM to 13:00 PM")

def test_valid():
    assert convert("9 AM to 5:32 PM") == "09:00 to 17:32"

def test_times():
    assert convert("12:43 PM to 9 AM") == "12:43 to 09:00"

def test_to():
    with pytest.raises(ValueError):
        convert("12:60 AM 13:00 PM")
