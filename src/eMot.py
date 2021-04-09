# Queue of urls 
from queue import Queue

# Implement threading
import threading, concurrent.futures as futures

# Get browser history
import os, sys, csv
from browserHistory.getHistory import GetHistory

# Scraper and url filter
from urlProcessor.scraper import Scraper
from urlProcessor.urlFilter import filterBlacklistedUrl
from urlProcessor.blacklists import Blacklists

import multiprocessing

cpu_cores = multiprocessing.cpu_count()
MAX_WORKERS = cpu_cores * 2
    
class Emot:
    def __init__(self, filtr, browser):
        self.filtr = filtr
        self.browser = browser
        self.scraped_csv = 'sentimentAnalysis/scraped.csv'
        self.clearCSV()

        self.blacklist = Blacklists().getItems()['urlSet']
        self.urls = self.getUrls()

    def getUrls(self):
        urls = GetHistory().getHistory(self.filtr, self.browser)
        print(f"History Retrieved: {len(urls)}")
        
        filtered_urls = set(filterBlacklistedUrl(urls.values(), self.blacklist))
        print(f"URLS remaining after filtering: {len(filtered_urls)}")
        return filtered_urls

    def startTasks(self):
        queue = Queue()
        for url in self.urls:
            queue.put(url)
        print("URLs added to queue!")

        """
        asynchronous execution of tasks using threads
        use a with statement to ensure threads are cleaned up promptly
        """
        with futures.ThreadPoolExecutor(max_workers=MAX_WORKERS) as executor:
            f = []
            while not queue.empty():
                url = queue.get()
                f.append(executor.submit(Scraper().scrape, url=url))

            # Deal with the threads as they complete individually
            for future in futures.as_completed(f):
                data = future.result()

                if(data != None):
                    # store scraped data
                    self.writeToCSV(data)

        
        if len(self.urls) > 0:
            print("Finished scraping!")
        else:
            print("Nothing to scrape!")

    def clearCSV(self):
            f = open(self.scraped_csv, "w+")
            f.close()

    def writeToCSV(self, document):
        data = []
        with open(self.scraped_csv, mode='a+', encoding="utf-8",  newline='') as scraped_text:
            writer = csv.writer(scraped_text, delimiter='.')

            for sentence in document:
                if(len(sentence.split()) > 3):
                    data.append(sentence)

            writer.writerow(data)

    def getFilter(self):
        return self.filtr

    def getNumSites(self):
        return self.urls


def main():
    print("Time filters include 'hour', 'day', 'week', 'month', or 'year' or '' (all time).")
    filtr = input('Filter the date: ').capitalize()
    print("Browser options include 'Chrome', 'Firefox', 'Safari', 'Edge', 'Opera', and 'Brave'.")
    browser = input('Enter the browser: ').capitalize()

    emot = Emot(filtr, browser)
    emot.startTasks()

if __name__ == "__main__":
    main()
