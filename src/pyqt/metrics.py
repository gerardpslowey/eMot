import sys

import funcy
from PyQt5 import QtCore
from PyQt5.QtChart import (QBarCategoryAxis, QBarSeries, QBarSet,
                           QCategoryAxis, QChart, QLineSeries,
                           QPercentBarSeries, QPieSeries, QValueAxis)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QColor, QFont, QPainter, QPen, QPixmap
from PyQt5.QtWidgets import QMainWindow

from pyqt.metrics_window import Ui_MetricsDashboard

colours = [
    QColor("#D8345F"),  # cerise
    QColor("#26474E"),  # Dark slate gray
    QColor("#A3DDCB"),  # middle blue green
    QColor("#5AA469"),  # forest green crayola
    QColor("#F9968B"),  # congo pink
    QColor("#8B5E83"),  # antique fuchsia
    QColor("#c0c0c0"),  # default grey for neutral
]


class MetricsDashboard(QMainWindow, Ui_MetricsDashboard):
    """
    Super class of metrics_windows.
    Class can be overwritten when converting from QT Designer UI file.
    This extended class to add functionality to the charts and wordclouds.
    """

    def __init__(self, browser, filtr, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)
        self.setWindowTitle("Metrics Dashboard")
        self.browserUsedEdit.setText(browser)
        self.dateUsedEdit.setText(filtr)

        self.stackedWidget.setCurrentWidget(self.chartPage)
        self.nextPageButton.clicked.connect(
            lambda: self.changePage(self.chartPage2)
        )
        self.nextPage2Button.clicked.connect(
            lambda: self.changePage(self.wordCloudPage)
        )
        self.previousPageButton.clicked.connect(
            lambda: self.changePage(self.chartPage2)
        )
        self.previousPage2Button.clicked.connect(
            lambda: self.changePage(self.chartPage)
        )
        self.font = QFont()
        self.font.setPixelSize(20)

    def displaySentenceExamples(self, sentences, prefix):
        posNeg = prefix + "SentEdit"
        # negativeSentEdit, positiveSentEdit
        sentenceEdit = getattr(self, posNeg)
        for sentence in sentences:
            sentenceEdit.setText(f"{sentenceEdit.text()}{sentence}\n\n")

    def showImage(self, image, prefix):
        self.image = QPixmap(image)
        posNeg = prefix + "Wordcloud"
        wordcloud = getattr(self, posNeg)
        self.image.scaled(wordcloud.size(), Qt.KeepAspectRatio)
        wordcloud.setPixmap(self.image)
        wordcloud.setScaledContents(True)

    def changePage(self, site):
        self.stackedWidget.setCurrentWidget(site)

    def makeCharts(self, emotClassify):
        self.emotions = emotClassify.getEmotions()

        self.emotionsPerSite = emotClassify.getEmotionsPerSite()
        self.uniqueSiteCount = emotClassify.getUniqueSiteCount()
        self.keys = ["neutral"]

        numEmotions = len(self.emotions)
        self.makePieChart(
            emotClassify.getEmotionCounts()  # pie chart data
        )
        self.makeLineChart(
            emotClassify.getEmotionIntensities()  # line chart data
        )
        self.makeSplitChart(
            numEmotions,
            emotClassify.getSplitChartValues()  # split chart data
        )
        self.makeBarChart(
            numEmotions,
            emotClassify.getSiteVisitCounts()  # bar chart data
        )

    def makeBarChart(self, numEmotions, siteVisits):
        maxLimit = 10 if len(siteVisits) < 10 else len(siteVisits)
        barSets = [QBarSet(site)
                   for site in list(siteVisits.keys())[:maxLimit]]
        series = QBarSeries()

        for i, value in enumerate(siteVisits.values()):
            barSets[i].append(value)
            # add number of visits to set
            series.append(barSets[i])
            barSets[i].setColor(colours[i % numEmotions])

        chart = QChart()
        chart.addSeries(series)

        chart.setTitleFont(self.font)
        chart.setTitle("Most Visited Sites")

        yAxis = QValueAxis()
        try:
            largestSiteVisitCount = max(siteVisits.values())
        except ValueError:
            largestSiteVisitCount = 1

        yAxis.setRange(0, largestSiteVisitCount)
        yAxis.setLabelFormat("%d")
        yAxis.setTickCount(largestSiteVisitCount + 1)
        yAxis.setTitleText("Number of visits")
        yAxis.setGridLineVisible(True)

        chart.setAnimationOptions(QChart.SeriesAnimations)
        chart.legend().setVisible(True)
        chart.legend().setAlignment(Qt.AlignBottom)
        chart.addAxis(yAxis, Qt.AlignLeft)
        series.attachAxis(yAxis)

        self.barChart.setChart(chart)

    def makeSplitChart(self, numEmotions, splitChartValues):
        # create a new QBarSet for each emotion
        barSets = [QBarSet(emotion) for emotion in self.emotions]
        series = QPercentBarSeries()

        # for top 10 websites
        maxLimit = 10 if self.uniqueSiteCount < 10 else self.uniqueSiteCount
        for i in range(maxLimit):
            # iterate through the array of emotions associated with that site
            barStatArray = splitChartValues[i]
            for emotion in range(len(barStatArray)):
                # add that emotion to the barset
                barSets[emotion].append(barStatArray[emotion])

        # append the completed barSet to the series
        for i in range(len(barSets)):
            series.append(barSets[i])
            # set the custom colours
            barSets[i].setColor(colours[i % numEmotions])

        chart = QChart()
        chart.addSeries(series)

        chart.setTitleFont(self.font)
        chart.setTitle("Emotions Seen Per Site")
        chart.setAnimationOptions(QChart.SeriesAnimations)

        # categories are the website names
        categories = list(self.emotionsPerSite.keys())[:maxLimit]
        # custom x axis
        axisX = QBarCategoryAxis()
        axisX.append(categories)

        # custom y axis
        axisY = QValueAxis()
        axisY.setTickCount(11)
        axisY.setRange(0, 100)
        axisY.setTitleText("% Emotion Per Site")

        chart.setAxisX(axisX, series)
        chart.setAxisY(axisY)

        chart.legend().setVisible(True)
        chart.legend().setAlignment(Qt.AlignBottom)

        self.splitChart.setChart(chart)

    def makePieChart(self, emotionCounts):
        pieEmotions = funcy.omit(emotionCounts, "neutral")
        # get the data
        series = QPieSeries()
        for i, (emotion, value) in enumerate(pieEmotions.items()):
            slices = series.append(emotion, value)
            slices.setBrush(colours[i])

        largest = max(pieEmotions, key=pieEmotions.get)
        index = list(pieEmotions.keys()).index(largest)
        # largest emotion
        pieSlice = series.slices()[index]
        pieSlice.setExploded(True)
        pieSlice.setLabelVisible(True)
        pieSlice.setPen(QPen(QtCore.Qt.black, 2))  # the border colour

        chart = QChart()
        chart.addSeries(series)

        chart.setTitleFont(self.font)
        chart.setTitle("Overall Emotion Counts Of Sentences")
        chart.createDefaultAxes()

        chart.legend().setVisible(True)
        chart.legend().setAlignment(Qt.AlignBottom)
        chart.setAnimationOptions(QChart.SeriesAnimations)
        self.pieChart.setChart(chart)
        self.pieChart.setRenderHint(QPainter.Antialiasing)

    def makeLineChart(self, emotionIntensities):
        series = QLineSeries()
        series.setPointLabelsVisible(True)
        series.setPointLabelsColor(Qt.black)
        series.setPointLabelsFormat("@yPoint" + "%")

        lineEmotions = funcy.omit(emotionIntensities, "neutral")

        for i, emotion in enumerate(lineEmotions.keys()):
            i += 0.5
            series.append(i, lineEmotions[emotion])

        yAxis = QValueAxis()
        yAxis.setRange(0, 100)
        yAxis.setLabelFormat("%.1f")
        yAxis.setTickCount(5)
        yAxis.setTitleText("Intensity (%)")
        yAxis.setGridLineVisible(False)

        xAxis = QCategoryAxis()
        for i, emotion in enumerate(lineEmotions.keys(), start=1):
            xAxis.append(emotion, i)

        xAxis.setRange(0, len(lineEmotions))
        xAxis.setTickCount(len(lineEmotions) + 1)
        xAxis.setTitleText("Emotions")
        xAxis.setGridLineVisible(False)

        chart = QChart()
        chart.setAnimationOptions(QChart.GridAxisAnimations)
        chart.addSeries(series)

        chart.addAxis(yAxis, Qt.AlignLeft)
        chart.addAxis(xAxis, Qt.AlignBottom)
        series.attachAxis(yAxis)
        series.attachAxis(xAxis)

        chart.setTitleFont(self.font)
        chart.setTitle("Largest Confidence Level Per Emotion")

        chart.legend().setVisible(False)
        self.lineChart.setChart(chart)

    def closeEvent(self, event):
        # Shuts down application on close.
        # Return stdout to defaults.
        sys.stdout = sys.__stdout__
        super().closeEvent(event)
