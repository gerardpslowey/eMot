import pandas as pd
import pickle
import threading
import logging
from utils.urlFilter import base
from pyqt import reportsInfo
import copy

scrapedFile = 'sentimentAnalysis/scraped.csv'

class EmotClassify:
    def __init__(self):
        self.emotions = ['anger', 'fear', 'joy', 'surprise', 'happiness', 'sadness']

        self.emotions_dict = dict.fromkeys(self.emotions, 0)

        self.emotion_count = {
            "anger": 0,
            "fear": 0,
            "joy": 0,
            "surprise": 0,
            "happiness": 0,
            "sadness": 0
        }

        self.emotion_intensity = {
            "anger": 0,
            "fear": 0,
            "joy": 0,
            "surprise": 0,
            "happiness": 0,
            "sadness": 0
        }

        self.site_visit_counts = None

        self.svc_model = "models/svc.pkl"
        self.svc_tfidf_file = "models/svc_tfidf.pkl"

        self.largest_emotion = None
        self.emotion_total = 0

    # number of times a site is visited
    def siteCount(self):
        # only load the urls column from the file
        urls_df = pd.read_csv(scrapedFile, usecols=["url"])
        urls_df['base'] = urls_df['url'].apply(base)
        self.site_visit_counts = urls_df.base.value_counts()
        print("Articles read per site")
        print(self.site_visit_counts.to_string())

    def sentenceClassify(self):
        scraped_df = pd.read_csv(scrapedFile)
        model = self.loadFiles(self.svc_model)
        tfidf = self.loadFiles(self.svc_tfidf_file)

        try:
            for row in scraped_df.itertuples(index=False):
                text = row[1]

                # score each sentence
                for sentence in text.split("."):
                    sentiment_score = model.predict_proba(tfidf.transform([sentence]))
                    sentiment_name = model.predict(tfidf.transform([sentence]))

                    emotion = sentiment_name[0]
                    intensity = sentiment_score.max()

                    # count in dictionary
                    self.emotion_count[emotion] += 1

                    if intensity > self.emotion_intensity.get(emotion):
                        # round the intensity float to 2 decimal place
                        self.emotion_intensity[emotion] = round(intensity, 2)

        except pd.errors.EmptyDataError:
            print("Nothing to classify, the file is empty")
        finally:
            print("\nEmotion Intensities")
            print(self.emotion_intensity)
            print("\nEmotion Counts")
            print(self.emotion_count)

    def documentClassify(self):
        scraped_document_df = pd.read_csv(scrapedFile)

        model = self.loadFiles(self.svc_model)
        tfidf = self.loadFiles(self.svc_tfidf_file)

        scraped_document_df['base'] = scraped_document_df['url'].apply(base)
        # create a list of unique base sites
        sitesList = scraped_document_df['base'].unique().tolist()
        # create a nested dictionary for each site
        # TODO do a write up on this shallow vs deepcopies
        sites = {}
        for site in sitesList:
            sites[site] = copy.deepcopy(self.emotions_dict)

        try:
            for row in scraped_document_df.itertuples(index=False):
                text = row[1]
                url = row[2]             

                # classify on document level
                sentiment_name = model.predict(tfidf.transform([text]))
                emotion = sentiment_name[0]

                sites[url][emotion] += 1

        except pd.errors.EmptyDataError:
            print("Nothing to classify, the file is empty")
        finally:
            print("\nSites and associated article primary emotion")
            print(sites)

    def loadFiles(self, filename):
        with open(filename, 'rb') as file:
            return pickle.load(file)

    def get_emotion_count(self):
        return self.emotion_count

    def get_emotion_intensity(self):
        return self.emotion_intensity

    def get_site_count(self):
        return self.site_visit_counts

    def get_sentence_intensity(self, emotion=None):
        if emotion is None:
            return self.sentence_intensity
        else:
            return self.sentence_intensity[emotion]

    def get_largest_emotion(self):
        return self.largest_emotion[0]


def main():
    test = EmotClassify()

    threads = []
    process1 = threading.Thread(target=test.sentenceClassify)
    process1.start()
    threads.append(process1)

    process2 = threading.Thread(target=test.siteCount)
    process2.start()
    threads.append(process2)

    process3 = threading.Thread(target=test.documentClassify)
    process3.start()
    threads.append(process3)

    for process in threads:
        process.join()

if __name__ == '__main__':
    main()
