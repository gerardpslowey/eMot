import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent.absolute())) 
from urlProcessor.scraper import Scraper

def main():
    url = 'https://www.independent.ie/irish-news/coronavirus-ireland-one-further-death-and-679-new-cases-of-covid-19-confirmed-40115477.html'
    tags_list = '../blacklists/tags_blacklist.txt'
    test1 = Scraper()
    data = test1.scrape(url,tags_list)
    assert data != None
    #print(data)

    url = 'https://webscraper.io/test-sites/e-commerce/allinone'
    print(f'testing {url}..')
    test2 = Scraper()
    status_code = test2.get_status(url)
    assert status_code == 200

if __name__ == "__main__":
    main()