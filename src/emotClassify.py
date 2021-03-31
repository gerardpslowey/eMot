import pandas as pd
import pickle
import csv

import numpy as np
import matplotlib.pyplot as plt

def classify():

    emotion_count = {
        "joy":0,
        "sadness":0,
        "anger":0,
        "neutral":0,
        "fear":0
    }

    SVC_Model = "models/svc.pkl"
    SVC_TFIDF_File = "models/svc_tfidf.pkl"

    model = loadFiles(SVC_Model)
    tfidf = loadFiles(SVC_TFIDF_File)

    with open('sentimentAnalysis/scraped.csv', encoding='utf-8') as scraped_file:
        scraped_text_file = csv.reader(scraped_file, delimiter=',')
        
        for row in scraped_text_file:
            for column in row:
                # sentiment_score = model.predict_proba(tfidf.transform([column]))
                sentiment_name = model.predict(tfidf.transform([column]))

                emotion = sentiment_name[0]

                if emotion_count.get(emotion) == 0:
                    emotion_count[emotion] = 1  
                else:
                    emotion_count[emotion] += 1


        print(emotion_count)

        plt.pie([float(emotion_count[v]) for v in emotion_count], labels=[str(k) for k in emotion_count], autopct='%1.1f%%')
        plt.show()

def loadFiles(filename):
    with open(filename, 'rb') as file:
        return pickle.load(file)


if __name__ == '__main__':
    classify()