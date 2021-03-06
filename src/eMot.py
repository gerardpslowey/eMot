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

import multiprocessing

cpu_cores = multiprocessing.cpu_count()
MAX_WORKERS = cpu_cores * 2
# print(MAX_WORKERS)
    
class Emot:
    def __init__(self, filtr, browser):
        self.filtr = filtr
        self.browser = browser
        blacklist = self.get_blacklist()
        urls = self.get_urls(filtr, browser, blacklist)
        self.start_tasks(urls)

    def get_blacklist(self):
        blacklist = []
        with open('blacklists/urls_blacklist.txt','r') as myfile:
            for line in myfile:
                blacklist.append(line.strip())
        return blacklist

    def get_urls(self, filtr, browser, blacklist):
        urls = GetHistory().get_history(filtr, browser)
        print("History Retrieved: " + str(len(urls)))
        filtered_urls = filter_blacklisted_url(urls.values(), blacklist)
        print("URLS remaining after filtering: " + str(len(filtered_urls)))
        return filtered_urls

    def start_tasks(self, urls):
        queue = Queue()
        for url in set(urls):
            queue.put(url)
        print("URLs added to queue")

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
                self.write_to_csv(data)

        print("Finished scraping!")

    def write_to_csv(self, data):
        text = []
        
        with open('sentimentAnalysis/scraped.csv', mode='a', encoding="utf-8",  newline='') as scraped_text:
            writer = csv.writer(scraped_text, delimiter=',')

            for item in data:
                if(len(item)!=0):
                    text.append(item)
                    
            if len(text) != 0:
                writer.writerow(text)

def main():
    print("Time filters include 'hour', 'day', 'week', 'month', or 'year' or '' (all time).")
    filtr = input('Filter the date: ').capitalize()
    print("Browser options include 'Chrome', 'Firefox', 'Safari', 'Edge', 'Opera', and 'Brave'.")
    browser = input('Enter the browser: ').capitalize()

    Emot(filtr, browser)

if __name__ == "__main__":
    main()
