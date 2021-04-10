import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent.absolute()))
from browserHistory.getHistory import GetHistory
import pytest


def test_capitalise():
    browser = 'opera'
    assert browser.capitalize() == 'Opera'


def test_getHistory():
    filtr = ''
    browser = 'opera'
    history = GetHistory().getHistory(filtr, browser.capitalize())
    assert history is not None


def test_filtr_hello():
    with pytest.raises(ValueError):
        filtr = 'hello'
        browser = 'opera'
        GetHistory().getHistory(filtr, browser)


def test_filtr_3weeks():
    try:
        filtr = '3 weeks'
        browser = 'chrome'
        GetHistory().getHistory(filtr, browser)
        assert False
    except ValueError:
        assert True


def test_browser():
    with pytest.raises(ValueError):
        filtr = 'day'
        browser = 'google'
        GetHistory().getHistory(filtr, browser)
