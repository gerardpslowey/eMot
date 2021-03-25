# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_window.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(880, 600)
        MainWindow.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.emotHeader = QtWidgets.QLabel(self.centralwidget)
        self.emotHeader.setGeometry(QtCore.QRect(330, 40, 221, 100))
        font = QtGui.QFont()
        font.setPointSize(40)
        font.setBold(False)
        font.setWeight(50)
        self.emotHeader.setFont(font)
        self.emotHeader.setAlignment(QtCore.Qt.AlignCenter)
        self.emotHeader.setObjectName("emotHeader")
        self.browserTextLabel = QtWidgets.QLabel(self.centralwidget)
        self.browserTextLabel.setGeometry(QtCore.QRect(350, 150, 191, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.browserTextLabel.setFont(font)
        self.browserTextLabel.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.browserTextLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.browserTextLabel.setObjectName("browserTextLabel")
        self.emptyBox = QtWidgets.QLabel(self.centralwidget)
        self.emptyBox.setGeometry(QtCore.QRect(320, 160, 251, 91))
        self.emptyBox.setStyleSheet("border: 1px solid rgb(165, 165, 165);\n"
"background-color: rgb(255, 255, 255);\n"
"")
        self.emptyBox.setText("")
        self.emptyBox.setObjectName("emptyBox")
        self.browserComboBox = QtWidgets.QComboBox(self.centralwidget)
        self.browserComboBox.setGeometry(QtCore.QRect(340, 180, 211, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.browserComboBox.setFont(font)
        self.browserComboBox.setStyleSheet("border: 1px solid black")
        self.browserComboBox.setPlaceholderText("")
        self.browserComboBox.setObjectName("browserComboBox")
        self.browserComboBox.addItem("")
        self.browserComboBox.addItem("")
        self.browserComboBox.addItem("")
        self.browserComboBox.addItem("")
        self.browserComboBox.addItem("")
        self.browserComboBox.addItem("")
        self.browserComboBox.addItem("")
        self.dateTextLabel = QtWidgets.QLabel(self.centralwidget)
        self.dateTextLabel.setGeometry(QtCore.QRect(350, 270, 191, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.dateTextLabel.setFont(font)
        self.dateTextLabel.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.dateTextLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.dateTextLabel.setObjectName("dateTextLabel")
        self.emptyBox_2 = QtWidgets.QLabel(self.centralwidget)
        self.emptyBox_2.setGeometry(QtCore.QRect(320, 280, 251, 101))
        self.emptyBox_2.setStyleSheet("border: 1px solid rgb(165, 165, 165);\n"
"background-color: rgb(255, 255, 255);\n"
"")
        self.emptyBox_2.setText("")
        self.emptyBox_2.setObjectName("emptyBox_2")
        self.dateComboBox = QtWidgets.QComboBox(self.centralwidget)
        self.dateComboBox.setGeometry(QtCore.QRect(340, 300, 211, 61))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.dateComboBox.setFont(font)
        self.dateComboBox.setStyleSheet("border: 1px solid black")
        self.dateComboBox.setObjectName("dateComboBox")
        self.dateComboBox.addItem("")
        self.dateComboBox.addItem("")
        self.dateComboBox.addItem("")
        self.dateComboBox.addItem("")
        self.dateComboBox.addItem("")
        self.dateComboBox.addItem("")
        self.button = QtWidgets.QPushButton(self.centralwidget)
        self.button.setGeometry(QtCore.QRect(290, 410, 311, 81))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.button.setFont(font)
        self.button.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(103, 171, 159);\n"
"border: 1px solid black;")
        self.button.setObjectName("button")
        self.emptyBox_2.raise_()
        self.emotHeader.raise_()
        self.emptyBox.raise_()
        self.browserTextLabel.raise_()
        self.browserComboBox.raise_()
        self.dateTextLabel.raise_()
        self.dateComboBox.raise_()
        self.button.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 880, 26))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionpreferences = QtWidgets.QAction(MainWindow)
        self.actionpreferences.setObjectName("actionpreferences")
        self.actionabout = QtWidgets.QAction(MainWindow)
        self.actionabout.setObjectName("actionabout")
        self.menuFile.addAction(self.actionpreferences)
        self.menuFile.addAction(self.actionabout)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.emotHeader.setText(_translate("MainWindow", "eMot"))
        self.browserTextLabel.setText(_translate("MainWindow", "Choose Your Browser"))
        self.browserComboBox.setStatusTip(_translate("MainWindow", "Choose the browser you want to use"))
        self.browserComboBox.setCurrentText(_translate("MainWindow", "Select Browser"))
        self.browserComboBox.setItemText(0, _translate("MainWindow", "Select Browser"))
        self.browserComboBox.setItemText(1, _translate("MainWindow", "Chrome"))
        self.browserComboBox.setItemText(2, _translate("MainWindow", "Edge"))
        self.browserComboBox.setItemText(3, _translate("MainWindow", "Firefox"))
        self.browserComboBox.setItemText(4, _translate("MainWindow", "Safari"))
        self.browserComboBox.setItemText(5, _translate("MainWindow", "Brave"))
        self.browserComboBox.setItemText(6, _translate("MainWindow", "Opera"))
        self.dateTextLabel.setText(_translate("MainWindow", "Choose A Date Filter"))
        self.dateComboBox.setStatusTip(_translate("MainWindow", "Choose a date filter"))
        self.dateComboBox.setItemText(0, _translate("MainWindow", "All"))
        self.dateComboBox.setItemText(1, _translate("MainWindow", "Hour"))
        self.dateComboBox.setItemText(2, _translate("MainWindow", "Day"))
        self.dateComboBox.setItemText(3, _translate("MainWindow", "Week"))
        self.dateComboBox.setItemText(4, _translate("MainWindow", "Month"))
        self.dateComboBox.setItemText(5, _translate("MainWindow", "Year"))
        self.button.setStatusTip(_translate("MainWindow", "Click to start the sentiment analysis"))
        self.button.setText(_translate("MainWindow", "Go!"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.actionpreferences.setText(_translate("MainWindow", "preferences"))
        self.actionabout.setText(_translate("MainWindow", "about"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
