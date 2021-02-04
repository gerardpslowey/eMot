# Queue of urls 
from queue import Queue

# Implement threading
import threading
import concurrent.futures as futures

# Get browser history from different folder by changing the Path
import os
import sys
from pathlib import Path
from browserHistory.getHistory import GetHistory

# Scraper
from urlProcessor.scraper import Scraper
from urlProcessor.fileMod import FileMod

MAX_WORKERS = 10

def main():
    FileMod().erase_file()
    queue = Queue()
    urls = GetHistory().get_history()
    print("History Retrieved")

    add_to_queue(urls, queue)

    with futures.ThreadPoolExecutor(max_workers=MAX_WORKERS) as executor:
        links = set()
        for url in urls.values():
            links.add(executor.submit(scrape, site=url))
        
        results = set()
        for link in futures.as_completed(links):
            results.add(link.result())

    print("Finished scraping!")

def add_to_queue(urls, q):

    # date, url
    for url in urls.values():
        q.put(url)

    print("URLs added to queue")
    return()

def scrape(site):
    # while True:
    #     # gets the url from the queue
    #     site = queue.get()

    # download the file
    print("scraping site: " + site)
    Scraper().scrape(site)
    print(f'task {site} finished') 

    return()

if __name__ == "__main__":
    main()
