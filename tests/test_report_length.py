from lib.report_length import *

def test_report_length():
    result = report_length("Howdie, partner")
    assert result == 'This string was 15 characters long.'