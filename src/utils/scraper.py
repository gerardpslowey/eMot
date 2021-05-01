import cProfile
import io
import pstats
import re

import requests
from bs4 import BeautifulSoup, Comment, Doctype

from .blacklists import Blacklists
from .textMod import preProcess


class Scraper:
    """
    Main GUI application. Uses eMot for scraping and emotClassify for metrics.
    You can run this file to test the scraping of the given web url below.
    """

    def scrape(self, url, task):
        blacklist = Blacklists()
        tagSet = blacklist.getItems()["tagSet"]
        print(f"{task}. {url}")
        soup = self.getSoup(url)

        if len(soup) != 0:
            text = self.getText(soup, tagSet)
            print(f'Task {task} Finished')
            return (url, text)
        else:
            print(f"{task}. unreachable, skipped")
            return None

    def getSoup(self, url):
        req = requests.get(
            "http://localhost:8050/render.html", params={"url": url, "wait": 3}
        )
        soup = BeautifulSoup(
            req.text, "html.parser") if req.status_code == 200 else ""
        return soup

    def getStatus(self, url):
        req = requests.get(
            "http://localhost:8050/render.html", params={"url": url, "wait": 3}
        )
        return req.status_code

    def getText(self, soup, blacklist):
        # get rid of the unwanted text in Comments, Doctype and the above tags
        for junk in soup(blacklist):
            junk.decompose()

        for comment in soup.findAll(
            text=lambda text: isinstance(text, (Comment, Doctype))
        ):
            comment.extract()

        processed = []
        for sentence in soup.find_all(text=True):
            sentence = sentence.strip().lower()
            if str(sentence) and not re.search(
                "(we and our partners use|we and our partners store|" +
                "personalised ads and content|our privacy policy|" + # noqa
                "click below to consent)",  # noqa
                sentence.lower()
            ):

                processed.append(preProcess(sentence))

        return processed


def main():
    url = "https://webscraper.io/test-sites/e-commerce/allinone/computers"
    print(Scraper().scrape(url, 1))


if __name__ == "__main__":
    main()
    pr = cProfile.Profile()
    pr.enable()

    my_result = main()

    pr.disable()
    stream = io.StringIO()
    ps = pstats.Stats(pr, stream=stream).sort_stats("tottime")
    ps.print_stats()

    with open("scraper_cprofile.txt", "w+") as f:
        f.write(stream.getvalue())
