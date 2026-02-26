import CSP_6_02_reading_files as HW
def test_to_string():
    assert HW.test_to_string("test to string.txt")=="Hello\nWorld\n"


def test_longest_line():
    assert HW.longestLine("longest line.txt")==3


def test_to_binary():
    assert HW.toBinary("binary.txt") == ["01010010","01"]
