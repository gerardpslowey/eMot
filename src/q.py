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

MAX_WORKERS = 5

def add_to_queue(urls, q):
    # Remove duplicates
    for url in set(urls):
        q.put(url)

    print("URLs added to queue")
    return(q)
    
def main():
    blacklist = ['www.google.com', 'www.google.ie', 'www.facebook.com', 'stackoverflow.com', 'docs.google.com', 'mail.google.com', 'www.twitter.com', 'discord.com', 'www.reddit.com', 'gitlab.computing.dcu.ie', 'github.com', 'www.messenger.com', 'www.youtube.com']

    print("Time filters include 'hour', 'day', 'week', 'month', or 'year' or '' (all time).")
    filtr = input('Filter the date: ')
    print("Browser options include 'Chrome', 'Firefox', 'Safari', 'Edge', 'Opera', and 'Brave'.")
    browser = input('Enter the browser: ')
    urls = GetHistory().get_history(filtr, browser)
    print("History Retrieved: " + str(len(urls)))

    filtered_urls = filter_blacklisted_url(urls.values(), blacklist)
    print("URLS remaining after filtering: " + str(len(filtered_urls)))

    queue = add_to_queue(urls=filtered_urls, q=Queue())

    # asynchronous execution of tasks using threads
    # use a with statement to ensure threads are cleaned up promptly
    with futures.ThreadPoolExecutor(max_workers=MAX_WORKERS) as executor:
        f = []

        while not queue.empty():
            url = queue.get()
            f.append(executor.submit(Scraper().scrape, url=url))

        # Deal with the threads as they complete individually
        for future in futures.as_completed(f):
            data = future.result()

            # store scraped data
            FileMod().write_to_csv(data)

    print("Finished scraping!")

if __name__ == "__main__":
    main()
