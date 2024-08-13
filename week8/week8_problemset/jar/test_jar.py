import pytest
from jar import Jar

def test_init():
    jar = Jar()
    assert jar.capacity == 12

def test_str():
    jar = Jar()
    jar.deposit(3)
    assert str(jar) == "🍪🍪🍪"

def test_deposit():
    jar = Jar(4)
    jar.deposit(3)
    assert jar.size == 3
    with pytest.raises(ValueError):
        jar.deposit(2)

def test_withdraw():
    jar = Jar(4)
    jar.deposit(3)
    jar.withdraw(1)
    assert jar.size == 2
    with pytest.raises(ValueError):
        jar.withdraw(4)

