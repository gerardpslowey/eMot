import sys
from pathlib import Path

from PyQt5.QtWidgets import QMainWindow, QMessageBox

from pyqt.about_window import Ui_About
from pyqt.browser_dialog import Ui_browserDialog
from pyqt.preferences_window import Ui_Form as PrefWindow
from utils.blacklists import Blacklists
from utils.urlFilter import base

sys.path.append(str(Path(__file__).parent.parent.absolute()))


class About(QMainWindow, Ui_About):
    """Super class of about_windows since it can be changed at any time from ui files."""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)


class Dialog(QMainWindow, Ui_browserDialog):
    """Super class of browser_dialog since it can be changed at any time from ui files."""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)


class Preference(QMainWindow, PrefWindow):
    """
    Super class of preferences_windows since it can be changed at any time from ui files.
    This class is extended to add functionality to the tag and url buttons.
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)
        self.blacklists = Blacklists()
        self.addTagButton.clicked.connect(self.addTag)
        self.deleteTagButton.clicked.connect(self.removeTag)
        self.addUrlButton.clicked.connect(self.addUrl)
        self.deleteUrlButton.clicked.connect(self.removeURL)

        self.errorMessage = "Please enter some text"

    def addTag(self):
        tag = self.tagEdit.toPlainText()
        if tag:
            self.blacklists.addItem(tag, "tagSet")
            self.showPopUp("Tag added!")
            self.tagEdit.clear()
        else:
            self.showPopUp(self.errorMessage)

    def removeTag(self):
        tag = self.tagEdit.toPlainText()
        if tag:
            self.blacklists.removeItem(tag, "tagSet")
            self.showPopUp("Tag removed!")
            self.tagEdit.clear()
        else:
            self.showPopUp(self.errorMessage)

    def addUrl(self):
        url = self.urlEdit.toPlainText()
        if url:
            baseUrl = base(url)
            self.blacklists.addItem(baseUrl, "urlSet")
            self.showPopUp("URL added!")
            self.urlEdit.clear()
        else:
            self.showPopUp(self.errorMessage)

    def removeURL(self):
        url = self.urlEdit.toPlainText()
        if url:
            baseUrl = base(url)
            self.blacklists.removeItem(baseUrl, "urlSet")
            self.showPopUp("URL removed!")
            self.urlEdit.clear()
        else:
            self.showPopUp(self.errorMessage)

    def showPopUp(self, message):
        msg = QMessageBox()
        msg.setWindowTitle("Message")
        msg.setText(message)
        msg.setIcon(QMessageBox.Information)
        msg.setStandardButtons(QMessageBox.Ok)
        msg.exec_()
