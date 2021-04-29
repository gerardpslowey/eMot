# Implement threading
import concurrent.futures as futures

import csv
import multiprocessing
from queue import Queue                             # Queue of urls

from browserHistory.getHistory import GetHistory    # Get browser history
from utils.blacklists import Blacklists

from utils.scraper import Scraper                   # Scraper and url filter
from utils.urlFilter import filterBlacklistedUrl

cpu_cores = multiprocessing.cpu_count()
MAX_WORKERS = cpu_cores * 2


class Emot:
    """
    eMot class is runnable itself in the terminal and does not rely on the GUI.
    It uses the browserHistory folder and scrapes sites.
    """

    def __init__(self, filtr, browser):
        self.filtr = filtr
        self.browser = browser
        self.scraped_csv = "sentimentAnalysis/scraped.csv"

        self.blacklist = Blacklists().getItems()["urlSet"]
        self.urls = self.getUrls()

    def getUrls(self):
        urls = GetHistory().getHistory(self.filtr, self.browser)
        if self.isEmpty(urls):
            return ""

        print("Starting URL scraping..")
        print(f"History Retrieved: {len(urls)}")

        filtered_urls = set(
            filterBlacklistedUrl(
                urls.values(),
                self.blacklist))
        print(f"URLS remaining after filtering: {len(filtered_urls)}")

        if self.isEmpty(filtered_urls):
            return ""
        else:
            return filtered_urls

    def isEmpty(self, urls):
        if len(urls) == 0:
            return True
        else:
            return False

    def startTasks(self):
        self.overwriteCSV()

        if self.isEmpty(self.urls):
            print("Nothing to scrape!")
            return ""

        queue = Queue()
        for url in self.urls:
            queue.put(url)
        print("URLs added to queue! \n\nScraping Sites: ")

        """
        asynchronous execution of tasks using threads
        use a with statement to ensure threads are cleaned up promptly
        """
        with futures.ThreadPoolExecutor(max_workers=MAX_WORKERS) as executor:
            threads = []
            i = 1
            while not queue.empty():
                url = queue.get()
                threads.append(
                    executor.submit(
                        Scraper().scrape,
                        url=url,
                        task=i))
                i += 1

            # Deal with the threads as they complete individually
            for future in futures.as_completed(threads):
                # tuple
                data = future.result()

                if data is not None:
                    url = data[0]
                    originalText = data[1]
                    # cleanedText = preProcess(originalText)
                    # store scraped data
                    self.writeToCSV(url, originalText)

        print("Finished Scraping!\n")
        return "scraped"

    def overwriteCSV(self):
        with open(
            self.scraped_csv, mode="w", encoding="utf-8", newline=""
        ) as scraped_text:
            fields = ["url", "original_data"]
            writer = csv.DictWriter(
                scraped_text, fieldnames=fields, delimiter=",")
            writer.writeheader()

    def writeToCSV(self, url, originalText):
        data = []
        with open(
            self.scraped_csv, mode="a+", encoding="utf-8", newline=""
        ) as scraped_text:
            writer = csv.writer(scraped_text, delimiter=",")

            for sentence in originalText:
                # remove silly sentences
                if len(sentence.split()) > 3:
                    data.append(sentence)

            writer.writerow([url, "|".join(data)])


def main():
    print(
        "Time filters include 'hour', 'day', 'week', 'month', or 'year' or '' (all time)."
    )
    filtr = input("Filter the date: ").capitalize()
    print(
        "Browser options include 'Chrome', 'Firefox', 'Safari', 'Edge', 'Opera', and 'Brave'."
    )
    browser = input("Enter the browser: ").capitalize()

    emot = Emot(filtr, browser)
    emot.startTasks()


if __name__ == "__main__":
    main()
