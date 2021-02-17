import spacy, requests, re, os, sys
from bs4 import BeautifulSoup, Comment, Doctype
from .fileMod import FileMod

nlp = spacy.load("en_core_web_sm")

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

        tokenized_data = []
        for token in soup.find_all(text=True):
            token = token.strip() 
            if str(token):
                tokens = token.split()
                for token in tokens:
                    tokenized_data.append(token)

        docs = nlp(" ".join(tokenized_data))
        cleaned = [word.lemma_ for word in docs if word.is_alpha and not word.is_stop and not word.is_punct and not word.like_email]

        return cleaned