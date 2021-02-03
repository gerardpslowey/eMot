# Queue of urls 
from queue import Queue

# Implement threading
import threading
import concurrent.futures as futures

# Resolve import errors
import os
import sys
from pathlib import Path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

# Get browser history
import browser_history

# Scraper
from urlScraper import scraper

MAX_WORKERS = 10

def add_to_queue(urls, q):
    for url in urls:
        q.put(url[1])

    print("URLs added to queue")
    return()

def scrape(site):
    # while True:
    #     # gets the url from the queue
    #     site = queue.get()

    # download the file
    print("scraping site: " + site)
    scraper.scrape(site)
    print(f'task {site} finished') 

    return()

def main():
    # queue = Queue()

    urls = browser_history.get_history()
    print("History Retrieved")

    # add_to_queue(urls, queue)

    with futures.ThreadPoolExecutor(max_workers=MAX_WORKERS) as executor:
        links = list()
        for url in urls:
            links.append(executor.submit(scrape, site=url[1]))
        
        results = list()
        for link in futures.as_completed(links):
            results.append(link.result())

    print("Finished scraping!")

if __name__ == "__main__":
    main()
