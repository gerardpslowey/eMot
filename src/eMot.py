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
        f = open(self.scraped_csv, "w+")
        f.close()

        urlSet = Blacklists().getItems()['urlSet']
        urls = self.getUrls(filtr, browser, urlSet)
        self.startTasks(urls)

    def getUrls(self, filtr, browser, blacklist):
        urls = GetHistory().getHistory(filtr, browser)
        print(f"History Retrieved: {len(urls)}")
        
        filtered_urls = set(filterBlacklistedUrl(urls.values(), blacklist))
        print(f"URLS remaining after filtering: {len(filtered_urls)}")
        return filtered_urls

    def startTasks(self, urls):
        queue = Queue()
        for url in urls:
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

        
        if len(urls) > 0:
            print("Finished scraping!")
        else:
            print("Nothing to scrape!")

    def writeToCSV(self, document):
        normal = []
        cleaned = []
        with open(self.scraped_csv, mode='a+', encoding="utf-8",  newline='') as csvfile:
            fieldnames = ['normalSentence', 'cleanedSentence']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames, delimiter=',')

            for normalSentence, cleanedSentence in document.items():
                if(len(normalSentence.split()) > 3):
                    normal.append(normalSentence)
                    cleaned.append(cleanedSentence)

            writer.writerow({'normalSentence':normal, 'cleanedSentence':cleaned})

def main():
    print("Time filters include 'hour', 'day', 'week', 'month', or 'year' or '' (all time).")
    filtr = input('Filter the date: ').capitalize()
    print("Browser options include 'Chrome', 'Firefox', 'Safari', 'Edge', 'Opera', and 'Brave'.")
    browser = input('Enter the browser: ').capitalize()

    Emot(filtr, browser)

if __name__ == "__main__":
    main()
