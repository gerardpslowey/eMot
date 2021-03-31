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
        urlsSet = Blacklists().getUrls()
        urls = self.getUrls(filtr, browser, urlsSet)
        self.startTasks(urls)

    def getUrls(self, filtr, browser, blacklist):
        urls = GetHistory().getHistory(filtr, browser)
        print("History Retrieved: " + str(len(urls)))
        filtered_urls = filterBlacklistedUrl(urls.values(), blacklist)
        print("URLS remaining after filtering: " + str(len(filtered_urls)))
        return filtered_urls

    def startTasks(self, urls):
        queue = Queue()
        for url in set(urls):
            queue.put(url)
        print("URLs added to queue")

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

        print("Finished scraping!")

    def writeToCSV(self, document):
        data = []
        with open('sentimentAnalysis/scraped.csv', mode='a+', encoding="utf-8",  newline='') as scraped_text:
            writer = csv.writer(scraped_text, delimiter=',')

            for sentence in document:
                if(len(sentence.split()) > 3):
                    data.append(sentence)

            writer.writerow(data)

def main():
    print("Time filters include 'hour', 'day', 'week', 'month', or 'year' or '' (all time).")
    filtr = input('Filter the date: ').capitalize()
    print("Browser options include 'Chrome', 'Firefox', 'Safari', 'Edge', 'Opera', and 'Brave'.")
    browser = input('Enter the browser: ').capitalize()

    Emot(filtr, browser)

if __name__ == "__main__":
    main()
