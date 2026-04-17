import pytest

def create_username(names):
    return [f"@{name}" for name in names]

def test_create_username():
    names = ["John", "Alice", "Bob"]
    expected_usernames = ["@John", "@Alice", "@Bob"]
    assert create_username(names) == expected_usernames

def test_create_username_empty_list():
    names = []
    expected_usernames = []
    assert create_username(names) == expected_usernames

def test_create_username_single_element():
    names = ["John"]
    expected_usernames = ["@John"]
    assert create_username(names) == expected_usernames
