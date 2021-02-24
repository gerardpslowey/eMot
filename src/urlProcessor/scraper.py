import spacy, requests, re, os, sys
import cProfile, io, pstats
from bs4 import BeautifulSoup, Comment, Doctype

nlp = spacy.load("en_core_web_sm")
sentencizer = nlp.add_pipe("sentencizer", first=True)

def main():
    url = 'https://www.independent.ie/opinion/letters/new-opening-hours-very-little-use-when-the-pubs-are-closed-40125545.html'
    tags_list = '../blacklists/tags_blacklist.txt'
    print(Scraper().scrape(url, tags_list))


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

    def cleaned(self, data):
        docs = nlp(data)
        clean = []
        for word in docs:
            if word.lemma_ != '-PRON-' and not word.is_stop and not word.is_punct:
                clean.append(word.lemma_)

        return clean
        # return ' '.join(clean)

    def get_text(self, soup, blacklist):
        # get rid of the unwanted text in Comments, Doctype and the above tags list.
        for junk in soup(blacklist):
            junk.decompose() 

        for comment in soup.findAll(text=lambda text: isinstance(text, (Comment, Doctype))):
            comment.extract()

        tokenized_data = []
        for token in soup.find_all(text=True):
            token = token.strip().lower()
            if str(token) and 'we and our partners use' not in token and 'our privacy policy' not in token:
                cleaned = self.cleaned(token)
                tokenized_data.append(cleaned)

            flat_list = []
            for sublist in tokenized_data:
                for item in sublist:
                    flat_list.append(item)

        return flat_list


if __name__ == '__main__':
    pr = cProfile.Profile()
    pr.enable()

    my_result = main()

    pr.disable()
    s = io.StringIO()
    ps = pstats.Stats(pr, stream=s).sort_stats('tottime')
    ps.print_stats()

    with open('test.txt', 'w+') as f:
        f.write(s.getvalue())