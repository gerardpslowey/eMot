import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent.absolute())) 
from urlProcessor.scraper import Scraper

def main():
    url = 'https://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html'
    print(f'testing {url}..')
    test1 = Scraper()
    test1.scrape(url)
    print('finished!')
    print("==============================")

    url = 'https://webscraper.io/test-sites/e-commerce/allinone'
    print(f'testing {url}..')
    test2 = Scraper()
    status_code = test2.get_status(url)
    print(f'status code = {status_code}')

if __name__ == "__main__":
    main()