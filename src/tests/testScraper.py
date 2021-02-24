import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent.absolute())) 
from urlProcessor.scraper import Scraper

def main():

    # test what sort of data is return 
    url = 'https://www.independent.ie/opinion/letters/new-opening-hours-very-little-use-when-the-pubs-are-closed-40125545.html'
    tags_list = '../blacklists/tags_blacklist.txt'
    test2 = Scraper()
    data = test2.scrape(url,tags_list)
    #assert data != None
    print(data)


    # check that a 404 or 503 code doesn't return
    url = 'https://webscraper.io/test-sites/e-commerce/allinone'
    print(f'testing {url}..')
    test3 = Scraper()
    status_code = test3.get_status(url)
    assert status_code == 200

if __name__ == "__main__":
    main()