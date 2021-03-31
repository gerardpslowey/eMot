class Blacklists:

    def __init__(self):
        self.urlsSet = {
            "www.google.com", "www.google.ie",
            "www.facebook.com", "docs.google.com",
            "mail.google.com", "accounts.google.com",
            "www.twitter.com", "discord.com",
            "www.reddit.com", "gitlab.computing.dcu.ie",
            "github.com", "www.messenger.com",
            "www.youtube.com", "stackoverflow.com",
            "dcu-ie.zoom.us", "www.bing.com",
        }

        self.tagsSet = {
            "[document]", "script",
            "noscript", "title",
            "style", "figure",
            "img", "iframe",
            "nav", "meta",
            "header", "head",
            "footer", "cookie",
        }

    def getTags(self):
        return self.tagsSet

    def addTag(self, tag):
        self.tagsSet.add(tag)

    def deleteTag(self, tag):
        self.tagsSet.remove(tag)

    def getUrls(self):
        return self.urlsSet

    def addUrl(self, url):
        self.urlsSet.add(url)

    def deleteUrl(self, url):
        self.urlsSet.remove(url)