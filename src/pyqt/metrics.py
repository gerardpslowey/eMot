from pyqt.metrics_window import Ui_MetricsDashboard
from PyQt5.QtChart import QChart, QLineSeries, QValueAxis, QCategoryAxis
from PyQt5.QtChart import QBarSet, QPercentBarSeries, QBarCategoryAxis
from PyQt5.QtChart import QPieSeries, QBarSeries
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPen, QColor, QPixmap, QPainter
from PyQt5.QtWidgets import QMainWindow
from PyQt5 import QtCore
import sys
import funcy

colours = [
    QColor("#ED5314"), QColor("#FFB92A"), QColor("#FEEB51"),
    QColor("#9BCA3E"), QColor("#3ABBC9"), QColor("#666DCB"),
    QColor("#c0c0c0")
]


class MetricsDashboard(QMainWindow, Ui_MetricsDashboard):

    def __init__(self, browser, filtr, *args, obj=None, **kwargs):
        super(MetricsDashboard, self).__init__(*args, **kwargs)
        self.setupUi(self)
        self.setWindowTitle("Metrics Dashboard")
        self.browserUsedEdit.setText(browser)
        self.dateUsedEdit.setText(filtr)

        self.stackedWidget.setCurrentWidget(self.chartPage)
        self.nextPageButton.clicked.connect(self.changePage)
        self.previousPageButton.clicked.connect(self.changePage)

    def showImage(self, image, prefix):
        self.image = QPixmap(image)
        if prefix == "neg":
            self.image.scaled(self.negativeWordcloud.size(), Qt.KeepAspectRatio)
            self.negativeWordcloud.setPixmap(self.image)
            self.negativeWordcloud.setScaledContents(True)
        else:
            self.image.scaled(self.positiveWordcloud.size(), Qt.KeepAspectRatio)
            self.positiveWordcloud.setPixmap(self.image)
            self.positiveWordcloud.setScaledContents(True)

    def changePage(self):
        if self.stackedWidget.currentWidget() == self.chartPage:
            self.stackedWidget.setCurrentWidget(self.wordCloudPage)
        else:
            self.stackedWidget.setCurrentWidget(self.chartPage)

    def makeCharts(self, emotClassify):
        self.emotions = emotClassify.getEmotions()
        # split chart data
        self.splitChartValues = emotClassify.getSplitChartValues()
        self.emotionsPerSite = emotClassify.getEmotionsPerSite()
        self.uniqueSiteCount = emotClassify.getUniqueSiteCount()
        # line chart data
        self.emotionIntensities = emotClassify.getEmotionIntensities()
        # pie chart data
        self.emotionCounts = emotClassify.getEmotionCounts()
        # bar chart data
        self.siteVisitCounts = emotClassify.getSiteVisitCounts()

        numEmotions = len(self.emotions)
        self.keys = ['neutral']
        self.makePieChart()
        self.makeLineChart()
        self.makeSplitChart(numEmotions)
        self.makeBarChart(numEmotions)

    def makeBarChart(self, numEmotions):
        barSets = [QBarSet(site) for site in self.siteVisitCounts.keys()]
        series = QBarSeries()

        for i, value in enumerate(self.siteVisitCounts.values()):
            barSets[i].append(value)
            # add number of visits to set
            series.append(barSets[i])
            barSets[i].setColor(colours[i % numEmotions])

        chart = QChart()
        chart.addSeries(series)
        chart.setTitle('Most Visited Sites')

        yAxis = QValueAxis()
        try:
            largestSiteVisitCount = max(self.siteVisitCounts.values())
        except ValueError:
            largestSiteVisitCount = 0

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

    def makeSplitChart(self, numEmotions):
        # create a new QBarSet for each emotion
        barSets = [QBarSet(emotion) for emotion in self.emotions]
        series = QPercentBarSeries()

        # for each website
        for i in range(self.uniqueSiteCount):
            # iterate through the array of emotions associated with that site
            barStatArray = self.splitChartValues[i]
            for j in range(len(barStatArray)):
                # add that emotion to the barset
                barSets[j].append(barStatArray[j])

        # append the completed barSet to the series
        for i in range(len(barSets)):
            series.append(barSets[i])
            # set the custom colours
            barSets[i].setColor(colours[i % numEmotions])

        chart = QChart()
        chart.addSeries(series)
        chart.setTitle('Emotions Seen Per Site')
        chart.setAnimationOptions(QChart.SeriesAnimations)

        # categories are the website names
        categories = list(self.emotionsPerSite.keys())
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

    def makePieChart(self):
        pieEmotions = funcy.omit(self.emotionCounts, 'neutral')
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
        pieSlice.setPen(QPen(QtCore.Qt.darkGray, 2))        # the border colour

        chart = QChart()
        chart.addSeries(series)
        chart.setTitle('Overall Emotion Counts Of Sentences')
        chart.createDefaultAxes()

        chart.legend().setVisible(True)
        chart.legend().setAlignment(Qt.AlignBottom)
        chart.setAnimationOptions(QChart.SeriesAnimations)
        self.pieChart.setChart(chart)
        self.pieChart.setRenderHint(QPainter.Antialiasing)

    def makeLineChart(self):
        series = QLineSeries()
        series.setPointLabelsVisible(True)
        series.setPointLabelsColor(Qt.black)
        series.setPointLabelsFormat("@yPoint" + "%")

        lineEmotions = funcy.omit(self.emotionIntensities, 'neutral')

        for i, (key, value) in enumerate(lineEmotions.items()):
            i += 0.5
            series.append(i, lineEmotions[key])

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

        chart.setTitle("Largest Confidence Level Per Emotion")

        chart.legend().setVisible(False)
        self.lineChart.setChart(chart)

    def closeEvent(self, event):
        """Shuts down application on close."""
        # Return stdout to defaults.
        sys.stdout = sys.__stdout__
        super().closeEvent(event)
