# Queue of urls 
from queue import Queue

# Implement threading
import threading, concurrent.futures as futures

# Get browser history
import os, sys, csv
from browserHistory.getHistory import GetHistory

import pandas as pd

# Scraper and url filter
from urlProcessor.scraper import Scraper
from urlProcessor.urlFilter import filterBlacklistedUrl
from urlProcessor.blacklists import Blacklists

from urlProcessor.textMod import cleanScrapedText, preProcess

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
        self.overwriteCSV()

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
                # tuple
                data = future.result()

                if(data != None):
                    url = data[0]
                    originalText = data[1]
                    # cleanedText = preProcess(originalText)
                    # store scraped data
                    self.writeToCSV(url, originalText)

        
        if len(urls) > 0:
            print("Finished scraping!")
        else:
            print("Nothing to scrape!")


    def overwriteCSV(self):
        with open('sentimentAnalysis/scraped.csv', mode='w', encoding="utf-8", newline='') as scraped_text:
            fields = ['url', 'original_data']
            writer = csv.DictWriter(scraped_text, fieldnames=fields, delimiter=',')
            writer.writeheader()


    def writeToCSV(self, url, originalText):
        # cleanedText = data[2]

        data = []
        with open('sentimentAnalysis/scraped.csv', mode='a+', encoding="utf-8",  newline='') as scraped_text:
            writer = csv.writer(scraped_text, delimiter=',')

            # print(originalText)
            # print(sentence)

            for sentence in originalText:
                # remove silly sentences
                if(len(sentence.split()) > 3):
                    data.append(sentence)

            writer.writerow([url, ".".join(data)])





        #     writer = csv.DictWriter(scraped_text, fieldnames=fields, delimiter='.') 

        #     for sentence in originalText:
        #         if(len(sentence.split()) > 3):
        #             cleaned.append(sentence)

        # row = {'url' : url, 'original_data' : originalText}


def main():
    print("Time filters include 'hour', 'day', 'week', 'month', or 'year' or '' (all time).")
    filtr = input('Filter the date: ').capitalize()
    print("Browser options include 'Chrome', 'Firefox', 'Safari', 'Edge', 'Opera', and 'Brave'.")
    browser = input('Enter the browser: ').capitalize()

    Emot(filtr, browser)

if __name__ == "__main__":
    main()
