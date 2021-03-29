from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from pyqt.main_window import Ui_MainWindow as MainWindow
from pyqt.about_window import Ui_Form
from pyqt.browser_dialog import Ui_browserDialog
from pyqt.print_window import Ui_MainWindow as PWindow
from eMot import Emot
from pyqt import dockerRunner

class Main(QtWidgets.QMainWindow, MainWindow):
    def __init__(self, *args, obj=None, **kwargs):
        super(Main, self).__init__(*args, **kwargs)
        self.setupUi(self)

        self.AboutWindow = AboutWindow()
        self.DialogWindow = DialogWindow()
        self.PrintWindow = PrintWindow()
        
        self.actionabout.triggered.connect(
            lambda checked: self.toggle_window(self.AboutWindow)
        )

        self.button.clicked.connect(self.go_button)

    def toggle_window(self, window):
        if window.isVisible():
            window.hide()
        else:
            window.show()

    def go_button(self):
        browser = str(self.browserComboBox.currentText()).capitalize()
        filtr = str(self.dateComboBox.currentText()).capitalize()

        dockerOn = dockerRunner.is_running("splash")

        if browser == "Select Browser":
            self.toggle_window(self.DialogWindow)

        else:
            self.PrintWindow.show()

            if not dockerOn:
                print("The docker container needs to be turned on..")
            else:
                Emot(filtr, browser)
                print("Finished!")

class AboutWindow(QtWidgets.QMainWindow, Ui_Form):
    def __init__(self, *args, obj=None, **kwargs):
        super(AboutWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)

class DialogWindow(QtWidgets.QMainWindow, Ui_browserDialog):
    def __init__(self, *args, obj=None, **kwargs):
        super(DialogWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)

class PrintWindow(QtWidgets.QMainWindow, PWindow):
    def __init__(self, *args, obj=None, **kwargs):
        super(PrintWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)

        # Create the text output widget.
        self.process = self.textEdit
        self.process.ensureCursorVisible()
        self.process.setLineWrapColumnOrWidth(400)
        self.process.setLineWrapMode(self.textEdit.FixedPixelWidth)
        self.process.setFixedHeight(369)
        self.process.move(10, 10)

        sys.stdout = Stream(newText=self.onUpdateText)

    def onUpdateText(self, text):
        """Write console output to text widget."""
        cursor = self.process.textCursor()
        cursor.movePosition(QtGui.QTextCursor.End)
        cursor.insertText(text)
        self.process.setTextCursor(cursor)
        self.process.ensureCursorVisible()
    
    def closeEvent(self, event):
        """Shuts down application on close."""
        # Return stdout to defaults.
        sys.stdout = sys.__stdout__
        super().closeEvent(event)

class Stream(QtCore.QObject):
    """Redirects console output to text widget."""
    newText = QtCore.pyqtSignal(str)
    
    def write(self, text):
        self.newText.emit(str(text))

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    main = Main()
    main.show()
    app.exec_()