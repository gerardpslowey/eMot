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
    assert results == ["stackoverflow.com", "mail.google.com"]


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
        "facebook.com",
        "mail.google.com",
        "twitter.com",
        "discord.com",
        "reddit.com",
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
    blacklist = ["github.com"]
    base_results = [base(url)
                    for url in filterBlacklistedUrl(history, blacklist)]
    expected_base = ["facebook.com", "github.com"]
    assert base_results != expected_base


def test_different_googles():
    urls = [
        "https://www.docs.google.com",
        "https://docs.google.com/document/d/1jdV4zmk841cUeMZV5fX7Qjv8nbX89r1axC9ZoXa6fsI/edit#",
        "google.com",
        "http://w3.maps.google.com/page1",
        "https://www.google.com/search?client=firefox-b-d&q=regex+remove+all+after+character"
    ]

    for url in urls:
        assert base(url)[-10:] == "google.com"
