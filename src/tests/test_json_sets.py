from utils.blacklists import Blacklists
from utils.urlFilter import base

test = Blacklists()


def test_get_first_url():
    assert test.getItems()["urlSet"][0] == "google.com"


def test_get_first_tag():
    assert test.getItems()["tagSet"][0] == "[document]"


def test_add_url():
    url = "test123.com"
    baseUrl = base(url)

    test.addItem(baseUrl, "urlSet")
    assert test.getItems()["urlSet"][-1] == "test123.com"
    test.removeItem(baseUrl, "urlSet")


def test_duplicate_url():
    url = "facebook.com"
    baseUrl = base(url)

    test.addItem(baseUrl, "urlSet")
    assert test.getItems()["urlSet"][-1] != "facebook.com"


def test_add_base_url():
    url = "https://www.pytest.org"
    baseUrl = base(url)

    test.addItem(baseUrl, "urlSet")
    assert test.getItems()["urlSet"][-1] == "pytest.org"
    test.removeItem(baseUrl, "urlSet")


def test_add_tag():
    tag = "p"
    test.addItem(tag, "tagSet")
    assert test.getItems()["tagSet"][-1] == "p"
    test.removeItem(tag, "tagSet")


def add_duplicate_tag():
    tag = "title"
    test.addItem(tag, "tagSet")
    assert test.getItems()["tagSet"][-1] != "title"


def test_remove_tag():
    tag = "div"
    test.addItem(tag, "tagSet")
    test.removeItem(tag, "tagSet")
    assert test.getItems()["tagSet"][-1] != "div"


def test_absent_tag():
    tag = "notreal"
    message = test.removeItem(tag, "tagSet")
    assert message == "notreal not in tag blacklist"
