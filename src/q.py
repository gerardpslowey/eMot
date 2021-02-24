# Queue of urls 
from queue import Queue

# Implement threading
import threading, concurrent.futures as futures

# Get browser history
import os, sys, csv
from browserHistory.getHistory import GetHistory

# Scraper and url filter
from urlProcessor.scraper import Scraper
from urlProcessor.urlFilter import filter_blacklisted_url

MAX_WORKERS = 5

def add_to_queue(urls, q):
    # Remove duplicates
    for url in set(urls):
        q.put(url)

    print("URLs added to queue")
    return(q)

def get_blacklist():
    blacklist = []
    with open('blacklists/urls_blacklist.txt','r') as myfile:
        for line in myfile:
            blacklist.append(line.strip())
    return blacklist

def write_to_csv(data):
    text = []
    
    with open('sentimentAnalyser/scraped.csv', mode='a', encoding="utf-8") as scraped_text:
        writer = csv.writer(scraped_text, delimiter=',')

        for item in data:
            if(len(item)!=0):
                text.append(item)
                
        if len(text) != 0:
            writer.writerow(text)
    
def main():
    blacklist = get_blacklist()

    print("Time filters include 'hour', 'day', 'week', 'month', or 'year' or '' (all time).")
    filtr = input('Filter the date: ').capitalize()
    print("Browser options include 'Chrome', 'Firefox', 'Safari', 'Edge', 'Opera', and 'Brave'.")
    browser = input('Enter the browser: ').capitalize()

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
            write_to_csv(data)

    print("Finished scraping!")

if __name__ == "__main__":
    main()
