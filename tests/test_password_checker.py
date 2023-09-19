import pytest
from lib.password_checker import *

def test_if_length_less_than_8():
    password = PasswordChecker()
    with pytest.raises(Exception) as e:
        password.check("cat")
    error_message = str(e.value)
    assert error_message == 'Invalid password, must be 8+ characters.'


def test_if_length_more_than_8():
    password = PasswordChecker()
    result = password.check("catanddog")
    assert result == True


def test_if_password_is_empty_string():
    password = PasswordChecker()
    with pytest.raises(Exception) as e:
        password.check("")
    error_message = str(e.value)
    assert error_message == 'Invalid password, must be 8+ characters.'

def test_if_length_is_equal_to_8():
    password = PasswordChecker()
    result = password.check("12345678")
    assert result == True
