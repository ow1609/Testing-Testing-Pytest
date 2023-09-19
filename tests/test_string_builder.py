from lib.string_builder import *

def test_output():
    string_builder = StringBuilder()
    string_builder.add("added_string")
    result = string_builder.output()
    assert result == "added_string"


def test_size():
    string_builder = StringBuilder()
    string_builder.add("cat")
    result = string_builder.size()
    assert result == 3