from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from pyqt.main_window import Ui_MainWindow as MainWindow
from pyqt.about_window import Ui_Form
from pyqt.browser_dialog import Ui_browserDialog
from pyqt.print_window import Ui_MainWindow as PWindow

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
        browser = str(self.browserComboBox.currentText())
        filtr = str(self.dateComboBox.currentText())

        if browser == "Select Browser":
            self.DialogWindow.show()
        else:
            self.PrintWindow.show()



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

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    main = Main()
    main.show()
    app.exec_()