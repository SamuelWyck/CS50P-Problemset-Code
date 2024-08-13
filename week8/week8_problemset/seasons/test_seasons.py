import pytest
from seasons import age

def test_valid():
    assert age("2002-08-09") == "Eleven million, four hundred seventy-nine thousand, six hundred eighty minutes"

def test_invalid():
    with pytest.raises(SystemExit):
        age("cat")

