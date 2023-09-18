from lib.check_codeword import *

def check_first_char():
    result = check_codeword("chicken")
    assert result == "WRONG!"