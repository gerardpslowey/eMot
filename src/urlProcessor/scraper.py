import spacy, requests, re, os, sys
from bs4 import BeautifulSoup, Comment, Doctype
from .fileMod import FileMod

nlp = spacy.load("en_core_web_sm")

class Scraper:
    
    def scrape(self, url):
        print("scraping site: " + url + "\n")
        soup = self.get_soup(url)
        text = self.get_text(soup)
        print(f'task {url} finished\n') 
        return text

    def get_soup(self, url):
        r = requests.get('http://localhost:8050/render.html', params={'url':url, 'wait':2})
        
        soup = BeautifulSoup(r.text, 'html.parser') if r.status_code == 200 else ''
        return soup

    def get_status(self, url):
        r = requests.get('http://localhost:8050/render.html', params={'url':url, 'wait':2})
        return r.status_code

    def get_text(self, soup):
        blacklist = ['[document]','script','noscript','title','style','figure','img','iframe','nav','meta','header','head','footer']

        # get rid of the unwanted text in Comments, Doctype and the above tags list.
        for junk in soup(blacklist):
            junk.decompose() 

        for comment in soup.findAll(text=lambda text: isinstance(text, (Comment, Doctype))):
            comment.extract()

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