import sys
from pathlib import Path

from browserHistory.getHistory import GetHistory

sys.path.append(str(Path(__file__).parent.parent.absolute()))


def test_capitalise():
    browser = "opera"
    assert browser.capitalize() == "Opera"


def test_getHistory():
    filtr = ""
    browser = "opera"
    history = GetHistory().getHistory(filtr, browser.capitalize())
    assert history is not None


def test_filtr_hello():
    filtr = "hello"
    browser = "opera"
    result = GetHistory().getHistory(filtr, browser)
    assert len(result) == 0


def test_filtr_3weeks():
    filtr = "3 weeks"
    browser = "chrome"
    result = GetHistory().getHistory(filtr, browser)
    assert result == {}


def test_browser(capsys):
    filtr = "Day"
    browser = "google"
    GetHistory().getHistory(filtr, browser)
    captured = capsys.readouterr()
    assert captured.out == "Browser spelling error: is Google valid?\n"
