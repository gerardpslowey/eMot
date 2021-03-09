import spacy, requests, re, os, sys
from pathlib import Path
import cProfile, io, pstats
from bs4 import BeautifulSoup, Comment, Doctype

sys.path.append(str(Path(__file__).parent.parent.absolute())) 
from sentimentAnalysis.textMod import preProcess

class Scraper:
    
    def scrape(self, url, tag_list='blacklists/tags_blacklist.txt'):
        print("scraping site: " + url + "\n")
        soup = self.getSoup(url)
        blacklist = self.getBlacklist(tag_list)
        text = self.getText(soup, blacklist)
        print(f'task {url} finished\n') 
        return text

    def getSoup(self, url):
        r = requests.get('http://localhost:8050/render.html', params={'url':url, 'wait':3, 'timeout':10})
        soup = BeautifulSoup(r.text, 'html.parser') if r.status_code == 200 else ''
        return soup

    def getStatus(self, url):
        r = requests.get('http://localhost:8050/render.html', params={'url':url, 'wait':3, 'timeout':10})
        return r.status_code

    def getBlacklist(self, tag_list):
        blacklist = []
        with open(tag_list,'r') as myfile:
            for line in myfile:
                blacklist.append(line.strip())
        return blacklist

    def getText(self, soup, blacklist):
        # get rid of the unwanted text in Comments, Doctype and the above tags list.
        for junk in soup(blacklist):
            junk.decompose() 

        for comment in soup.findAll(text=lambda text: isinstance(text, (Comment, Doctype))):
            comment.extract()

        cleaned =[]
        for sentence in soup.find_all(text=True):
            sentence = sentence.strip().lower()
            if (str(sentence) 
                and 'we and our partners use' not in sentence
                and 'we and our partners do' not in sentence
                and 'Personalised ads and content' not in sentence
                and 'our privacy policy' not in sentence):

                cleaned.append(preProcess(sentence))
        return cleaned

def main():
    url = 'https://www.independent.ie/opinion/letters/new-opening-hours-very-little-use-when-the-pubs-are-closed-40125545.html'
    tags_list = '../blacklists/tags_blacklist.txt'
    print(Scraper().scrape(url, tags_list))

if __name__ == '__main__':
    pr = cProfile.Profile()
    pr.enable()

    my_result = main()

    pr.disable()
    s = io.StringIO()
    ps = pstats.Stats(pr, stream=s).sort_stats('tottime')
    ps.print_stats()

    with open('scraper_cprofile.txt', 'w+') as f:
        f.write(s.getvalue())