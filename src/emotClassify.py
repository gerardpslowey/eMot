import pandas as pd
import pickle
import threading
from utils.urlFilter import base
import copy

scrapedFile = 'sentimentAnalysis/scraped.csv'


class EmotClassify:
    def __init__(self):
        self.emotions = ['anger', 'fear', 'joy', 'surprise', 'happiness', 'sadness']
        # make a nested dictionary setting the emotion_1 count values to zero
        self.emotionsDict = dict.fromkeys(self.emotions, 0)

        self.emotionCounts = copy.deepcopy(self.emotionsDict)
        self.emotionIntensities = copy.deepcopy(self.emotionsDict)

        self.emotionsPerSite = {}

        self.sentenceExamples = set()

        self.siteVisitCounts = None
        self.totalSiteCount = 0

        self.svcModel = "models/svc.pkl"
        self.svcTfidfModel = "models/svc_tfidf.pkl"
        self.sgdModel = "models/sgd.pkl"
        self.sgd_cv_file = "models/sgd_cv.pkl"

        self.model_1 = self.loadFiles(self.svcModel)
        self.tfidf = self.loadFiles(self.svcTfidfModel)
        self.model_2 = self.loadFiles(self.sgdModel)
        self.cv = self.loadFiles(self.sgd_cv_file)

        # an empty array for line chart array values
        self.splitChartValues = []
        self.wordCloudBag = []

    # number of times a site is visited
    def siteCount(self):
        # only load the urls column from the file
        urls_df = pd.read_csv(scrapedFile, usecols=["url"]).astype('U')
        urls_df['base'] = urls_df['url'].apply(base)
        self.siteVisitCounts = urls_df['base'].value_counts().to_dict()

        print("Articles read per site: ")
        self.prettyPrint(self.siteVisitCounts.items())

    def sentenceClassify(self):
        # read scraped file
        scraped_df = pd.read_csv(scrapedFile).astype('U')
        # create a new column with the base url as its value
        scraped_df['base'] = scraped_df['url'].apply(base)
        # create a list of unique base sites
        sitesList = scraped_df['base'].unique().tolist()
        # create a nested dictionary for each site
        for site in sitesList:
            # dictionary key maps to a nested dictionary
            self.emotionsPerSite[site] = copy.deepcopy(self.emotionsDict)

        try:
            for row in scraped_df.itertuples(index=False):
                text = row[1]
                url = row[2]

                # score each sentence
                for sentence in text.split("|"):
                    sentiment_score_1 = self.model_1.predict_proba(self.tfidf.transform([sentence]))
                    sentiment_score_2 = self.model_2.predict_proba(self.cv.transform([sentence]))

                    # use 2 models to score the data for comparison
                    intensity_1 = sentiment_score_1.max()
                    intensity_2 = sentiment_score_2.max()
                    intensity = (intensity_1 + intensity_2) / 2

                    sentiment_name_1 = self.model_1.predict(self.tfidf.transform([sentence]))
                    sentiment_name_2 = self.model_2.predict(self.cv.transform([sentence]))
                    emotion_1 = sentiment_name_1[0]
                    emotion_2 = sentiment_name_2[0]

                    # for a sentiment to be accepted both models have to have a score greater than 0.6
                    if intensity_1 >= 0.6 and intensity_2 >= 0.6 and emotion_1 == emotion_2:
                        # count total emotion count
                        self.emotionCounts[emotion_1] += 1
                        # count of distribution of emotions per site
                        self.emotionsPerSite[url][emotion_1] += 1

                    if intensity > self.emotionIntensities.get(emotion_1):
                        # round the intensity float to 2 decimal place
                        self.emotionIntensities[emotion_1] = round(intensity, 2)
                        self.wordCloudBag.append(sentence)
                        self.sentenceExamples.update([tuple((round(intensity, 2), emotion_1, sentence))])

            # process split chart values
            self.processSplitChartValues()

        except pd.errors.EmptyDataError:
            print("Nothing to classify, the file is empty")
        finally:
            print("\nThe Intensity level of each Emotion:")
            self.prettyPrint(self.emotionIntensities.items(), "percent")

            print("\nThe Amount of each Emotion:")
            self.prettyPrint(self.emotionCounts.items())

            print("\nSites and associated article primary emotion_1: ")
            print(f"website: {*self.emotions,}")
            self.prettyPrint(self.emotionsPerSite.items(), "lst")

            print("\nExamples of emotion_1 based sentences: ")
            sentenceExampleList = list(self.sentenceExamples)
            sentenceExampleList.sort(key=lambda tup: tup[0], reverse=True)
            for item in sentenceExampleList[0:int(len(sentenceExampleList) / 2)]:
                print(f"{item[0]:.1%} {item[1]} = {item[2]}")

    def processSplitChartValues(self):
        # total site visits = the number of sites visited
        self.totalSiteCount = len(self.emotionsPerSite)

        for _ in range(self.totalSiteCount):
            for emotionsPerSite in self.emotionsPerSite.values():
                self.splitChartValues.append(list(emotionsPerSite.values()))

    def prettyPrint(self, items, format=None):
        for key, value in items:

            if format == "lst":
                print(f"{key}: {*list(value.values()),}")

            elif format == "percent":
                print(f"{key}: {value:.1%}")

            else:
                print(f"{key}: {value}")

    def loadFiles(self, filename):
        with open(filename, 'rb') as file:
            return pickle.load(file)

    def getEmotions(self):
        return self.emotions

    def getEmotionCount(self):
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
        return self.wordCloudBag

    def getEmotionsPerSite(self):
        return self.emotionsPerSite

    def startAll(self):
        threads = []
        process1 = threading.Thread(target=self.sentenceClassify)
        process1.start()
        threads.append(process1)

        process2 = threading.Thread(target=self.siteCount)
        process2.start()
        threads.append(process2)

        for process in threads:
            process.join()


if __name__ == '__main__':
    test = EmotClassify()
    test.startAll()
