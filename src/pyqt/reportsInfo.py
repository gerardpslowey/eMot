from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import QtChart
import pyqtgraph as pg
# flake8: noqa

import dash
import dash_core_components as dcc
import dash_html_components as html

def setStats(self):
    self.emotClassify.get_largest_emotion()
    self.emotClassify.get_sentence_intensity("joy")
    self.emotClassify.get_anger_total()
    self.emotClassify.get_sentence_intensity("fear")
    self.getFilter()
    self.getNumSites()

    emotionsDict = self.emotClassify.get_emotion_count()
    emotions = dict(sorted(emotionsDict.items(), key=lambda item: item[1], reverse= True))
    
    # series = QtChart.QPieSeries()
    # for emotion in emotions:
    #     series.append(emotion, emotionsDict[emotion])

def printTextInfo(self):
    print(self.emotion_count)
    self.largest_emotion = [key for key in self.emotion_count.keys() if self.emotion_count[key] == max(self.emotion_count.values())]
    print(f"\nThe most prominent emotion that you read was {self.largest_emotion[0]}.")
    print(contentMessage(self))

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
