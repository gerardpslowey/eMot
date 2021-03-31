from PyQt5 import QtCore, QtGui, QtWidgets
import sys, subprocess
from qtWorker import Worker
from pyqt.main_window import Ui_MainWindow as MainWindow
from pyqt.windows import AboutWindow, DialogWindow, PrintWindow, PreferenceWindow
from eMot import Emot
from tests import dockerRunner
from urlProcessor.blacklists import Blacklists

class Main(QtWidgets.QMainWindow, MainWindow):
    def __init__(self, *args, obj=None, **kwargs):
        super(Main, self).__init__(*args, **kwargs)
        self.setupUi(self)

        self.threadpool = QtCore.QThreadPool()

        self.AboutWindow = AboutWindow()
        self.DialogWindow = DialogWindow()
        self.PrintWindow = PrintWindow()
        self.PreferenceWindow = PreferenceWindow()
        
        self.actionAbout.triggered.connect(
            lambda checked: self.toggle_item(self.AboutWindow))

        self.actionPreferences.triggered.connect(
            lambda checked: self.toggle_item(self.PreferenceWindow))

        self.actionNew.triggered.connect(self.restart_window)
        self.button.clicked.connect(self.go_button)
        self.PrintWindow.analysis_button.clicked.connect(self.onAnalysisButton)

        self.blacklists = Blacklists()
        self.PreferenceWindow.addTagButton.clicked.connect(self.addTag)
        self.PreferenceWindow.deleteTagButton.clicked.connect(self.removeTag)
        self.PreferenceWindow.addUrlButton.clicked.connect(self.addUrl)
        self.PreferenceWindow.deleteUrlButton.clicked.connect(self.removeURL)

    def addTag(self):
        tag = self.PreferenceWindow.tagEdit.toPlainText()
        self.blacklists.addItem(tag, "tagSet")
        self.showPopUp("Tag added!")
        self.PreferenceWindow.tagEdit.clear()

    def removeTag(self):
        tag = self.PreferenceWindow.tagEdit.toPlainText()
        self.blacklists.removeItem(tag, "tagSet")
        self.showPopUp("Tag removed!")
        self.PreferenceWindow.tagEdit.clear()

    def addUrl(self):
        url = self.PreferenceWindow.urlEdit.toPlainText()
        self.blacklists.addItem(url, "urlSet")
        self.showPopUp("URL added!")
        self.PreferenceWindow.urlEdit.clear()

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
        x = msg.exec_()

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
            self.PrintWindow.show()
            worker = Worker(Emot, filtr, browser)
            self.threadpool.start(worker)
            worker.signals.finished.connect(self.toggleAnalysis)

    def restart_window(self):
        self.close()
        subprocess.Popen(['python', 'emotQT.py'])

    def toggleAnalysis(self):
        self.PrintWindow.analysis_button.setEnabled(True)

    def onAnalysisButton(self):
            self.PrintWindow.textEdit.clear()
            print("Starting Analysis")
            # TODO: import a sentiment Program and run.
            #worker = Worker(emotSentiment) 
            # self.threadpool.start(worker)

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