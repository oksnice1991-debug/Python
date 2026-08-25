import pytest
from string_utils import StringUtils


@pytest.mark.parametrize("input_text, expected", [
    ("hello", "Hello"),
    ("heLlo", "Hello"),
    ("", ""),
    ("h", "H"),
])
def test_capitalize(input_text, expected):
    string_utils = StringUtils()
    assert string_utils.capitalize(input_text) == expected


@pytest.mark.parametrize("input_text, expected", [
    (" hello", "hello"),
    ("   ", ""),
    ("", ""),
    ("hello", "hello"),
    (" hello ", "hello "),
])
def test_trim(input_text, expected):
    string_utils = StringUtils()
    assert string_utils.trim(input_text) == expected


@pytest.mark.parametrize("string, symbol, expected", [
    ("Hello", "o", True),
    ("Hello", "x", False),
    ("Hello", "", True),
    ("", "", False),
])
def test_contains(string, symbol, expected):
    string_utils = StringUtils()
    assert string_utils.contains(string, symbol) == expected


@pytest.mark.parametrize("string, symbol, expected", [
    ("Hello world", "e", "Hllo world"),
    ("Hello world", "world", "Hello "),
    ("Hello world", "k", "Hello world"),
    ("", "", ""),
])
def test_delete_symbol(string, symbol, expected):
    string_utils = StringUtils()
    assert string_utils.delete_symbol(string, symbol) == expected
