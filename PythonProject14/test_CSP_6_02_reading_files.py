import CSP_6_02_reading_files as HW
def test_to_string():
    assert HW.toString("test_to_string.txt")=="Hello\nWorld"


def test_longest_line():
    assert HW.longestLine("longest_line.txt")=="ewewewewewweew"


def test_to_binary():
    assert HW.toBinary("binary.txt") == ["01010101","010"]
