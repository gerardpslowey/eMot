import sys
# import threading

from PyQt5 import QtCore, QtGui, QtWidgets
from pyqt import main_window, windows  # reportsInfo
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
        self.emotClassify = EmotClassify()

        # Set all the UI windows
        self.AboutWindow = windows.About()
        self.DialogWindow = windows.Dialog()
        self.PreferenceWindow = windows.Preference()
        self.MetricsDashboard = windows.MetricsDashboard()

        # file menu
        self.actionAbout.triggered.connect(
            lambda checked: self.toggle_item(self.AboutWindow))

        self.actionPreferences.triggered.connect(
            lambda checked: self.toggle_item(self.PreferenceWindow))
        self.actionNew.triggered.connect(self.restart_window)

        self.button.clicked.connect(self.go_button)
        self.results_button.setEnabled(False)
        self.results_button.clicked.connect(self.createMetrics)

    def restart_window(self):
        QtCore.QCoreApplication.quit()
        status = QtCore.QProcess.startDetached(sys.executable, sys.argv)
        print(status)

    def toggle_item(self, item):
        if item.isVisible():
            item.hide()
        else:
            item.show()

    def go_button(self):
        self.browser = str(self.browserComboBox.currentText()).capitalize()
        self.filtr = str(self.dateComboBox.currentText()).capitalize()

        if self.browser == "Select browser":
            self.toggle_item(self.DialogWindow)
            self.DialogWindow.label.setText("Choose a browser from \nthe dropdown menu")
            self.DialogWindow.label_2.setText("You Must Choose A Browser")

        elif not dockerRunner.is_running("splash"):
            self.toggle_item(self.DialogWindow)
            self.DialogWindow.label.setText("The splash docker \nmust to be turned on")
            self.DialogWindow.label_2.setText("Docker Container")

        else:
            self.setupPrintPage()
            self.browserUsedEdit.setPlainText(self.browser)
            self.dateUsedEdit.setPlainText(self.filtr)

    def setupPrintPage(self):
        self.stackedWidget.setCurrentWidget(self.printPage)
        sys.stdout = windows.Stream(newText=self.onUpdateText)

        emot = Emot(self.filtr, self.browser)
        worker = Worker(emot.startTasks)
        self.threadpool.start(worker)
        worker.signals.finished.connect(self.startClassify)

    def onUpdateText(self, text):
        # Write console output to textEdit widget.
        cursor = self.textEdit.textCursor()
        cursor.movePosition(QtGui.QTextCursor.End)
        cursor.insertText(text)
        self.textEdit.setTextCursor(cursor)
        self.textEdit.ensureCursorVisible()

    def startClassify(self):
        # self.textEdit.clear()
        print("Starting Classification..\n")
        worker = Worker(self.emotClassify.startAll)
        self.threadpool.start(worker)
        worker.signals.finished.connect(self.enableResultsButton)

    def enableResultsButton(self):
        print("Click to find out more!")
        self.numSitesEdit.setPlainText(self.emotClassify.get_total_site_visit())
        self.startDrawing()
        self.results_button.setEnabled(True)
        self.results_button.setText("Show Results!")
        self.results_button.setStyleSheet(
            "color: rgb(255, 255, 255);\n"
            "background-color: rgb(103, 171, 159);\n"
            "border: 1px solid black;")

    def createMetrics(self):
        self.stackedWidget.setCurrentWidget(self.reportsPage)
        self.MetricsDashboard.show()

    def startDrawing(self):
        worker = Worker(self.draw_WordCloud)
        self.threadpool.start(worker)

    def draw_WordCloud(self):
        data = ["happy", "sad", "hungry", "hungry", "design", "right", "wrong", "end", "happy"]
        words = ' '.join(data)
        wordcloud = WordCloud(
            background_color="white",
            width=2500, height=2000).generate(words)

        wordcloud.to_file("pyqt/wordCloud.png")
        self.wordCloud.setPixmap(QtGui.QPixmap("pyqt/wordCloud.png"))
        self.wordCloud.setScaledContents(True)

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
