import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent.absolute())) 
from urlProcessor.urlFilter import base, filterBlacklistedUrl


def test_base():
    urls = ['https://www.stackoverflow.com/questions', 'https://mail.google.com/very_important/email']

    results = [base(url) for url in urls]
    assert results == ['www.stackoverflow.com', 'mail.google.com']

def test_blacklist_checker():
    history_list = ['https://www.dcu.ie/', 'https://opentimetable.dcu.ie/', 'https://gitlab.computing.dcu.ie/', 'https://github.com/notifications', 'https://www.facebook.com/help', 'https://stackoverflow.com/users/']
    blacklist = ['www.facebook.com', 'www.mail.google.com', 'www.twitter.com', 'https://discord.com', 'https://www.reddit.com/']

    expected_filtered = ['https://www.dcu.ie/', 'https://opentimetable.dcu.ie/', 'https://gitlab.computing.dcu.ie/', 'https://github.com/notifications', 'https://stackoverflow.com/users/']
    assert filterBlacklistedUrl(history_list, blacklist) == expected_filtered

def test_base_with_blacklist():
    history = ['https://github.com/', 'https://www.facebook.com/help', 'https://stackoverflow.com/questions/']
    blacklist = ['www.github.com']
    base_results = [base(url) for url in filterBlacklistedUrl(history, blacklist)]
    expected_base = ['www.facebook.com', 'github.com']
    assert base_results != expected_base