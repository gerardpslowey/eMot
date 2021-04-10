import pandas as pd
import pickle
from pyqt import reportsInfo

from urlProcessor.urlFilter import base

import sys

import threading

import dash
import dash_core_components as dcc
import dash_html_components as html

class EmotClassify:

    def __init__(self):
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

        # 'anger', 'fear', 'joy', 'surprise', 'happiness', 'sadness'

        self.svc_model = "models/svc.pkl"
        self.svc_tfidf_file = "models/svc_tfidf.pkl"

        self.largest_emotion = None
        self.emotion_total = 0

    def classify(self):
    
        df = pd.read_csv('sentimentAnalysis/scraped.csv')

        # Sort out urls first
        urls_df = pd.DataFrame(df['url'])
        urls_df['base'] = urls_df['url'].apply(base)

        print(urls_df.base.value_counts())


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

    def loadFiles(self, filename):
        with open(filename, 'rb') as file:
            return pickle.load(file)

    def get_emotion_count(self):
        return self.emotion_count

    def get_emotion_intensity(self):
        return self.emotion_intensity

    def get_sentence_intensity(self, emotion=None):
        if emotion is None:
            return self.sentence_intensity
        else:
            return self.sentence_intensity[emotion]

    def get_largest_emotion(self):
        return self.largest_emotion[0]

    def run_dash(self, data, layout):
        app = dash.Dash()

        app.layout = html.Div(children=[
            html.H1(children='Hello Dash'),

            html.Div(children='''
                Dash: A web application framework for Python.
            '''),

            dcc.Graph(
                id='example-graph',
                figure={
                    'data': data,
                    'layout': layout
                })
            ])
        app.run_server(debug=False)

if __name__ == '__main__':
    test = EmotClassify()
    test.classify()
