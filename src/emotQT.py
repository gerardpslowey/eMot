# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'emotQT.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from functools import partial
from q import Emot

class Ui_emotMainWindow(object):
    def setupUi(self, emotMainWindow):
        emotMainWindow.setObjectName("emotMainWindow")
        emotMainWindow.resize(800, 600)
        emotMainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(emotMainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.emotText = QtWidgets.QLabel(self.centralwidget)
        self.emotText.setGeometry(QtCore.QRect(270, 60, 251, 121))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.emotText.setFont(font)
        self.emotText.setAlignment(QtCore.Qt.AlignCenter)
        self.emotText.setObjectName("emotText")
        self.browserChoice = QtWidgets.QComboBox(self.centralwidget)
        self.browserChoice.setGeometry(QtCore.QRect(190, 200, 141, 51))
        self.browserChoice.setObjectName("browserChoice")
        self.browserChoice.addItem("")
        self.browserChoice.addItem("")
        self.browserChoice.addItem("")
        self.browserChoice.addItem("")
        self.browserChoice.addItem("")
        self.browserChoice.addItem("")
        self.filterChoice = QtWidgets.QComboBox(self.centralwidget)
        self.filterChoice.setGeometry(QtCore.QRect(460, 200, 141, 51))
        self.filterChoice.setObjectName("filterChoice")
        self.filterChoice.addItem("")
        self.filterChoice.addItem("")
        self.filterChoice.addItem("")
        self.filterChoice.addItem("")
        self.filterChoice.addItem("")
        self.filterChoice.addItem("")
        self.browserLabel = QtWidgets.QLabel(self.centralwidget)
        self.browserLabel.setGeometry(QtCore.QRect(190, 170, 141, 31))
        self.browserLabel.setObjectName("browserLabel")
        self.dateLabel = QtWidgets.QLabel(self.centralwidget)
        self.dateLabel.setGeometry(QtCore.QRect(460, 170, 141, 31))
        self.dateLabel.setObjectName("dateLabel")
        self.goButton = QtWidgets.QPushButton(self.centralwidget)
        self.goButton.setGeometry(QtCore.QRect(190, 280, 411, 71))
        self.goButton.setObjectName("goButton")
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setGeometry(QtCore.QRect(189, 380, 411, 151))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 409, 149))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        emotMainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(emotMainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        self.menuNew = QtWidgets.QMenu(self.menubar)
        self.menuNew.setObjectName("menuNew")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        emotMainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(emotMainWindow)
        self.statusbar.setObjectName("statusbar")
        emotMainWindow.setStatusBar(self.statusbar)
        self.actionNew = QtWidgets.QAction(emotMainWindow)
        self.actionNew.setObjectName("actionNew")
        self.actionAbout = QtWidgets.QAction(emotMainWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.actionPreferences = QtWidgets.QAction(emotMainWindow)
        self.actionPreferences.setObjectName("actionPreferences")
        self.menuNew.addAction(self.actionNew)
        self.menuNew.addAction(self.actionPreferences)
        self.menuHelp.addAction(self.actionAbout)
        self.menubar.addAction(self.menuNew.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(emotMainWindow)
        QtCore.QMetaObject.connectSlotsByName(emotMainWindow)

        self.goButton.clicked.connect(partial(Emot, str(self.browserChoice.currentText()), str(self.filterChoice.currentText())))


    def retranslateUi(self, emotMainWindow):
        _translate = QtCore.QCoreApplication.translate
        emotMainWindow.setWindowTitle(_translate("emotMainWindow", "eMot"))
        self.emotText.setText(_translate("emotMainWindow", "eMot"))
        self.browserChoice.setStatusTip(_translate("emotMainWindow", "Choose the browser you use"))
        self.browserChoice.setItemText(0, _translate("emotMainWindow", "Chrome"))
        self.browserChoice.setItemText(1, _translate("emotMainWindow", "Edge"))
        self.browserChoice.setItemText(2, _translate("emotMainWindow", "Firefox"))
        self.browserChoice.setItemText(3, _translate("emotMainWindow", "Safari"))
        self.browserChoice.setItemText(4, _translate("emotMainWindow", "Brave"))
        self.browserChoice.setItemText(5, _translate("emotMainWindow", "Opera"))
        self.filterChoice.setStatusTip(_translate("emotMainWindow", "Choose the date filter"))
        self.filterChoice.setItemText(0, _translate("emotMainWindow", "All"))
        self.filterChoice.setItemText(1, _translate("emotMainWindow", "Hour"))
        self.filterChoice.setItemText(2, _translate("emotMainWindow", "Day"))
        self.filterChoice.setItemText(3, _translate("emotMainWindow", "Week"))
        self.filterChoice.setItemText(4, _translate("emotMainWindow", "Month"))
        self.filterChoice.setItemText(5, _translate("emotMainWindow", "Year"))
        self.browserLabel.setText(_translate("emotMainWindow", "Choose Your Browser "))
        self.dateLabel.setText(_translate("emotMainWindow", "Choose Date Filter"))
        self.goButton.setStatusTip(_translate("emotMainWindow", "Click to start the Sentiment Analysis"))
        self.goButton.setText(_translate("emotMainWindow", "Go!"))
        self.menuNew.setTitle(_translate("emotMainWindow", "File"))
        self.menuHelp.setTitle(_translate("emotMainWindow", "Help"))
        self.actionNew.setText(_translate("emotMainWindow", "New"))
        self.actionAbout.setText(_translate("emotMainWindow", "About"))
        self.actionPreferences.setText(_translate("emotMainWindow", "Preferences"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    emotMainWindow = QtWidgets.QMainWindow()
    ui = Ui_emotMainWindow()
    ui.setupUi(emotMainWindow)
    emotMainWindow.show()
    sys.exit(app.exec_())
