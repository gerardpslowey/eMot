import pandas as pd
import pickle
import threading
import logging

from utils.urlFilter import base
from pyqt import reportsInfo

import dash
import dash_core_components as dcc
import dash_html_components as html


class EmotClassify:
    def __init__(self):
        # 'anger', 'fear', 'joy', 'surprise', 'happiness', 'sadness'
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

        self.df = pd.read_csv('sentimentAnalysis/scraped.csv')

    # number of times a site is visited
    def siteCount(self):
        urls_df = pd.DataFrame(self.df['url'])
        urls_df['base'] = urls_df['url'].apply(base)
        self.site_visit_counts = urls_df.base.value_counts()

    def classify(self):
        model = self.loadFiles(self.svc_model)
        tfidf = self.loadFiles(self.svc_tfidf_file)

        try:
            # rows
            for _, row in self.df.iterrows():
                # columns
                for _, values in row.iteritems():

                    # individual page sentences
                    values = values.split(".")

                    # score each sentence
                    for value in values:
                        # print(value)

                        sentiment_score = model.predict_proba(tfidf.transform([value]))
                        sentiment_name = model.predict(tfidf.transform([value]))

                        emotion = sentiment_name[0]
                        intensity = sentiment_score.max()

                        self.emotion_count[emotion] += 1

                        if intensity > self.emotion_intensity.get(emotion):
                            self.emotion_intensity[emotion] = intensity

        except pd.errors.EmptyDataError:
            print("Panda file is empty")

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

    def run_dash(self, data, layout):
        app = dash.Dash()
        log = logging.getLogger('werkzeug')
        log.setLevel(logging.ERROR)
        
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
        app.run_server(debug=False, port=8051)


def main():
    test = EmotClassify()

    threads = []
    process1 = threading.Thread(target=test.classify)
    process1.start()
    threads.append(process1)

    process2 = threading.Thread(target=test.siteCount)
    process2.start()
    threads.append(process2)

    for process in threads:
        process.join()

    # data = [
    #     {'x': [1, 2, 3], 'y': [4, 1, 2], 'type': 'bar', 'name': 'SF'},
    #     {'x': [1, 2, 3], 'y': [2, 4, 5], 'type': 'bar', 'name': u'Montréal'},
    # ]

    # layout = {
    #     'title': 'Dash Data Visualization'
    # }

    # threading.Thread(target=reportsInfo.run_dash, args=(test, data, layout), daemon=True).start()
    # reportsInfo.run_dash(test, data, layout)


if __name__ == '__main__':
    main()
