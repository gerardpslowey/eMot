# Queue of urls 
from queue import Queue

# Implement threading
import threading, concurrent.futures as futures

# Get browser history from different folder by changing the Path
import os, sys
from pathlib import Path
from browserHistory.getHistory import GetHistory

# Scraper and file modification
from urlProcessor.scraper import Scraper
from urlProcessor.fileMod import FileMod
from urlProcessor.urlFilter import filter_blacklisted_url

MAX_WORKERS = 10

def main():
    blacklist = ['www.facebook.com', 'mail.google.com', 'www.twitter.com', 'discord.com', 'www.reddit.com', 'gitlab.computing.dcu.ie', 'github.com', 'www.messenger.com']

    FileMod().erase_file()
    queue = Queue()
    urls = GetHistory().get_history()
    print("History Retrieved: " + str(len(urls)))

    filtered_urls = filter_blacklisted_url(urls.values(), blacklist)

    add_to_queue(filtered_urls, queue)

    with futures.ThreadPoolExecutor(max_workers=MAX_WORKERS) as executor:
        while not queue.empty():
            url = queue.get()
            s = executor.submit(scrape, site=url) 

    print("Finished scraping!")

def add_to_queue(urls, q):
    # Remove duplicates
    for url in set(urls):
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
