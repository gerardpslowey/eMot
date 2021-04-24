from pyqt.metrics_window import Ui_MetricsDashboard
from PyQt5.QtChart import QChart, QLineSeries, QValueAxis, QCategoryAxis
from PyQt5.QtChart import QBarSet, QPercentBarSeries, QBarCategoryAxis
from PyQt5.QtChart import QPieSeries, QBarSeries
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPen, QColor, QPixmap
from PyQt5.QtWidgets import QMainWindow
from PyQt5 import QtCore

colours = [QColor("#83677B"), QColor("#379683"), QColor("salmon"),
           QColor("#7395AE"), QColor("#D79922"), QColor("#99738E")]


class MetricsDashboard(QMainWindow, Ui_MetricsDashboard):

    def __init__(self, *args, obj=None, **kwargs):
        super(MetricsDashboard, self).__init__(*args, **kwargs)
        self.setupUi(self)
        self.setWindowTitle("Metrics Dashboard")

        self.stackedWidget.setCurrentWidget(self.chartPage)
        self.nextPageButton.clicked.connect(self.changePage)
        self.previousPageButton.clicked.connect(self.changePage)

    def showImage(self, image):
        self.image = QPixmap(image)
        self.image.scaled(self.wordCloud.size(), Qt.KeepAspectRatio)
        self.wordCloud.setPixmap(self.image)
        self.wordCloud.setScaledContents(True)

    def changePage(self):
        if self.stackedWidget.currentWidget() == self.chartPage:
            self.stackedWidget.setCurrentWidget(self.wordCloudPage)
        else:
            self.stackedWidget.setCurrentWidget(self.chartPage)

    def makeCharts(self, emotClassify):
        self.emotions = emotClassify.get_emotions()
        self.splitBarStats = emotClassify.get_split_chart_values()
        self.visitedUniqueSites = emotClassify.get_total_sites()
        self.lineStats = emotClassify.get_emotion_intensity()
        self.pieStats = emotClassify.get_emotion_count()
        self.siteVisitStats = emotClassify.get_site_count()

        self.makePieChart()
        self.makeLineChart()
        self.makeSplitChart()
        self.makeBarChart()

    def makeBarChart(self):
        barSets = [QBarSet(site) for site in self.siteVisitStats.keys()]

        series = QBarSeries()

        for i, value in enumerate(self.siteVisitStats.values()):
            barSets[i].append(value)       # add number of visits to set
            series.append(barSets[i])
            barSets[i].setColor(colours[i % 6])

        chart = QChart()

        chart.addSeries(series)
        chart.setTitle('Site Visit Counts Chart')
        # chart.createDefaultAxes()

        yAxis = QValueAxis()
        # yAxis.setRange(0, len(self.siteVisitStats))
        yAxis.setLabelFormat("%.1f")
        # yAxis.setTickCount(len(self.siteVisitStats))
        yAxis.setTitleText("No. Sites")
        yAxis.setGridLineVisible(True)

        chart.setAnimationOptions(QChart.SeriesAnimations)
        chart.legend().setVisible(True)
        chart.legend().setAlignment(Qt.AlignBottom)
        chart.addAxis(yAxis, Qt.AlignLeft)
        series.attachAxis(yAxis)

        self.barChart.setChart(chart)

    def makeSplitChart(self):
        # create a new QBarSet for each emotion in emotions
        barSets = [QBarSet(emotion) for emotion in self.emotions]  # 6 emotions
        series = QPercentBarSeries()

        # for each website
        for i in range(self.visitedUniqueSites):
            # iterate through the array of emotions associated with that site
            barStatArray = self.splitBarStats[i]
            for j in range(len(barStatArray)):
                # add that emotion to the barset
                barSets[j].append(barStatArray[j])

        # append the completed barSet to the series
        for i in range(len(barSets)):
            series.append(barSets[i])
            barSets[i].setColor(colours[i])

        chart = QChart()
        chart.addSeries(series)
        chart.setTitle('Split Chart of Emotions per Site')
        chart.setAnimationOptions(QChart.SeriesAnimations)

        # categories are the website names
        categories = list(self.siteVisitStats.keys())
        axisX = QBarCategoryAxis()
        axisX.append(categories)

        axisY = QValueAxis()
        axisY.setTickCount(11)
        axisY.setRange(0, 100)
        axisY.setTitleText("% Emotion Per Site")

        chart.createDefaultAxes()
        chart.setAxisX(axisX, series)
        chart.setAxisY(axisY)

        chart.legend().setVisible(True)
        chart.legend().setAlignment(Qt.AlignBottom)

        self.splitChart.setChart(chart)

    def makePieChart(self):
        # get the data
        emotions = dict(sorted(self.pieStats.items(), key=lambda item: item[1], reverse=True))

        series = QPieSeries()
        for i, (emotion, value) in enumerate(emotions.items()):
            slices = series.append(emotion, value)
            slices.setBrush(colours[i])

        # largest emotion
        pieSlice = series.slices()[0]
        pieSlice.setExploded(True)
        pieSlice.setLabelVisible(True)
        pieSlice.setPen(QPen(QtCore.Qt.lightGray, 2))
        pieSlice.setBrush(QtCore.Qt.lightGray)

        chart = QChart()
        chart.addSeries(series)
        chart.setTitle('Overall Emotion Counts Of Sentences')
        chart.createDefaultAxes()
        chart.setAnimationOptions(QChart.SeriesAnimations)
        self.pieChart.setChart(chart)

    def makeLineChart(self):
        series = QLineSeries()
        series.setPointLabelsVisible(True)
        series.setPointLabelsColor(Qt.black)
        series.setPointLabelsFormat("@yPoint" + "%")

        for i, (key, value) in enumerate(self.lineStats.items()):
            i += 0.5
            series.append(i, self.lineStats[key])

        yAxis = QValueAxis()
        yAxis.setRange(0, 1)
        yAxis.setLabelFormat("%.1f")
        yAxis.setTickCount(5)
        yAxis.setTitleText("Intensity (%)")
        yAxis.setGridLineVisible(False)

        xAxis = QCategoryAxis()
        for i, emotion in enumerate(self.lineStats.keys(), start=1):
            xAxis.append(emotion, i)

        xAxis.setRange(0, len(self.lineStats))
        xAxis.setTickCount(len(self.lineStats) + 1)
        xAxis.setTitleText("Emotions")
        xAxis.setGridLineVisible(False)

        chart = QChart()
        chart.setAnimationOptions(QChart.GridAxisAnimations)
        chart.addSeries(series)

        chart.addAxis(yAxis, Qt.AlignLeft)
        chart.addAxis(xAxis, Qt.AlignBottom)
        series.attachAxis(yAxis)
        series.attachAxis(xAxis)

        # chart.setAnimationOptions(QChart.SeriesAnimations)
        chart.setTitle("Emotion Intensity Line Chart")

        chart.legend().setVisible(False)
        self.lineChart.setChart(chart)
