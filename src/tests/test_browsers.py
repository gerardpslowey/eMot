import sys
from pathlib import Path

import browserHistory

from .test_utils import (become_linux, become_mac, become_windows,
                         change_homedir)

sys.path.append(str(Path(__file__).parent.parent.absolute()))

become_linux = become_linux
become_mac = become_mac
become_windows = become_windows
change_homedir = change_homedir


def test_firefox_linux(become_linux, change_homedir):
    firefox = browserHistory.browsers.Firefox()
    outputs = firefox.fetchHistory()
    his = outputs.histories

    assert len(his) == 5


def test_chrome_linux(become_linux, change_homedir):
    chrome = browserHistory.browsers.Chrome()
    outputs = chrome.fetchHistory()
    his = outputs.histories

    assert len(his) == 2


def test_safari_mac(become_mac, change_homedir):
    safari = browserHistory.browsers.Safari()
    outputs = safari.fetchHistory()
    his = outputs.histories

    assert len(his) == 5


def test_edge_windows(become_windows, change_homedir):
    edge = browserHistory.browsers.Edge()
    outputs = edge.fetchHistory()
    his = outputs.histories

    assert len(his) == 1


def test_opera_windows(become_windows, change_homedir):
    opera = browserHistory.browsers.Opera()
    outputs = opera.fetchHistory()
    his = outputs.histories

    assert len(his) == 2


def test_brave_windows(become_windows, change_homedir):
    brave = browserHistory.browsers.Brave()
    outputs = brave.fetchHistory()
    his = outputs.histories

    assert len(his) == 4


def test_firefox_windows(become_windows, change_homedir):
    firefox = browserHistory.browsers.Firefox()
    outputs = firefox.fetchHistory()
    his = outputs.histories

    assert len(his) == 8
