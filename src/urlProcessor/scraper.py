import requests, re, os, sys, json, random

from bs4 import BeautifulSoup, Comment
from .fileMod import FileMod

# tags in html that we don't need to search through.
blacklist = [
    '[document]',
    'noscript',
    'header',
    'footer',
    'html',
    'meta',
    'head', 
    'input',
    'script',
    'style',
    'nav',
]

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
        emoji_pattern = re.compile("["
            u"\U0001F600-\U0001F64F"  # emoticons
            u"\U0001F300-\U0001F5FF"  # symbols & pictographs
            u"\U0001F680-\U0001F6FF"  # transport & map symbols
            u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
            u"\U0001F1F2-\U0001F1F4"  # Macau flag
            u"\U0001F1E6-\U0001F1FF"  # flags
            u"\U0001F600-\U0001F64F"
            u"\U00002702-\U000027B0"
            u"\U000024C2-\U0001F251"
            u"\U0001f926-\U0001f937"
            u"\U0001F1F2"
            u"\U0001F1F4"
            u"\U0001F620"
            u"\u200d"
            u"\u2640-\u2642"
            "]+", flags=re.UNICODE)

        for comments in soup.findAll(text=lambda text:isinstance(text, Comment)):
            comments.extract()

        text = soup.find_all(text=True)
        info = [emoji_pattern.sub(r'',t.strip()) for t in text if t.parent.name not in blacklist]

        return info