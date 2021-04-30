import sys
from pathlib import Path

from utils.urlFilter import base, filterBlacklistedUrl

# sets path to src
sys.path.append(str(Path(__file__).parent.parent.absolute()))


def test_base():
    urls = [
        "https://www.stackoverflow.com/questions",
        "https://mail.google.com/very_important/email",
    ]

    results = [base(url) for url in urls]
    assert results == ["www.stackoverflow.com", "mail.google.com"]


def test_blacklist_checker():
    history_list = [
        "https://www.dcu.ie/",
        "https://opentimetable.dcu.ie/",
        "https://gitlab.computing.dcu.ie/",
        "https://github.com/notifications",
        "https://www.facebook.com/help",
        "https://stackoverflow.com/users/",
    ]
    blacklist = [
        "www.facebook.com",
        "www.mail.google.com",
        "www.twitter.com",
        "https://discord.com",
        "https://www.reddit.com/",
    ]

    expected_filters = [
        "https://www.dcu.ie/",
        "https://opentimetable.dcu.ie/",
        "https://gitlab.computing.dcu.ie/",
        "https://github.com/notifications",
        "https://stackoverflow.com/users/",
    ]
    assert filterBlacklistedUrl(history_list, blacklist) == expected_filters


def test_base_with_blacklist():
    history = [
        "https://github.com/",
        "https://www.facebook.com/help",
        "https://stackoverflow.com/questions/",
    ]
    blacklist = ["www.github.com"]
    base_results = [base(url)
                    for url in filterBlacklistedUrl(history, blacklist)]
    expected_base = ["www.facebook.com", "github.com"]
    assert base_results != expected_base
