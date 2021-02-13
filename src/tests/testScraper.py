import spacy, requests, re, sys
from bs4 import BeautifulSoup, Comment, Doctype
from pathlib import Path

# go back to parent directory
sys.path.append(str(Path(__file__).parent.parent.absolute())) 
from urlProcessor.fileMod import FileMod

nlp = spacy.load("en_core_web_sm")

def main():
    # url = input("Enter a URL (must include 'https') : ")
    FileMod().erase_file()
    url = 'https://webscraper.io/test-sites'
    print(f'testing {url}..')

    soup = get_soup(url)
    get_text(soup)
    #FileMod().write_file(text)
    print('finished!')

def get_soup(url):
    r = requests.get('http://localhost:8050/render.html', params={'url':url, 'wait':2})
    #print(r.status_code)
    soup = BeautifulSoup(r.text, 'html.parser')
    return soup

def get_text(soup):
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
    print(cleaned)

if __name__ == "__main__":
    main()