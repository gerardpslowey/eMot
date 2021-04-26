import requests, re
import cProfile, io, pstats
from bs4 import BeautifulSoup, Comment, Doctype

from .textMod import preProcess
from .blacklists import Blacklists


class Scraper:
    def scrape(self, url, task):
        blacklist = Blacklists()
        tagSet = blacklist.getItems()['tagSet']
        print(f"{task}. {url}")
        soup = self.getSoup(url)

        if(len(soup) != 0):
            text = self.getText(soup, tagSet)
            print(f'Task {task} Finished')
            return (url, text)

        print(f"{task}. {url} returned null, skipped")
        return None

    def getSoup(self, url):
        r = requests.get('http://localhost:8050/render.html', params={'url': url, 'wait': 3})
        soup = BeautifulSoup(r.text, 'html.parser') if r.status_code == 200 else ''
        return soup

    def getStatus(self, url):
        r = requests.get('http://localhost:8050/render.html', params={'url': url, 'wait': 3})
        return r.status_code

    def getText(self, soup, blacklist):
        # get rid of the unwanted text in Comments, Doctype and the above tags list.
        for junk in soup(blacklist):
            junk.decompose()

        for comment in soup.findAll(text=lambda text: isinstance(text, (Comment, Doctype))):
            comment.extract()

        cleaned = []
        for sentence in soup.find_all(text=True):
            sentence = sentence.strip().lower()
            if (str(sentence) and not re.search(
                '(we and our partners use|we and our partners store|'
                + 'personalised ads and content|our privacy policy|'    # noqa
                + 'click below to consent)',                            # noqa
                    sentence.lower())):

                cleaned.append(preProcess(sentence))

        return cleaned


def main():
    url = 'https://webscraper.io/test-sites/e-commerce/allinone/computers'
    print(Scraper().scrape(url, 1))


if __name__ == "__main__":
    main()
    pr = cProfile.Profile()
    pr.enable()

    my_result = main()

    pr.disable()
    s = io.StringIO()
    ps = pstats.Stats(pr, stream=s).sort_stats('tottime')
    ps.print_stats()

    with open('scraper_cprofile.txt', 'w+') as f:
        f.write(s.getvalue())
