from pyqt.about_window import Ui_Form
from pyqt.browser_dialog import Ui_browserDialog
from pyqt.preferences_window import Ui_Form as PrefWindow
from pyqt.metrics import Ui_MetricsDashboard
from utils.blacklists import Blacklists
from PyQt5 import QtCore
from PyQt5.QtCore import Qt, QObject
from PyQt5.QtGui import QPen  # QPainter,
from PyQt5.QtWidgets import QMessageBox, QMainWindow
from PyQt5.QtChart import QChart, QLineSeries, QValueAxis, QCategoryAxis
from PyQt5.QtChart import QBarSet, QPercentBarSeries, QBarCategoryAxis
from PyQt5.QtChart import QPieSeries


class About(QMainWindow, Ui_Form):
    def __init__(self, *args, obj=None, **kwargs):
        super(About, self).__init__(*args, **kwargs)
        self.setupUi(self)


class Dialog(QMainWindow, Ui_browserDialog):
    def __init__(self, *args, obj=None, **kwargs):
        super(Dialog, self).__init__(*args, **kwargs)
        self.setupUi(self)


class MetricsDashboard(QMainWindow, Ui_MetricsDashboard):
    def __init__(self, *args, obj=None, **kwargs):
        super(MetricsDashboard, self).__init__(*args, **kwargs)
        self.setupUi(self)
        self.setWindowTitle("Metrics Dashboard")

        self.stackedWidget.setCurrentWidget(self.chartPage)
        self.nextPageButton.clicked.connect(self.changePage)
        self.previousPageButton.clicked.connect(self.changePage)

    def changePage(self):
        if self.stackedWidget.currentWidget() == self.chartPage:
            self.stackedWidget.setCurrentWidget(self.wordCloudPage)
        else:
            self.stackedWidget.setCurrentWidget(self.chartPage)

    def makeCharts(self, emotClassify):

        lineStats = emotClassify.get_emotion_intensity()
        pieStats = emotClassify.get_emotion_count()
        self.makeBarChart()
        self.makePieChart(pieStats)
        self.makeLineChart(lineStats)
        self.makeSplitChart()

    def makeBarChart(self):

        set0 = QBarSet("One") # noqa
        set1 = QBarSet("Two") # noqa
        set2 = QBarSet("Three") # noqa
        set3 = QBarSet("Four") # noqa
        set4 = QBarSet("Five") # noqa

        data = {
            0: [1, 2, 3, 4, 5, 6],
            1: [5, 0, 0, 4, 0, 7],
            2: [3, 5, 8, 4, 13, 4],
            3: [5, 1, 5, 9, 11, 2],
            4: [11, 3, 7, 4, 3, 6]
        }

        series = QPercentBarSeries()
        for key, value in data.items():
            barSet = eval(f"set{key}")
            barSet.append(data[key])
            series.append(barSet)

        chart = QChart()
        chart.addSeries(series)
        chart.setTitle('Bar Chart')
        chart.setAnimationOptions(QChart.SeriesAnimations)

        categories = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]
        axis = QBarCategoryAxis()
        axis.append(categories)

        chart.createDefaultAxes()
        chart.setAxisX(axis, series)

        self.barChart.setChart(chart)

    def makePieChart(self, pieStats):
        # get the data
        emotions = dict(sorted(pieStats.items(), key=lambda item: item[1], reverse=True))

        series = QPieSeries()
        for emotion in emotions:
            series.append(emotion, pieStats[emotion])

        # largest emotion
        pieSlice = series.slices()[0]
        pieSlice.setExploded(True)
        pieSlice.setLabelVisible(True)
        pieSlice.setPen(QPen(QtCore.Qt.lightGray, 2))
        pieSlice.setBrush(QtCore.Qt.lightGray)

        chart = QChart()
        chart.addSeries(series)
        chart.setTitle('Overall Emotion Counts')
        chart.createDefaultAxes()
        chart.setAnimationOptions(QChart.SeriesAnimations)
        self.pieChart.setChart(chart)

    def makeLineChart(self, lineStats):
        series = QLineSeries()
        series.setPointLabelsVisible(True)
        series.setPointLabelsColor(Qt.black)
        series.setPointLabelsFormat("@yPoint" + "%")

        for i, (key, value) in enumerate(lineStats.items()):
            i += 0.5
            series.append(i, lineStats[key])

        yAxis = QValueAxis()
        yAxis.setRange(0, 1)
        yAxis.setLabelFormat("%.1f")
        yAxis.setTickCount(5)
        yAxis.setTitleText("Intensity (%)")
        yAxis.setGridLineVisible(False)

        xAxis = QCategoryAxis()
        for i, emotion in enumerate(lineStats.keys(), start=1):
            xAxis.append(emotion, i)

        xAxis.setRange(0, len(lineStats))
        xAxis.setTickCount(len(lineStats) + 1)
        xAxis.setTitleText("Emotions")
        xAxis.setGridLineVisible(False)

        chart = QChart()
        chart.addSeries(series)

        chart.addAxis(yAxis, Qt.AlignLeft)
        chart.addAxis(xAxis, Qt.AlignBottom)
        series.attachAxis(yAxis)
        series.attachAxis(xAxis)

        # chart.setAnimationOptions(QChart.SeriesAnimations)
        chart.setTitle("Emotion Intensity Line Chart")

        chart.legend().setVisible(False)
        self.lineChart.setChart(chart)

    def makeSplitChart(self):
        chart = QChart()
        series = QLineSeries()

        series.append(1, 3)
        series.append(2, 4)

        chart.addSeries(series)
        chart.setTitle('Example')
        chart.createDefaultAxes()
        self.barChart_4.setChart(chart)


class Preference(QMainWindow, PrefWindow):
    def __init__(self, *args, obj=None, **kwargs):
        super(Preference, self).__init__(*args, **kwargs)
        self.setupUi(self)
        self.blacklists = Blacklists()
        self.addTagButton.clicked.connect(self.addTag)
        self.deleteTagButton.clicked.connect(self.removeTag)
        self.addUrlButton.clicked.connect(self.addUrl)
        self.deleteUrlButton.clicked.connect(self.removeURL)

    def addTag(self):
        tag = self.tagEdit.toPlainText()
        self.blacklists.addItem(tag, "tagSet")
        self.showPopUp("Tag added!")
        self.tagEdit.clear()

    def removeTag(self):
        tag = self.tagEdit.toPlainText()
        self.blacklists.removeItem(tag, "tagSet")
        self.showPopUp("Tag removed!")
        self.tagEdit.clear()

    def addUrl(self):
        url = self.urlEdit.toPlainText()
        self.blacklists.addItem(url, "urlSet")
        self.showPopUp("URL added!")
        self.urlEdit.clear()

    def removeURL(self):
        url = self.PreferenceWindow.urlEdit.toPlainText()
        self.blacklists.removeItem(url, "urlSet")
        self.showPopUp("URL removed!")
        self.PreferenceWindow.urlEdit.clear()

    def showPopUp(self, message):
        msg = QMessageBox()
        msg.setWindowTitle("Message")
        msg.setText(message)
        msg.setIcon(QMessageBox.Information)
        msg.setStandardButtons(QMessageBox.Ok)
        msg.exec_()


class Stream(QObject):
    """Redirects console output to text widget."""
    newText = QtCore.pyqtSignal(str)

    def write(self, text):
        self.newText.emit(str(text))
