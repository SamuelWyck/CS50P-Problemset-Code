from bank import value

def test_hello():
    assert value("hello") == 0

def test_h():
    assert value("h") == 20

def test_else():
    assert value("what's up?") == 100

def test_case():
    assert value("Hello") == 0

def test_phrase():
    assert value("hello there") == 0

