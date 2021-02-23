import spacy, requests, re, os, sys
from bs4 import BeautifulSoup, Comment, Doctype

nlp = spacy.load("en_core_web_sm")
# sentencizer = nlp.add_pipe("sentencizer")

# Construction from class
# from spacy.pipeline import Sentencizer
# sentencizer = Sentencizer()

class Scraper:
    
    def scrape(self, url, tag_list='blacklists/tags_blacklist.txt'):
        print("scraping site: " + url + "\n")
        soup = self.get_soup(url)
        blacklist = self.get_blacklist(tag_list)
        text = self.get_text(soup, blacklist)
        print(f'task {url} finished\n') 
        return text

    def get_soup(self, url):
        r = requests.get('http://localhost:8050/render.html', params={'url':url, 'wait':3})
        soup = BeautifulSoup(r.text, 'html.parser') if r.status_code == 200 else ''
        return soup

    def get_status(self, url):
        r = requests.get('http://localhost:8050/render.html', params={'url':url, 'wait':3})
        return r.status_code

    def get_blacklist(self, tag_list):
        blacklist = []
        with open(tag_list,'r') as myfile:
            for line in myfile:
                blacklist.append(line.strip())
        return blacklist

    def get_text(self, soup, blacklist):
        # get rid of the unwanted text in Comments, Doctype and the above tags list.
        for junk in soup(blacklist):
            junk.decompose() 

        for comment in soup.findAll(text=lambda text: isinstance(text, (Comment, Doctype))):
            comment.extract()

        tokenized_data = []
        for token in soup.find_all(text=True):
            token = token.strip() 
            if str(token) and 'cookie' not in str(token) and 'our partners' not in str(token):
                tokenized_data.append(token)

        # return tokenized_data

        docs = nlp(" ".join(tokenized_data))
        cleaned = [word.lemma_ for word in docs if word.is_alpha and not word.is_stop and not word.is_punct and not word.like_email]

        return cleaned
        