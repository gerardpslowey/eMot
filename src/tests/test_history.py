import sys
from pathlib import Path

from browserHistory.getHistory import GetHistory

# sets path to src
sys.path.append(str(Path(__file__).parent.parent.absolute()))


def test_capitalise():
    browser = "opera"
    assert browser.capitalize() == "Opera"


def test_browser_installed(capsys):
    filtr = "All"
    browser = "Brave"
    GetHistory().getHistory(filtr, browser.capitalize())
    captured = capsys.readouterr()
    assert captured.out == "Brave browser is not installed\n"


def test_filter_error():
    filtr = "3 weeks"
    browser = "chrome"
    result = GetHistory().getHistory(filtr, browser)
    assert result == {}


def test_filter_spelling():
    filtr = "Yeer"
    browser = "opera"
    result = GetHistory().getHistory(filtr, browser)
    assert len(result) == 0


def test_browser_spelling(capsys):
    filtr = "Day"
    browser = "google"
    GetHistory().getHistory(filtr, browser)
    captured = capsys.readouterr()
    assert captured.out == "Browser spelling error: is Google valid?\n"
