import pandas as pd
import pickle
import threading
from utils.urlFilter import base
import copy

scrapedFile = 'sentimentAnalysis/scraped.csv'


class EmotClassify:
    def __init__(self):
        self.emotions = ['anger', 'fear', 'sadness', 'happiness', 'joy', 'surprise', 'neutral']
        # make a template dictionary setting the emotion count values to zero
        self.emotionsDict = dict.fromkeys(self.emotions, 0)

        self.emotionCounts = copy.deepcopy(self.emotionsDict)
        self.emotionIntensities = copy.deepcopy(self.emotionsDict)

        self.emotionsPerSite = {}

        self.sentenceExamples = set()

        self.siteVisitCounts = None
        self.totalSiteCount = 0

        self.classifierModel1 = self.loadFiles("models/svc.pkl")    # svcModel
        self.tfidf = self.loadFiles("models/svc_tfidf.pkl")         # svcTfidfModel
        self.classifierModel2 = self.loadFiles("models/sgd.pkl")    # sgdModel
        self.cv = self.loadFiles("models/sgd_cv.pkl")               # sgd_cv_file

        # an empty array for line chart array values
        self.splitChartValues = []
        self.negativeWordcloud = []
        self.positiveWordcloud = []

    def startAll(self):
        scraped_df = self.readScrapedFile()

        threads = []
        process1 = threading.Thread(target=self.sentenceClassify, args=(scraped_df,))
        threads.append(process1)

        process2 = threading.Thread(target=self.siteVisitCount, args=(scraped_df,))
        threads.append(process2)

        for process in threads:
            process.start()

        for process in threads:
            process.join()

    def readScrapedFile(self):
        # read scraped file
        scraped_df = pd.read_csv(scrapedFile).astype('U')
        # create a new column with the base baseUrl as its value
        scraped_df['base'] = scraped_df['url'].apply(base)
        # create a list of unique base sites
        sitesList = scraped_df['base'].unique().tolist()
        # create a nested dictionary for each site
        for site in sitesList:
            # dictionary key maps to a nested dictionary
            self.emotionsPerSite[site] = copy.deepcopy(self.emotionsDict)
        return scraped_df

    # number of times a site is visited
    def siteVisitCount(self, scraped_df):
        self.siteVisitCounts = scraped_df['base'].value_counts().to_dict()
        self.prettyPrint(self.siteVisitCounts.items())

    def sentenceClassify(self, scraped_df):
        try:
            for row in scraped_df.itertuples(index=False):
                text = row[1]
                baseUrl = row[2]

                # score each sentence
                for sentence in text.split("|"):
                    sentimentScore1 = self.classifierModel1.predict_proba(self.tfidf.transform([sentence]))
                    sentimentScore2 = self.classifierModel2.predict_proba(self.cv.transform([sentence]))

                    # use 2 models to score the data for comparison
                    emotionIntensity1 = int(sentimentScore1.max() * 100)
                    emotionIntensity2 = int(sentimentScore2.max() * 100)
                    averageEmotionIntensity = (emotionIntensity1 + emotionIntensity2) / 2
                    emotionIntensity = averageEmotionIntensity

                    emotionLabel1 = self.classifierModel1.predict(self.tfidf.transform([sentence]))[0]
                    emotionLabel2 = self.classifierModel2.predict(self.cv.transform([sentence]))[0]

                    # for a sentiment to be accepted both models have to have a score greater than 0.6
                    if emotionLabel1 == emotionLabel2:
                        self.emotionCounts[emotionLabel1] += 1              # count total emotion count
                        self.emotionsPerSite[baseUrl][emotionLabel1] += 1   # count of distribution of emotions per site
                    else:
                        # count total emotion count
                        self.emotionCounts['neutral'] += 1
                        # count of distribution of emotions per site
                        self.emotionsPerSite[baseUrl]['neutral'] += 1

                    if emotionIntensity > self.emotionIntensities.get(emotionLabel1):
                        self.emotionIntensities[emotionLabel1] = emotionIntensity
                        self.sentenceExamples.update([tuple((emotionIntensity, emotionLabel1, sentence))])

            self.processWordClouds(list(self.sentenceExamples))
            self.processSplitChartValues()

        except pd.errors.EmptyDataError:
            print("Nothing to classify, the file is empty")
        finally:
            self.prettyPrint(self.emotionIntensities.items(), "percent")
            self.prettyPrint(self.emotionCounts.items(), "amount")
            self.prettyPrint(self.emotionsPerSite.items(), "lst")

    def processWordClouds(self, sentences):
        sentenceExampleList = sentences     # prepare some sentence examples for the wordcloud
        sentenceExampleList.sort(key=lambda tup: tup[0], reverse=True)
        halfListRange = int(len(sentenceExampleList) / 2)

        negative = self.emotions[:len(self.emotions) // 2]
        # dont include neutral words
        positive = self.emotions[len(self.emotions) // 2:-1]
        print("\nExamples of emotion based sentences: ")

        for item in sentenceExampleList[:halfListRange]:

            if item[1] in negative:
                self.negativeWordcloud.append(item[2])

            if item[1] in positive:
                self.positiveWordcloud.append(item[2])

            print(f"{item[0]}% {item[1]} = {item[2]}")

    def processSplitChartValues(self):
        # total site visits = the number of sites visited
        self.totalSiteCount = len(self.emotionsPerSite)

        for _ in range(self.totalSiteCount):
            for emotionsPerSite in self.emotionsPerSite.values():
                self.splitChartValues.append(list(emotionsPerSite.values()))

    def prettyPrint(self, items, format=None):

        if format == "lst":
            print("\nSites and associated primary emotions: ")
            print(f"website: {*self.emotions,}")
            for key, value in items:
                print(f"{key}: {*list(value.values()),}")

        elif format == "percent":
            print("\nThe Intensity level of each Emotion:")
            for key, value in items:
                print(f"{key}: {value}%")

        elif format == "amount":
            print("\nThe Amount of each Emotion:")
            for key, value in items:
                print(f"{key}: {value}")

        else:
            print("Articles read per site: ")
            for key, value in items:
                print(f"{key}: {value}")

    def loadFiles(self, filename):
        with open(filename, 'rb') as file:
            return pickle.load(file)

    def getEmotions(self):
        return self.emotions

    def getEmotionCounts(self):
        return self.emotionCounts

    def getEmotionIntensities(self):
        return self.emotionIntensities

    def getSiteVisitCounts(self):
        return self.siteVisitCounts

    def getUniqueSiteCount(self):
        return self.totalSiteCount

    def getSplitChartValues(self):
        return self.splitChartValues

    def getWordCloudBag(self):
        return self.negativeWordcloud, self.positiveWordcloud

    def getEmotionsPerSite(self):
        return self.emotionsPerSite


if __name__ == '__main__':
    test = EmotClassify()
    test.startAll()
