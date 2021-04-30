import sys
from pathlib import Path

from utils.scraper import Scraper

# sets path to src
sys.path.append(str(Path(__file__).parent.parent.absolute()))


def test_scraper():
    # test what sort of data is return
    url = "https://www.independent.ie/opinion/letters/new-opening-hours-very-little-use-when-the-pubs-are-closed-40125545.html"  # noqa
    assert Scraper().scrape(url) is not None


def test_blank_site():
    url = "https://www.blank.org/"
    assert Scraper().scrape(url) == [""]


def test_good_status_code():
    # check that a 404 or 503 code doesn't return
    url = "https://webscraper.io/test-sites/e-commerce/allinone"
    assert Scraper().getStatus(url) == 200


def test_bad_status_code():
    url = "https://weblisting.freetemplatespot.com/testing-ground.scraping.pro"
    assert Scraper().getStatus(url) != 404


def test_bad_url():
    url = "https:/testing.1.2.3"
    assert Scraper().getStatus(url) == 502
