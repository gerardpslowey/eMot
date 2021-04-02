from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from pyqt.about_window import Ui_Form
from pyqt.browser_dialog import Ui_browserDialog
from pyqt.print_window import Ui_MainWindow as PrintWindow
from pyqt.preferences_window import Ui_Form as PrefWindow

class AboutWindow(QtWidgets.QMainWindow, Ui_Form):
    def __init__(self, *args, obj=None, **kwargs):
        super(AboutWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)

class DialogWindow(QtWidgets.QMainWindow, Ui_browserDialog):
    def __init__(self, *args, obj=None, **kwargs):
        super(DialogWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)

class PreferenceWindow(QtWidgets.QMainWindow, PrefWindow):
    def __init__(self, *args, obj=None, **kwargs):
        super(PreferenceWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)

class PrintWindow(QtWidgets.QMainWindow, PrintWindow):
    def __init__(self, *args, obj=None, **kwargs):
        super(PrintWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)
        self.results_button.setEnabled(False)
        sys.stdout = Stream(newText=self.onUpdateText)

    def onUpdateText(self, text):
        """Write console output to text widget."""
        cursor = self.textEdit.textCursor()
        cursor.movePosition(QtGui.QTextCursor.End)
        cursor.insertText(text)
        self.textEdit.setTextCursor(cursor)
        self.textEdit.ensureCursorVisible()
    
    def closeEvent(self, event):
        """Shuts down application on close."""
        self.textEdit.clear()
        self.results_button.setStyleSheet("color: rgb(255, 255, 255);\n"
                                        "background-color: rgb(255, 125, 102);\n"
                                        "border: 1px solid black;")
        super().closeEvent(event)

class Stream(QtCore.QObject):
    """Redirects console output to text widget."""
    newText = QtCore.pyqtSignal(str)
    
    def write(self, text):
        self.newText.emit(str(text))