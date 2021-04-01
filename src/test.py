from PyQt5.QtCore import QThreadPool, Qt
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtChart import QChart, QChartView, QPieSeries, QPieSlice
from PyQt5.QtGui import QPainter, QPen

from emotClassify import EmotClassify
from qtWorker import Worker
import sys


class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("PyQtChart Pie Chart")
        self.setGeometry(100,100, 1280,600)
        self.show()
        self.emotClassify = EmotClassify()

        self.threadpool = QThreadPool()
        worker = Worker(self.emotClassify.classify) 
        self.threadpool.start(worker)
        worker.signals.finished.connect(self.create_piechart)

    def create_piechart(self):
        
        emotions = self.emotClassify.get_emotion_count()
        emot = dict(sorted(emotions.items(), key=lambda item: item[1], reverse= True))

        series = QPieSeries()
        for e in emot:
            series.append(e, emotions[e])

        #adding slice
        slice = QPieSlice()
        slice = series.slices()[0]
        slice.setExploded(True)
        slice.setLabelVisible(True)
        slice.setPen(QPen(Qt.darkGreen, 2))
        slice.setBrush(Qt.green)


        chart = QChart()
        chart.legend().hide()
        chart.addSeries(series)
        chart.createDefaultAxes()
        chart.setAnimationOptions(QChart.SeriesAnimations)
        chart.setTitle("Emotions")

        chart.legend().setVisible(True)
        chart.legend().setAlignment(Qt.AlignBottom)

        chartview = QChartView(chart)
        chartview.setRenderHint(QPainter.Antialiasing)

        self.setCentralWidget(chartview)





App = QApplication(sys.argv)
window = Window()
sys.exit(App.exec_())