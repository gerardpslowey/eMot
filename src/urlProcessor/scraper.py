import spacy, requests, re, os, sys
from pathlib import Path
import cProfile, io, pstats
from bs4 import BeautifulSoup, Comment, Doctype

from .textMod import preProcess, removeURLs
from .blacklists import Blacklists

class Scraper:
    def scrape(self, url):
        tagSet = Blacklists().getItems()['tagSet']
        print("scraping site: " + url + "\n")
        soup = self.getSoup(url)
        if(len(soup) != 0):
            text = self.getText(soup, tagSet)
            print(f'task {url} finished\n') 
            return text

        print(f'task {url} returned null, skipped\n') 
        return None

    def getSoup(self, url):
        r = requests.get('http://localhost:8050/render.html', params={'url': url, 'wait': 3})
        soup = BeautifulSoup(r.text, 'html.parser') if r.status_code == 200 else ''
        return soup

    def getStatus(self, url):
        r = requests.get('http://localhost:8050/render.html', params={'url':url, 'wait':3})
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
            if (str(sentence)
                and 'we and our partners use' not in sentence
                and 'we and our partners do' not in sentence
                and 'personalised ads and content' not in sentence
                and 'our privacy policy' not in sentence):

                sent = preProcess(sentence)
                cleaned.append(removeURLs(sent))

        return cleaned

def main():
    url = 'https://www.independent.ie/opinion/letters/new-opening-hours-very-little-use-when-the-pubs-are-closed-40125545.html'
    print(Scraper().scrape(url))


if __name__ == '__main__':
    main()
    # pr = cProfile.Profile()
    # pr.enable()

    # my_result = main()

    # pr.disable()
    # s = io.StringIO()
    # ps = pstats.Stats(pr, stream=s).sort_stats('tottime')
    # ps.print_stats()

    # with open('scraper_cprofile.txt', 'w+') as f:
    #     f.write(s.getvalue())