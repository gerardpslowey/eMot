import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent.absolute())) 

from urlProcessor.urlFilter import base, filterBlacklistedUrl

def main():
    testBase()
    print("\n")
    testBlacklistChecker()

def testBase():
    urls = ['https://www.stackoverflow.com/questions', 'https://mail.google.com/very_important/email']

    for url in urls:
        print(base(url))

def testBlacklistChecker():
    history_list = ['https://www.dcu.ie/', 'https://opentimetable.dcu.ie/', 'https://gitlab.computing.dcu.ie/', 'https://github.com/', 'https://www.facebook.com/help', 'https://stackoverflow.com/questions/']
    blacklist = ['www.facebook.com', 'www.mail.google.com', 'www.twitter.com', 'https://discord.com', 'https://www.reddit.com/']

    result = filterBlacklistedUrl(history_list, blacklist) 
    print(result)

if __name__ == '__main__':
    main()
