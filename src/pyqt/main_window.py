import sys

# flake8: noqa
from PyQt5 import QtCore, QtGui, QtWidgets

import pyqt.resource_rc


class Ui_MainWindow:
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1081, 720)
        MainWindow.setMinimumSize(QtCore.QSize(1081, 720))
        MainWindow.setMaximumSize(QtCore.QSize(1081, 720))
        icon = QtGui.QIcon()
        icon.addPixmap(
            QtGui.QPixmap(
                ":/newPrefix/icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off
        )
        MainWindow.setWindowIcon(icon)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setGeometry(QtCore.QRect(0, 0, 1081, 671))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.stackedWidget.setFont(font)
        self.stackedWidget.setStatusTip("")
        self.stackedWidget.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.stackedWidget.setStyleSheet("")
        self.stackedWidget.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.stackedWidget.setObjectName("stackedWidget")
        self.homePage = QtWidgets.QWidget()
        self.homePage.setObjectName("homePage")
        self.browserTextLabel = QtWidgets.QLabel(self.homePage)
        self.browserTextLabel.setGeometry(QtCore.QRect(430, 170, 199, 21))
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(
            self.browserTextLabel.sizePolicy().hasHeightForWidth()
        )
        self.browserTextLabel.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.browserTextLabel.setFont(font)
        self.browserTextLabel.setStyleSheet("")
        self.browserTextLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.browserTextLabel.setObjectName("browserTextLabel")
        self.emptyBox = QtWidgets.QLabel(self.homePage)
        self.emptyBox.setGeometry(QtCore.QRect(410, 180, 241, 101))
        self.emptyBox.setStyleSheet(
            "border: 1px solid rgb(165, 165, 165);\n" "")
        self.emptyBox.setText("")
        self.emptyBox.setObjectName("emptyBox")
        self.dateComboBox = QtWidgets.QComboBox(self.homePage)
        self.dateComboBox.setGeometry(QtCore.QRect(430, 331, 199, 58))
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(
            self.dateComboBox.sizePolicy().hasHeightForWidth())
        self.dateComboBox.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.dateComboBox.setFont(font)
        self.dateComboBox.setCursor(
            QtGui.QCursor(
                QtCore.Qt.PointingHandCursor))
        self.dateComboBox.setStyleSheet("border: 1px solid black")
        self.dateComboBox.setObjectName("dateComboBox")
        self.dateComboBox.addItem("")
        self.dateComboBox.addItem("")
        self.dateComboBox.addItem("")
        self.dateComboBox.addItem("")
        self.dateComboBox.addItem("")
        self.dateComboBox.addItem("")
        self.dateTextLabel = QtWidgets.QLabel(self.homePage)
        self.dateTextLabel.setGeometry(QtCore.QRect(430, 300, 199, 24))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.dateTextLabel.setFont(font)
        self.dateTextLabel.setStyleSheet("")
        self.dateTextLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.dateTextLabel.setObjectName("dateTextLabel")
        self.emotHeader = QtWidgets.QLabel(self.homePage)
        self.emotHeader.setGeometry(QtCore.QRect(390, 28, 279, 121))
        font = QtGui.QFont()
        font.setPointSize(40)
        font.setBold(False)
        font.setWeight(50)
        self.emotHeader.setFont(font)
        self.emotHeader.setAlignment(QtCore.Qt.AlignCenter)
        self.emotHeader.setObjectName("emotHeader")
        self.emptyBox_2 = QtWidgets.QLabel(self.homePage)
        self.emptyBox_2.setGeometry(QtCore.QRect(410, 310, 241, 101))
        self.emptyBox_2.setStyleSheet(
            "border: 1px solid rgb(165, 165, 165);\n" "")
        self.emptyBox_2.setText("")
        self.emptyBox_2.setObjectName("emptyBox_2")
        self.button = QtWidgets.QPushButton(self.homePage)
        self.button.setGeometry(QtCore.QRect(390, 450, 279, 99))
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.button.sizePolicy().hasHeightForWidth())
        self.button.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.button.setFont(font)
        self.button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.button.setAutoFillBackground(False)
        self.button.setStyleSheet(
            "color: rgb(255, 255, 255);\n"
            "selection-color: rgb(0, 0, 0);\n"
            "background-color: rgb(103, 171, 159);\n"
            "selection-background-color: rgb(68, 112, 104);\n"
            "border: 1px solid black;\n"
            "border-radius: 10px;"
        )
        self.button.setObjectName("button")
        self.browserComboBox = QtWidgets.QComboBox(self.homePage)
        self.browserComboBox.setGeometry(QtCore.QRect(430, 200, 199, 58))
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(2)
        sizePolicy.setHeightForWidth(
            self.browserComboBox.sizePolicy().hasHeightForWidth()
        )
        self.browserComboBox.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.browserComboBox.setFont(font)
        self.browserComboBox.setCursor(
            QtGui.QCursor(QtCore.Qt.PointingHandCursor))
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
        self.emptyBox_2.raise_()
        self.emptyBox.raise_()
        self.browserTextLabel.raise_()
        self.dateComboBox.raise_()
        self.dateTextLabel.raise_()
        self.emotHeader.raise_()
        self.button.raise_()
        self.browserComboBox.raise_()
        self.stackedWidget.addWidget(self.homePage)
        self.printPage = QtWidgets.QWidget()
        self.printPage.setObjectName("printPage")
        self.emotHeader2 = QtWidgets.QLabel(self.printPage)
        self.emotHeader2.setGeometry(QtCore.QRect(388, 40, 281, 91))
        font = QtGui.QFont()
        font.setPointSize(40)
        font.setBold(False)
        font.setWeight(50)
        self.emotHeader2.setFont(font)
        self.emotHeader2.setAlignment(QtCore.Qt.AlignCenter)
        self.emotHeader2.setObjectName("emotHeader2")
        self.textEdit = QtWidgets.QTextEdit(self.printPage)
        self.textEdit.setGeometry(QtCore.QRect(260, 130, 531, 301))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.textEdit.setFont(font)
        self.textEdit.setStyleSheet(
            "border: 1px solid black;\n"
            "border-radius: 10px;")
        self.textEdit.setSizeAdjustPolicy(
            QtWidgets.QAbstractScrollArea.AdjustIgnored)
        self.textEdit.setReadOnly(True)
        self.textEdit.setObjectName("textEdit")
        self.results_button = QtWidgets.QPushButton(self.printPage)
        self.results_button.setGeometry(QtCore.QRect(380, 450, 291, 101))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.results_button.setFont(font)
        self.results_button.setCursor(
            QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.results_button.setAutoFillBackground(False)
        self.results_button.setStyleSheet(
            "color: rgb(255, 255, 255);\n"
            "background-color: rgb(255, 125, 102);\n"
            "border: 1px solid black;\n"
            "border-radius: 10px;"
        )
        self.results_button.setObjectName("results_button")
        self.stackedWidget.addWidget(self.printPage)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1081, 26))
        self.menubar.setStyleSheet("")
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setStyleSheet(
            "selection-background-color: rgb(103, 171, 159);\n"
            "selection-color: rgb(255, 255, 255);"
        )
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionpreferences = QtWidgets.QAction(MainWindow)
        self.actionpreferences.setVisible(True)
        self.actionpreferences.setObjectName("actionpreferences")
        self.actionabout = QtWidgets.QAction(MainWindow)
        self.actionabout.setObjectName("actionabout")
        self.actionNew = QtWidgets.QAction(MainWindow)
        self.actionNew.setObjectName("actionNew")
        self.actionPreferences = QtWidgets.QAction(MainWindow)
        self.actionPreferences.setObjectName("actionPreferences")
        self.actionAbout = QtWidgets.QAction(MainWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.menuFile.addAction(self.actionNew)
        self.menuFile.addAction(self.actionPreferences)
        self.menuFile.addAction(self.actionAbout)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "eMot"))
        self.browserTextLabel.setText(_translate(
            "MainWindow", "Choose Your Browser"))
        self.dateComboBox.setStatusTip(_translate(
            "MainWindow", "Choose a date filter"))
        self.dateComboBox.setItemText(0, _translate("MainWindow", "All"))
        self.dateComboBox.setItemText(1, _translate("MainWindow", "Hour"))
        self.dateComboBox.setItemText(2, _translate("MainWindow", "Day"))
        self.dateComboBox.setItemText(3, _translate("MainWindow", "Week"))
        self.dateComboBox.setItemText(4, _translate("MainWindow", "Month"))
        self.dateComboBox.setItemText(5, _translate("MainWindow", "Year"))
        self.dateTextLabel.setText(
            _translate(
                "MainWindow",
                "Choose A Date Filter"))
        self.emotHeader.setText(_translate("MainWindow", "eMot"))
        self.button.setStatusTip(
            _translate("MainWindow", "Click to start the sentiment analysis")
        )
        self.button.setText(_translate("MainWindow", "Go!"))
        self.browserComboBox.setStatusTip(
            _translate("MainWindow", "Choose the browser you want to use")
        )
        self.browserComboBox.setCurrentText(
            _translate("MainWindow", "Select Browser"))
        self.browserComboBox.setItemText(
            0, _translate("MainWindow", "Select Browser"))
        self.browserComboBox.setItemText(1, _translate("MainWindow", "Chrome"))
        self.browserComboBox.setItemText(2, _translate("MainWindow", "Edge"))
        self.browserComboBox.setItemText(
            3, _translate("MainWindow", "Firefox"))
        self.browserComboBox.setItemText(4, _translate("MainWindow", "Safari"))
        self.browserComboBox.setItemText(5, _translate("MainWindow", "Brave"))
        self.browserComboBox.setItemText(6, _translate("MainWindow", "Opera"))
        self.emotHeader2.setText(_translate("MainWindow", "eMot"))
        self.results_button.setStatusTip(
            _translate("MainWindow", "Click to start the sentiment analysis")
        )
        self.results_button.setText(_translate("MainWindow", "Calculating..."))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.actionpreferences.setText(_translate("MainWindow", "Preferences"))
        self.actionabout.setText(_translate("MainWindow", "about"))
        self.actionNew.setText(_translate("MainWindow", "New"))
        self.actionPreferences.setText(_translate("MainWindow", "Preferences"))
        self.actionAbout.setText(_translate("MainWindow", "About"))


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
