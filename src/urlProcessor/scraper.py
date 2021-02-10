import requests, re, os, sys
from bs4 import BeautifulSoup, Comment, Doctype
from .fileMod import FileMod

class Scraper:

    def scrape(self,url):
        soup = self.get_soup(url)
        text = self.get_text(soup)
        FileMod().write_file(text)

    def get_soup(self,url):
        r = requests.get('http://localhost:8050/render.html', params={'url':url, 'wait':2})
        # print(f'{url} status code = {r.status_code}')
        soup = BeautifulSoup(r.text, 'html.parser')
        return soup

    def get_text(self,soup):
        blacklist = ['[document]','script', 'noscript', 'title','style','figure','img','iframe','nav','meta', 'header','head','footer']

        #get rid of the unwanted text in the above tags list.
        [junk.decompose() for junk in soup(blacklist)]
        [item.extract() for item in soup.contents if isinstance(item, Doctype)]
                
        comments = soup.findAll(text=lambda text: isinstance(text, Comment))
        [comment.extract() for comment in comments]

        tokens = [token.strip() for token in soup.find_all(text=True)] 
        r = re.compile('^[A-Za-z0-9]+')
        info = list(filter(r.match,tokens))

        return info