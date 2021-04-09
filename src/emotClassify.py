import pandas as pd
import pickle
import csv

import numpy as np
import matplotlib.pyplot as plt
from pyqt import reportsInfo

class EmotClassify:

    def __init__(self):
        self.emotion_count = {
            "anger":0,
            "fear":0,
            "joy":0,
            "surprise":0,
            "happiness":0
        }

        self.emotion_intensity = {
            "anger":0,
            "fear":0,
            "joy":0,
            "surprise":0,
            "happiness":0
        }

        self.sentence_intensity = {
            "anger":"None",
            "fear":"None",
            "joy":"None",
            "surprise":"None",
            "happiness":"None"
        }

        self.svc_model = "models/svc.pkl"
        self.svc_tfidf_file = "models/svc_tfidf.pkl"

        self.largest_emotion = None
        self.emotion_total = 0

    def classify(self):
        try:
            df = pd.read_csv('sentimentAnalysis/scraped.csv')

            model = self.loadFiles(self.svc_model)
            tfidf = self.loadFiles(self.svc_tfidf_file)

            for i, row in df.iterrows():
                row = row.str.split(pat=".", expand=True)

                for _, values in row.iteritems():
                    value = values[0]
                    sentiment_score = model.predict_proba(tfidf.transform([value]))
                    sentiment_name = model.predict(tfidf.transform([value]))

                    emotion = sentiment_name[0]
                    intensity = sentiment_score.max()

                    if self.emotion_count.get(emotion) == 0:
                        self.emotion_count[emotion] = 1  
                    else:
                        self.emotion_count[emotion] += 1
                    self.emotion_total += 1
                
                    if intensity > self.emotion_intensity.get(emotion):
                        self.emotion_intensity[emotion] = intensity
                        self.sentence_intensity[emotion] = value

            reportsInfo.printTextInfo(self)
        except pd.errors.EmptyDataError:
            print("Panda file is empty")

    def loadFiles(self,filename):
        with open(filename, 'rb') as file:
            return pickle.load(file)

    def get_emotion_count(self):
        return self.emotion_count

    def get_emotion_intensity(self):
        return self.emotion_intensity

    def get_sentence_intensity(self, emotion=None):
        if emotion==None:
            return self.sentence_intensity
        else:
            return self.sentence_intensity[emotion]

    def get_largest_emotion(self):
        return self.largest_emotion[0]

    def get_anger_total(self):
        if self.emotion_total != 0:
            return f"{self.emotion_count['anger'] / self.emotion_total:.1%}"
        else:
            return 0


if __name__ == '__main__':
    test = EmotClassify()
    test.classify()
