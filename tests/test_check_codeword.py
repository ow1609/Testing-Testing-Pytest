from lib.check_codeword import *

def test_first_char_not_h():
    result = check_codeword("chicken")
    assert result == "WRONG!"

def test_last_char_not_e():
    result = check_codeword("penguin")
    assert result == "WRONG!"

def test_word_is_horse():
    result = check_codeword('horse')
    assert result == "Correct! Come in."

def test_first_letter_h_and_last_letter_e_but_not_horse():
    result = check_codeword('house')
    assert result == "Close, but nope."