import sys
from pathlib import Path
from .test_utils import become_linux, become_mac, become_windows, change_homedir

sys.path.append(str(Path(__file__).parent.parent.absolute()))
import browserHistory

become_linux = become_linux
become_mac = become_mac
become_windows = become_windows
change_homedir = change_homedir


def test_firefox_linux(become_linux, change_homedir):
    f = browserHistory.browsers.Firefox()
    outputs = f.fetchHistory()
    his = outputs.histories

    assert len(his) == 5


def test_chrome_linux(become_linux, change_homedir):
    f = browserHistory.browsers.Chrome()
    outputs = f.fetchHistory()
    his = outputs.histories

    assert len(his) == 2


def test_safari_mac(become_mac, change_homedir):
    f = browserHistory.browsers.Safari()
    outputs = f.fetchHistory()
    his = outputs.histories

    assert len(his) == 5


def test_edge_windows(become_windows, change_homedir):
    f = browserHistory.browsers.Edge()
    outputs = f.fetchHistory()
    his = outputs.histories

    assert len(his) == 1


def test_opera_windows(become_windows, change_homedir):
    f = browserHistory.browsers.Opera()
    outputs = f.fetchHistory()
    his = outputs.histories

    assert len(his) == 2


def test_brave_windows(become_windows, change_homedir):
    f = browserHistory.browsers.Brave()
    outputs = f.fetchHistory()
    his = outputs.histories

    assert len(his) == 4


def test_firefox_windows(become_windows, change_homedir):
    f = browserHistory.browsers.Brave()
    outputs = f.fetchHistory()
    his = outputs.histories

    assert len(his) == 4
