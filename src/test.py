import sys

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import QtChart
from pyqt import main_window, windows, reportCharts

from emotClassify import EmotClassify

class Main(QtWidgets.QMainWindow, main_window.Ui_MainWindow):

    def __init__(self, *args, obj=None, **kwargs):
        super(Main, self).__init__(*args, **kwargs)
        self.setupUi(self)
        self.stackedWidget.setCurrentWidget(self.printPage)

        self.threadpool = QtCore.QThreadPool()
        self.emotClassify = EmotClassify()
        self.emotClassify.classify()
        self.results_button.clicked.connect(self.showPieChart)

    def showPieChart(self):

        self.stackedWidget.setCurrentWidget(self.reportsPage)

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

        self.showLineChart()

    def showLineChart(self):
        series = QtChart.QLineSeries(self)

        emotionsDict = self.emotClassify.get_emotion_intensity()
        emotions = dict(sorted(emotionsDict.items(), key=lambda item: item[1], reverse= True))

        i = 1
        for emotion in emotions:
            series.append(i, emotionsDict[emotion])
            i+=1

        series << QtCore.QPointF(11, 1) << QtCore.QPointF(13, 3) << QtCore.QPointF(17, 6) << QtCore.QPointF(18, 3) << QtCore.QPointF(20, 2)
        chart = QtChart.QChart()

        chart.addSeries(series)
        chart.createDefaultAxes()
        chart.setAnimationOptions(QtChart.QChart.SeriesAnimations)
        chart.setTitle("Line Chart")

        chart.legend().setVisible(True)
        chart.legend().setAlignment(QtCore.Qt.AlignBottom)

        chartview = QtChart.QChartView(chart)
        chartview.setRenderHint(QtGui.QPainter.Antialiasing)
        self.layout.addWidget(chartview)


    def closeEvent(self, event):
        """Shuts down application on close."""
        # Return stdout to defaults.
        sys.stdout = sys.__stdout__
        super().closeEvent(event)

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    main = Main()
    main.show()
    app.exec_()