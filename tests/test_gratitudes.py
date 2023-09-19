from lib.gratitudes import *

def test_gratitude():
    gratitude = Gratitudes()
    gratitude.add('the sunny weather')
    gratitude.add('my dog.')

    result = gratitude.format()
    assert result == 'Be grateful for: the sunny weather, my dog.'

