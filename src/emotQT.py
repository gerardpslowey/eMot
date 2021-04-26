import sys

from PyQt5 import QtCore, QtGui, QtWidgets
from pyqt import main_window, windows, metrics  # reportsInfo
from qtWorker import Worker

from eMot import Emot
from emotClassify import EmotClassify
from tests import dockerRunner
from wordcloud import WordCloud


class Main(QtWidgets.QMainWindow, main_window.Ui_MainWindow):
    def __init__(self, *args, obj=None, **kwargs):
        super(Main, self).__init__(*args, **kwargs)
        self.setupUi(self)
        self.stackedWidget.setCurrentWidget(self.homePage)

        self.threadpool = QtCore.QThreadPool()

        # Set all the UI windows
        self.AboutWindow = windows.About()
        self.DialogWindow = windows.Dialog()
        self.PreferenceWindow = windows.Preference()

        # file menu
        self.actionAbout.triggered.connect(
            lambda checked: self.toggleItem(self.AboutWindow))

        self.actionPreferences.triggered.connect(
            lambda checked: self.toggleItem(self.PreferenceWindow))
        self.actionNew.triggered.connect(self.restartWindow)

        self.button.clicked.connect(self.goButton)
        self.results_button.setEnabled(False)
        self.results_button.clicked.connect(self.showMetrics)

    def toggleItem(self, item):
        if item.isVisible():
            item.hide()
        else:
            item.show()

    def goButton(self):
        self.browser = str(self.browserComboBox.currentText()).capitalize()
        self.filtr = str(self.dateComboBox.currentText()).capitalize()

        if self.browser == "Select browser":
            self.toggleItem(self.DialogWindow)
            self.DialogWindow.label.setText("Choose a browser from \nthe dropdown menu")
            self.DialogWindow.label_2.setText("You Must Choose A Browser")

        elif not dockerRunner.is_running("splash"):
            self.toggleItem(self.DialogWindow)
            self.DialogWindow.label.setText("The splash container \nmust be turned on")
            self.DialogWindow.label_2.setText("Docker Container")

        else:
            self.setupPrintPage()
            self.MetricsDashboard = metrics.MetricsDashboard(self.browser, self.filtr)

    def setupPrintPage(self):
        self.stackedWidget.setCurrentWidget(self.printPage)
        sys.stdout = windows.Stream(newText=self.redirectText)

        emot = Emot(self.filtr, self.browser)
        worker = Worker(emot.startTasks)
        self.threadpool.start(worker)

        worker.signals.result.connect(lambda result: self.startClassify(result))

    def startClassify(self, result):
        if result:
            self.emotClassify = EmotClassify()
            worker = Worker(self.emotClassify.startAll)
            self.threadpool.start(worker)
            worker.signals.finished.connect(self.enableResultsButton)
        else:
            self.results_button.setEnabled(True)
            self.results_button.setText("Start again?")
            self.results_button.clicked.connect(self.restartWindow)

    def enableResultsButton(self):
        print("\nClick the 'Show Results' button to view the results!")
        self.startDrawing()
        self.MetricsDashboard.makeCharts(self.emotClassify)
        sites = f"{len(self.emotClassify.getSiteVisitCounts())} Sites"
        self.MetricsDashboard.sitesVisitedEdit.setText(sites)
        self.results_button.setEnabled(True)
        self.results_button.setText("Show Results!")
        self.results_button.setStyleSheet(
            "color: rgb(255, 255, 255);\n"
            "background-color: rgb(103, 171, 159);\n"
            "border: 1px solid black;\n"
            "border-radius: 10px;"
        )

    def showMetrics(self):
        self.MetricsDashboard.show()

    def startDrawing(self):
        worker = Worker(self.createWordCloud)
        self.threadpool.start(worker)

    def createWordCloud(self):
        data = self.emotClassify.getWordCloudBag()
        words = ' '.join(data)
        wordcloud = WordCloud(
            background_color="white",
            width=2500, height=2000).generate(words)

        wordCloudImage = "pyqt/wordCloud.png"
        wordcloud.to_file(wordCloudImage)
        self.MetricsDashboard.showImage(wordCloudImage)

    def redirectText(self, text):
        # Write console output to textEdit widget.
        cursor = self.textEdit.textCursor()
        cursor.movePosition(QtGui.QTextCursor.End)
        cursor.insertText(text)
        self.textEdit.setTextCursor(cursor)
        self.textEdit.ensureCursorVisible()

    def restartWindow(self):
        sys.stdout = sys.__stdout__
        QtCore.QCoreApplication.quit()
        QtCore.QProcess.startDetached(sys.executable, sys.argv)
        # print(status)

    def closeEvent(self, event):
        """Shuts down application on close."""
        # Return stdout to defaults.
        sys.stdout = sys.__stdout__
        dockerRunner.stop("splash")
        super().closeEvent(event)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    main = Main()
    main.show()
    app.exec_()
