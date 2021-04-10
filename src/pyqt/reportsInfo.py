from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import QtChart
import pyqtgraph as pg

def setStats(self):

    self.commonTextEdit.setText(self.emotClassify.get_largest_emotion())
    self.positiveTextEdit.setText(self.emotClassify.get_sentence_intensity("joy"))
    self.angerTextEdit.setText(self.emotClassify.get_anger_total())
    self.fearTextEdit.setText(self.emotClassify.get_sentence_intensity("fear"))
    #TODO: self.websiteTextEdit.setText(SOME WEBSITE)

    self.browserUsedTextEdit.setText(self.getFilter())
    self.dateFiltrTextEdit.setText(self.getNumSites())

def showPieChart(self):

    emotionsDict = self.emotClassify.get_emotion_count()
    emotions = dict(sorted(emotionsDict.items(), key=lambda item: item[1], reverse= True))
    
    series = QtChart.QPieSeries()
    for emotion in emotions:
        series.append(emotion, emotionsDict[emotion])

    #adding slice
    slice = series.slices()[0]
    slice.setExploded(True)
    slice.setLabelVisible(True)
    slice.setPen(QtGui.QPen(QtCore.Qt.darkGreen, 2))
    slice.setBrush(QtCore.Qt.green)

    chart = QtChart.QChart()
    chart.legend().hide()
    chart.addSeries(series)
    chart.createDefaultAxes()
    chart.setAnimationOptions(QtChart.QChart.SeriesAnimations)
    chart.setTitle("Pie Chart")

    chart.legend().setVisible(True)
    chart.legend().setAlignment(QtCore.Qt.AlignBottom)

    chartview = QtChart.QChartView(chart)
    self.layout.addWidget(chartview)

def printTextInfo(self):
    print("\n")
    print(self.emotion_count)
    self.largest_emotion = [key for key in self.emotion_count.keys() if self.emotion_count[key] == max(self.emotion_count.values())]
    print(f"\nThe most prominent emotion that you read was {self.largest_emotion[0]}.")
    print(contentMessage(self))

    i = 1
    print("\nExamples of each emotion:")
    for emotion in self.emotion_intensity:
        print(f" {i}. {emotion} = '{self.sentence_intensity[emotion]}' with a score of {self.emotion_intensity[emotion]:.1%}")
        i+=1

        # print(self.emotion_intensity)
        # print(self.sentence_intensity)

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