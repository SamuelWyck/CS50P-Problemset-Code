from plates import is_valid

def test_req1():
    assert is_valid("12") == False

def test_req2():
    assert is_valid("wewewewewe") == False

def test_req3():
    assert is_valid("hello.") == False

def test_req4():
    assert is_valid("he23er") == False

def test_zero():
    assert is_valid("we012") == False
