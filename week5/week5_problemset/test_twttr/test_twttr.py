from twttr import shorten

def test_argument():
    assert shorten("All their would") == "ll thr wld"

def test_num():
    assert shorten("123") == "123"

def test_punc():
    assert shorten("hello,.") == "hll,."
