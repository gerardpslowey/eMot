import sys, subprocess

from PyQt5 import QtCore, QtGui, QtWidgets
from pyqt import main_window, windows, reportCharts
from qtWorker import Worker

from eMot import Emot
from emotClassify import EmotClassify
from tests import dockerRunner

class Main(QtWidgets.QMainWindow, main_window.Ui_MainWindow):

    def __init__(self, *args, obj=None, **kwargs):
        super(Main, self).__init__(*args, **kwargs)
        self.setupUi(self)
        self.stackedWidget.setCurrentWidget(self.homePage)

        self.threadpool = QtCore.QThreadPool()
        self.emotClassify = EmotClassify()

        #Set all the UI windows
        self.AboutWindow = windows.About()
        self.DialogWindow = windows.Dialog()
        self.PreferenceWindow = windows.Preference()
        
        #file menu
        self.actionAbout.triggered.connect(lambda checked: self.toggle_item(self.AboutWindow))
        self.actionPreferences.triggered.connect(lambda checked: self.toggle_item(self.PreferenceWindow))
        self.actionNew.triggered.connect(self.restart_window)
        
        self.button.clicked.connect(self.go_button)
        self.results_button.setEnabled(False)
        self.results_button.clicked.connect(self.showPieChart)

    def restart_window(self):
        self.close()
        subprocess.Popen(['python', 'emotQT.py'])

    def toggle_item(self, item):
        if item.isVisible():
            item.hide()
        else:
            item.show()

    def go_button(self):

        browser = str(self.browserComboBox.currentText()).capitalize()
        filtr = str(self.dateComboBox.currentText()).capitalize()

        if browser == "Select browser":
            self.toggle_item(self.DialogWindow)
            self.DialogWindow.label.setText("Choose a browser from \nthe dropdown menu")
            self.DialogWindow.label_2.setText("You Must Choose A Browser")

        elif not dockerRunner.is_running("splash"):
            self.toggle_item(self.DialogWindow)
            self.DialogWindow.label.setText("The splash docker \nmust to be turned on")
            self.DialogWindow.label_2.setText("Docker Container")

        else:
            self.setupPrintPage(filtr, browser)

    def setupPrintPage(self, filtr, browser):

        self.stackedWidget.setCurrentWidget(self.printPage)
        sys.stdout = windows.Stream(newText=self.onUpdateText)
        
        emot = Emot(filtr, browser)
        worker = Worker(emot.startTasks)
        self.threadpool.start(worker)
        worker.signals.finished.connect(self.startClassify)

    def onUpdateText(self, text):

        #Write console output to textEdit widget.
        cursor = self.textEdit.textCursor()
        cursor.movePosition(QtGui.QTextCursor.End)
        cursor.insertText(text)
        self.textEdit.setTextCursor(cursor)
        self.textEdit.ensureCursorVisible()

    def startClassify(self):
        self.textEdit.clear()
        print("Starting Classification..")
        worker = Worker(self.emotClassify.classify) 
        self.threadpool.start(worker)
        worker.signals.finished.connect(self.enableResultsButton)

    def enableResultsButton(self):
        self.results_button.setEnabled(True)
        self.results_button.setStyleSheet(
            "color: rgb(255, 255, 255);\n"                                        
            "background-color: rgb(103, 171, 159);\n"
            "border: 1px solid black;")

    def showPieChart(self):

        self.stackedWidget.setCurrentWidget(self.reportsPage)
        emotionsDict = self.emotClassify.get_emotion_count()
        pieChart = reportCharts.PieChart(emotionsDict)

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