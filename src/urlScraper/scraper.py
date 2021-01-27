import requests
from bs4 import BeautifulSoup
import re

# tags in html that we don't need to search through.
blacklist = [
    '[document]',
    'noscript',
    'header',
    'html',
    'meta',
    'head', 
    'input',
    'script',
    'style',
    'nav',
]

def main():
    url = 'http://quotes.toscrape.com/'
    file = 'text.txt'
    soup = get_soup(url)
    text = get_text(soup)
    write_to_file(file, text)


def get_soup(url):
    r = requests.get('http://localhost:8050/render.html', params={'url':url, 'wait':2})
    soup = BeautifulSoup(r.text, 'html.parser')
    return soup

def get_text(soup):

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

    text = soup.find_all(text=True)
    info = [emoji_pattern.sub(r'',t.strip()) for t in text if t.parent.name not in blacklist]

    return info

def write_to_file(file, chunks):

    with open(file, "w", encoding="utf-8") as f:
        for chunk in chunks:
            if(len(chunk)!=0):
                f.write(str(chunk) + " ")

if __name__ == "__main__":
    main()