# Queue of urls 
from queue import Queue

# Implement threading
import threading, concurrent.futures as futures

# Get browser history from different folder by changing the Path
import os, sys
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
    print("History Retrieved: " + str(len(urls)))

    add_to_queue(urls, queue)

    with futures.ThreadPoolExecutor(max_workers=MAX_WORKERS) as executor:
        while not queue.empty():
            url = queue.get()
            print(url)
            s = executor.submit(scrape, site=url) 

    print("Finished scraping!")

def add_to_queue(urls, q):
    # Remove duplicates
    links = set(urls.values())

    # date, url
    for url in links:
        q.put(url)

    print("URLs added to queue")
    return()

def scrape(site):
    print("scraping site: " + site)
    Scraper().scrape(site)
    print(f'task {site} finished') 

    return()

if __name__ == "__main__":
    main()
