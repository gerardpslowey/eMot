import copy
import os
import pickle
import threading

import pandas as pd

from utils.textMod import clean
from utils.urlFilter import base


class EmotClassify:
    """
    emotClassify produces metrics about the different emotions below seen in sites.
    It can be run on its own and information will print to the terminal.
    """

    def __init__(self, test=None):
        if test:
            os.chdir("..")

        self.emotions = [
            'anger',
            'fear',
            'sadness',
            'happiness',
            'joy',
            'surprise',
            'neutral'
        ]
        # treat anger, fear and sadness as negative
        self.negative = self.emotions[:len(self.emotions) // 2]
        # treat happy, joy and surprise as positive
        # but don't include neutral words
        self.positive = self.emotions[len(self.emotions) // 2:-1]

        # make a template dictionary setting the emotion count values to zero
        self.emotionsDict = dict.fromkeys(self.emotions, 0)

        self.emotionCounts = copy.deepcopy(self.emotionsDict)
        self.emotionIntensities = copy.deepcopy(self.emotionsDict)

        self.emotionsPerSite = {}

        self.sentenceExamples = set()

        self.siteScores = []

        self.siteVisitCounts = 0
        self.totalSiteCount = 0

        self.classifierModel1 = self.loadFiles("models/svc.pkl")  # svcModel
        self.tfidf = self.loadFiles("models/svc_tfidf.pkl")  # svcTfidfModel
        self.classifierModel2 = self.loadFiles("models/sgd.pkl")  # sgdModel
        self.cv = self.loadFiles("models/sgd_cv.pkl")  # sgd_cv_file

        # an empty array for line chart array values
        self.splitChartValues = []
        self.negativeWordcloud = []
        self.positiveWordcloud = []
        self.negativeSentenceList = []
        self.positiveSentenceList = []

        self.mostNegativeSite = None
        self.mostPositiveSite = None

        self.scrapedFile = "sentimentAnalysis/scraped.csv"

    def startAll(self):
        scraped_df = self.readScrapedFile()
        print("Classifying Scraped Data..")

        threads = []
        process1 = threading.Thread(
            target=self.sentenceClassify, args=(
                scraped_df,))
        threads.append(process1)

        process2 = threading.Thread(
            target=self.siteVisitCount, args=(
                scraped_df,))
        threads.append(process2)

        [process.start() for process in threads]
        [process.join() for process in threads]

    def readScrapedFile(self):
        scraped_df = pd.read_csv(
            self.scrapedFile).astype("U")

        # create a new column with the base baseUrl as its value
        scraped_df["base"] = scraped_df["url"].apply(base)
        # create a list of unique base sites
        sitesList = scraped_df["base"].unique().tolist()

        # stem the data for classification
        scraped_df["stemmedText"] = scraped_df["text"].apply(clean)

        # create a nested dictionary for each site
        for site in sitesList:
            # dictionary key maps to a nested dictionary
            self.emotionsPerSite[site] = copy.deepcopy(self.emotionsDict)
        return scraped_df

    # number of times a site is visited
    def siteVisitCount(self, scraped_df):
        print("Gathering Site Visit Counts..")
        self.siteVisitCounts = scraped_df["base"].value_counts().to_dict()

    def sentenceClassify(self, scraped_df):
        try:
            print("Analysing Sentences..")
            for row in scraped_df.itertuples(index=False):
                positiveSiteScore = 0
                negativeSiteScore = 0

                url = row[0]
                text = row[1]
                baseUrl = row[2]
                stemmedText = row[3]
                splitText = stemmedText.split("|")

                for sentence in splitText:
                    # label each sentence
                    emotionLabel1, emotionLabel2 = self.classifySentence(
                        sentence)

                    # get positive and negative site score
                    positiveSiteScore, negativeSiteScore = self.classifierModelAssertions(
                        baseUrl, emotionLabel1, emotionLabel2, positiveSiteScore, negativeSiteScore)

                    # score each sentence
                    sentimentScore1, sentimentScore2 = self.sentimentScore(
                        sentence)

                    averageEmotionIntensity = self.emotionIntensity(
                        sentimentScore1, sentimentScore2)

                    if averageEmotionIntensity > self.emotionIntensities.get(
                            emotionLabel1):
                        self.updateEmotionValues(
                            averageEmotionIntensity, text, splitText, sentence, emotionLabel1)

                # store site with associated positive and negative score
                positivePercentage, negativePercentage = self.posAndNegPercentage(
                    positiveSiteScore, negativeSiteScore
                )

                self.siteScores.append(
                    (url, positivePercentage, negativePercentage))

            print("Scoring Sentence Emotions..")
            self.processWordClouds(self.sentenceExamples)
            self.processSplitChartValues()
            self.mostPosandNeg(self.siteScores)

        except pd.errors.EmptyDataError:
            print("Nothing to Classify, The File is Empty")
        finally:
            print("Finished Classification!")

    # use 2 models to label the data
    def classifySentence(self, sentence):
        emotionLabel1 = self.classifierModel1.predict(
            self.tfidf.transform([sentence]))[0]
        emotionLabel2 = self.classifierModel2.predict(
            self.cv.transform([sentence]))[0]
        return emotionLabel1, emotionLabel2

    # use 2 models to score the data
    def sentimentScore(self, sentence):
        sentimentScore1 = self.classifierModel1.predict_proba(
            self.tfidf.transform([sentence]))
        sentimentScore2 = self.classifierModel2.predict_proba(
            self.cv.transform([sentence]))
        return sentimentScore1, sentimentScore2

    def classifierModelAssertions(
            self, baseUrl, emotionLabel1, emotionLabel2, positiveSiteScore, negativeSiteScore):
        # for a sentiment to be accepted both models have to agree on the label
        if emotionLabel1 == emotionLabel2:
            # count total emotion count
            self.emotionCounts[emotionLabel1] += 1
            # count of distribution of emotions per site
            self.emotionsPerSite[baseUrl][emotionLabel1] += 1
            if emotionLabel1 in self.positive:
                positiveSiteScore += 1
            else:
                negativeSiteScore += 1
        else:
            self.emotionCounts['neutral'] += 1
            self.emotionsPerSite[baseUrl]['neutral'] += 1

        return positiveSiteScore, negativeSiteScore

    def emotionIntensity(self, sentimentScore1, sentimentScore2):
        emotionIntensity1 = int(sentimentScore1.max() * 100)
        emotionIntensity2 = int(sentimentScore2.max() * 100)

        averageEmotionIntensity = (
            emotionIntensity1 + emotionIntensity2) / 2
        return averageEmotionIntensity

    def posAndNegPercentage(self, positiveSiteScore, negativeSiteScore):
        totalSiteSentimentCount = positiveSiteScore + negativeSiteScore
        if totalSiteSentimentCount == 0:
            totalSiteSentimentCount = 1

        positivePercentage = positiveSiteScore / totalSiteSentimentCount
        negativePercentage = negativeSiteScore / totalSiteSentimentCount
        return positivePercentage, negativePercentage

    def updateEmotionValues(self, averageEmotionIntensity,
                            text, splitText, sentence, emotionLabel1):
        self.emotionIntensities[emotionLabel1] = averageEmotionIntensity

        origText = text.split("|")
        sentenceIndex = splitText.index(sentence)
        originalSentence = origText[sentenceIndex]
        self.sentenceExamples.update(
            [(averageEmotionIntensity, emotionLabel1, originalSentence)])

    def mostPosandNeg(self, scores):
        self.mostPositiveSite = sorted(
            scores, key=lambda tup: tup[1], reverse=True)[0]
        self.mostNegativeSite = sorted(
            scores, key=lambda tup: tup[2], reverse=True)[0]

    def processWordClouds(self, sentences):
        # prepare some sentence examples for the wordcloud
        sentenceExampleList = list(sentences)
        # sort the list using the tuple structure
        sentenceExampleList.sort(key=lambda tup: tup[0], reverse=True)

        numRange = 10

        for item in sentenceExampleList[:numRange]:
            emotionLabel = item[1]
            sentence = item[2]

            if emotionLabel in self.negative:
                self.negativeWordcloud.append(sentence)
                self.negativeSentenceList.append(
                    f"{emotionLabel.upper()}\n{sentence.capitalize()}."
                )

            if emotionLabel in self.positive:
                self.positiveWordcloud.append(sentence)
                self.positiveSentenceList.append(
                    f"{emotionLabel.upper()}\n{sentence.capitalize()}."
                )

    def processSplitChartValues(self):
        # total site visits = the number of sites visited
        self.totalSiteCount = len(self.emotionsPerSite)

        for _ in range(self.totalSiteCount):
            for emotionsPerSite in self.emotionsPerSite.values():
                self.splitChartValues.append(list(emotionsPerSite.values()))

    def loadFiles(self, filename):
        with open(filename, "rb") as file:
            return pickle.load(file)  # noqa

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

    def getWordcloudBag(self):
        return self.negativeWordcloud, self.positiveWordcloud

    def getSentenceExamples(self):
        return self.negativeSentenceList, self.positiveSentenceList

    def getEmotionsPerSite(self):
        return self.emotionsPerSite

    def getMostPosandNeg(self):
        return self.mostNegativeSite[0], self.mostPositiveSite[0]


if __name__ == "__main__":
    test = EmotClassify()
    test.startAll()
