import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent.absolute())) 
from urlProcessor.blacklists import Blacklists

test = Blacklists()

def test_get_first_url():
    assert test.getItems()['urlSet'][0] == "www.google.com"

def test_get_first_tag():
    assert test.getItems()['tagSet'][0] == "[document]"

def test_add_url():
    url = "test123.com"
    test.addItem(url, 'urlSet')
    assert test.getItems()['urlSet'][-1] == "test123.com"
    test.removeItem(url, 'urlSet')

def test_remove_tag():
    tag = "div"
    test.addItem(tag, 'tagSet')
    test.removeItem(tag, 'tagSet')
    assert test.getItems()['tagSet'][-1] != "div"

# if __name__ == '__main__':
#     test_remove_tag()