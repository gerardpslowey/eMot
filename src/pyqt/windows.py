from PyQt5 import QtCore, QtWidgets
from pyqt.about_window import Ui_Form
from pyqt.browser_dialog import Ui_browserDialog
from pyqt.preferences_window import Ui_Form as PrefWindow
from pyqt.metrics import Ui_MetricsDashboard
from utils.blacklists import Blacklists
from PyQt5.QtChart import QChart, QLineSeries


class About(QtWidgets.QMainWindow, Ui_Form):
    def __init__(self, *args, obj=None, **kwargs):
        super(About, self).__init__(*args, **kwargs)
        self.setupUi(self)


class Dialog(QtWidgets.QMainWindow, Ui_browserDialog):
    def __init__(self, *args, obj=None, **kwargs):
        super(Dialog, self).__init__(*args, **kwargs)
        self.setupUi(self)


class MetricsDashboard(QtWidgets.QMainWindow, Ui_MetricsDashboard):
    def __init__(self, *args, obj=None, **kwargs):
        super(MetricsDashboard, self).__init__(*args, **kwargs)
        self.setupUi(self)
        self.setWindowTitle("Metrics Dashboard")
        self.makeBarChart()
        self.makePieChart()
        self.makeLineChart()
        self.makeChart()
        self.stackedWidget.setCurrentWidget(self.chartPage)
        self.nextPageButton.clicked.connect(self.changePage)
        self.previousPageButton.clicked.connect(self.changePage)

    def changePage(self):
        if self.stackedWidget.currentWidget() == self.chartPage:
            self.stackedWidget.setCurrentWidget(self.wordCloudPage)
        else:
            self.stackedWidget.setCurrentWidget(self.chartPage)

    def makeBarChart(self):
        chart = QChart()
        series = QLineSeries()

        series.append(1, 3)
        series.append(2, 4)

        chart.addSeries(series)
        chart.setTitle('Bar Chart')
        chart.createDefaultAxes()
        self.barChart.setChart(chart)

    def makePieChart(self):
        chart = QChart()
        series = QLineSeries()

        series.append(1, 3)
        series.append(2, 4)

        chart.addSeries(series)
        chart.setTitle('Pie Chart')
        chart.createDefaultAxes()
        self.pieChart.setChart(chart)

    def makeLineChart(self):
        chart = QChart()
        series = QLineSeries()

        series.append(1, 3)
        series.append(2, 4)

        chart.addSeries(series)
        chart.setTitle('Line Chart')
        chart.createDefaultAxes()
        self.lineChart.setChart(chart)

    def makeChart(self):
        chart = QChart()
        series = QLineSeries()

        series.append(1, 3)
        series.append(2, 4)

        chart.addSeries(series)
        chart.setTitle('Example')
        chart.createDefaultAxes()
        self.barChart_4.setChart(chart)


class Preference(QtWidgets.QMainWindow, PrefWindow):
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
        msg = QtWidgets.QMessageBox()
        msg.setWindowTitle("Message")
        msg.setText(message)
        msg.setIcon(QtWidgets.QMessageBox.Information)
        msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
        msg.exec_()


class Stream(QtCore.QObject):
    """Redirects console output to text widget."""
    newText = QtCore.pyqtSignal(str)

    def write(self, text):
        self.newText.emit(str(text))
