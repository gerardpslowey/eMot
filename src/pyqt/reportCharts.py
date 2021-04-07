from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtChart import QChart, QChartView, QPieSeries, QPieSlice
import pyqtgraph as pg

class PieChart(QtWidgets.QWidget):
    def __init__(self, emotionsDict, parent): 
        super(PieChart, self).__init__(parent)
        emotions = dict(sorted(emotionsDict.items(), key=lambda item: item[1], reverse= True))

        series = QPieSeries()
        for emotion in emotions:
            series.append(emotion, emotionsDict[emotion])

        #adding slice
        #slice = QPieSlice()
        slice = series.slices()[0]
        slice.setExploded(True)
        slice.setLabelVisible(True)
        slice.setPen(QtGui.QPen(QtCore.Qt.darkGreen, 2))
        slice.setBrush(QtCore.Qt.green)

        chart = QChart()
        chart.legend().hide()
        chart.addSeries(series)
        chart.createDefaultAxes()
        chart.setAnimationOptions(QChart.SeriesAnimations)
        chart.setTitle("Emotions")

        chart.legend().setVisible(True)
        chart.legend().setAlignment(QtCore.Qt.AlignBottom)

        chartview = QChartView(chart)
        chartview.setRenderHint(QtGui.QPainter.Antialiasing)