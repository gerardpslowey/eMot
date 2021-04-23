from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPainter
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtChart import QChartView, QChart, QLineSeries, QValueAxis, QCategoryAxis

from sys import exit as sysExit  # I rename this for numerous reason but you do not have to


class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.resize(640, 480)

        series = QLineSeries()
        series.setPointLabelsVisible(True)
        series.setPointLabelsColor(Qt.black)
        series.setPointLabelsFormat("@yPoint" + "%")

        data = {
            "anger": 0.78,
            "fear": 0.67,
            "joy": 0.54,
            "surprise": 0.64,
            "happiness": 0.82,
            "sadness": 0.78
        }

        for i, (key, value) in enumerate(data.items()):
            i += 0.5
            series.append(i, data[key])

        yAxis = QValueAxis()
        yAxis.setRange(0, 1)
        yAxis.setLabelFormat("%.1f")
        yAxis.setTickCount(5)
        yAxis.setTitleText("Intensity (%)")
        yAxis.setGridLineVisible(False)

        xAxis = QCategoryAxis()
        for i, emotion in enumerate(data.keys(), start=1):
            xAxis.append(emotion, i)

        xAxis.setRange(0, len(data))
        xAxis.setTickCount(len(data) + 1)
        xAxis.setTitleText("Emotions")
        xAxis.setGridLineVisible(False)

        chart = QChart()
        chart.addSeries(series)
        chart.addAxis(yAxis, Qt.AlignLeft)
        chart.addAxis(xAxis, Qt.AlignBottom)
        series.attachAxis(yAxis)
        series.attachAxis(xAxis)

        chart.setAnimationOptions(QChart.SeriesAnimations)
        chart.setTitle("Emotion Intensity Line Chart")

        chart.legend().setVisible(False)

        self.chartView = QChartView(chart)

        self.setCentralWidget(self.chartView)


if __name__ == "__main__":
    MainEventHandler = QApplication([])

    MainApp = MainWindow()
    MainApp.show()

    sysExit(MainEventHandler.exec_())
