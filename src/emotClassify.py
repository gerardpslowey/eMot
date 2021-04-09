import pandas as pd
import pickle
import csv

import numpy as np
import matplotlib.pyplot as plt

from urlProcessor.urlFilter import base

class EmotClassify:

    def __init__(self):
        self.emotion_count = {
            "anger":0,
            "fear":0,
            "joy":0,
            "surprise":0,
            "happiness":0,
            "sadness":0
        }

        self.emotion_intensity = {
            "anger":0,
            "fear":0,
            "joy":0,
            "surprise":0,
            "happiness":0,
            "sadness":0
        }

        self.sentence_intensity = {
            "anger":0,
            "fear":0,
            "joy":0,
            "surprise":0,
            "happiness":0,
            "sadness":0
        }
        # 'anger', 'fear', 'joy', 'surprise', 'happiness', 'sadness'

        self.svc_model = "models/svc.pkl"
        self.svc_tfidf_file = "models/svc_tfidf.pkl"

        self.largest_emotion = None

    def classify(self):
    
        df = pd.read_csv('sentimentAnalysis/scraped.csv')

        # Sort out urls first
        urls_df = pd.DataFrame(df['url'])
        urls_df['base'] = urls_df['url'].apply(base)

        urls_df.base.value_counts().plot(kind='barh')
        plt.xlabel('No. of Products');


        # for _, row in urls_df.iterrows():
        #     for name, values in row.iteritems():
        #         print('{name}: {value}'.format(name=name, value=values))

        model = self.loadFiles(self.svc_model)
        tfidf = self.loadFiles(self.svc_tfidf_file)


        # looking at 
        # for _, row in df.iterrows():
        #     for name, values in row.iteritems():
        #         print('{name}: {value}'.format(name=name, value=values))

        #         row = row.str.split(pat=".", expand=True)

                # for _, values in row.iteritems():
                #     value = values[0]
                #     print(value)
                    # sentiment_score = model.predict_proba(tfidf.transform([value]))
                    # sentiment_name = model.predict(tfidf.transform([value]))

                    # emotion = sentiment_name[0]
                    # intensity = sentiment_score.max()

                    # if self.emotion_count.get(emotion) == 0:
                    #     self.emotion_count[emotion] = 1  
                    # else:
                    #     self.emotion_count[emotion] += 1
                
                    # if intensity > self.emotion_intensity.get(emotion):
                    #     self.emotion_intensity[emotion] = intensity
                    #     self.sentence_intensity[emotion] = value


        print("\n")
        print(self.emotion_count)
        self.largest_emotion = [key for key in self.emotion_count.keys() if self.emotion_count[key] == max(self.emotion_count.values())]
        print(f"\nThe most prominent emotion that you read was {self.largest_emotion[0]}.")
        print(self.contentMessage())

        i = 1
        print("\nExamples of each emotion:")
        for emotion in self.emotion_intensity:
            print(f" {i}. {emotion} = '{self.sentence_intensity[emotion]}' with a score of {self.emotion_intensity[emotion]}")
            i+=1

            # print(self.emotion_intensity)
            # print(self.sentence_intensity)

            # plt.pie([float(emotion_count[v]) for v in emotion_count], labels=[str(k) for k in emotion_count], autopct='%1.1f%%')
            # plt.show()

    def loadFiles(self,filename):
        with open(filename, 'rb') as file:
            return pickle.load(file)

    def contentMessage(self):
        if self.largest_emotion[0] == 'joy':
            return "This is great! You are looking at happy content on the web."
        elif self.largest_emotion[0] == 'sadness':
            return "Oh no! You are looking at content that is primarily sad. Try to stay away from websites that have negative content."
        elif self.largest_emotion[0] == 'anger':
            return "You are consuming content that can invoke anger. We recommend that you try to avoid this sort of content."
        elif self.largest_emotion[0] == 'fear':
            return "You are reading fear based content. Oh no! You should try to avoid this sort of content."
        else:
            return "This is good. You aren't viewing content that is very emotional."

    def get_emotion_count(self):
        return self.emotion_count

    def get_emotion_intensity(self):
        return self.emotion_intensity

    def get_sentence_intensity(self):
        return self.sentence_intensity

    def get_biggest_emotion(self):
        return self.largest_emotion[0]

if __name__ == '__main__':
    test = EmotClassify()
    test.classify()