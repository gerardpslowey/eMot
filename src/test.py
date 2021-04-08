import sys

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import QtChart
from pyqt import main_window, windows, reportsInfo
import pyqtgraph as pg

from emotClassify import EmotClassify

class Main(QtWidgets.QMainWindow, main_window.Ui_MainWindow):

    def __init__(self, *args, obj=None, **kwargs):
        super(Main, self).__init__(*args, **kwargs)
        self.setupUi(self)
        self.stackedWidget.setCurrentWidget(self.printPage)

        self.threadpool = QtCore.QThreadPool()
        self.emotClassify = EmotClassify()
        self.emotClassify.classify()
        self.results_button.clicked.connect(self.setStatistics)

        self.nextPageButton.clicked.connect(self.changePage)
        self.previousPageButton.clicked.connect(self.changePage)

        self.browser = "Opera"
        self.filtr = "All"

    def changePage(self):
        if self.stackedWidget.currentWidget() == self.reportsPage:
            self.stackedWidget.setCurrentWidget(self.reportsPage2)
        else:
            self.stackedWidget.setCurrentWidget(self.reportsPage)

    def setStatistics(self):
        self.stackedWidget.setCurrentWidget(self.reportsPage)
        reportsInfo.setStats(self)
        axes = self.wordCloud.figure.add_subplot(1,1,1)
        axes.plot([1,2,3],[4,5,6])

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