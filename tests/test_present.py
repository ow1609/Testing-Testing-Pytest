import pytest 
from lib.present import *

def test_if_contents_is_not_none():
    present = Present()
    present.wrap("toy")
    with pytest.raises(Exception) as e:
        present.wrap("toy")
    error_message = str(e.value)
    assert error_message == "A contents has already been wrapped."