from PyQt5 import QtCore, QtGui, QtWidgets, QtWebEngineWidgets
import sys
from pyqt.about_window import Ui_Form
from pyqt.browser_dialog import Ui_browserDialog
from pyqt.preferences_window import Ui_Form as PrefWindow
from urlProcessor.blacklists import Blacklists

class About(QtWidgets.QMainWindow, Ui_Form):
    def __init__(self, *args, obj=None, **kwargs):
        super(About, self).__init__(*args, **kwargs)
        self.setupUi(self)

class Dialog(QtWidgets.QMainWindow, Ui_browserDialog):
    def __init__(self, *args, obj=None, **kwargs):
        super(Dialog, self).__init__(*args, **kwargs)
        self.setupUi(self)

class Preference(QtWidgets.QMainWindow, PrefWindow):
    def __init__(self, *args, obj=None, **kwargs):
        super(Preference, self).__init__(*args, **kwargs)
        self.setupUi(self)
        self.blacklists = Blacklists()
        self.addTagButton.clicked.connect(self.addTag)
        self.deleteTagButton.clicked.connect(self.removeTag)
        self.addUrlButton.clicked.connect(self.addUrl)
        self.deleteUrlButton.clicked.connect(self.removeURL)

    def addTag(self):
        tag = self.tagEdit.toPlainText()
        self.blacklists.addItem(tag, "tagSet")
        self.showPopUp("Tag added!")
        self.tagEdit.clear()

    def removeTag(self):
        tag = self.tagEdit.toPlainText()
        self.blacklists.removeItem(tag, "tagSet")
        self.showPopUp("Tag removed!")
        self.tagEdit.clear()

    def addUrl(self):
        url = self.urlEdit.toPlainText()
        self.blacklists.addItem(url, "urlSet")
        self.showPopUp("URL added!")
        self.urlEdit.clear()

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
        msg.exec_()

class Stream(QtCore.QObject):
    """Redirects console output to text widget."""
    newText = QtCore.pyqtSignal(str)
    
    def write(self, text):
        self.newText.emit(str(text))

class DashWindow(QtWidgets.QMainWindow):
    def __init__(self, *args, **kwargs):
        super(DashWindow, self).__init__(*args, **kwargs)

        self.setWindowTitle("Window Title")

        label = QtGui.QLabel("Label")
        label.setAlignment(QtCore.Qt.AlignCenter)
#        
        layout = QtGui.QVBoxLayout()
        
        web = QtWebEngineWidgets.QWebEngineView()
        web.load(QtCore.QUrl("http://127.0.0.1:8050"))

        layout.addWidget(web)

        widget = QtGui.QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)  