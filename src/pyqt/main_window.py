# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_window.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1081, 720)
        MainWindow.setMinimumSize(QtCore.QSize(1081, 720))
        MainWindow.setMaximumSize(QtCore.QSize(1081, 720))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/newPrefix/resources/icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setGeometry(QtCore.QRect(0, 0, 1081, 661))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.stackedWidget.setFont(font)
        self.stackedWidget.setStatusTip("")
        self.stackedWidget.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.stackedWidget.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.stackedWidget.setObjectName("stackedWidget")
        self.homePage = QtWidgets.QWidget()
        self.homePage.setObjectName("homePage")
        self.browserTextLabel = QtWidgets.QLabel(self.homePage)
        self.browserTextLabel.setGeometry(QtCore.QRect(430, 170, 199, 21))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.browserTextLabel.sizePolicy().hasHeightForWidth())
        self.browserTextLabel.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.browserTextLabel.setFont(font)
        self.browserTextLabel.setStyleSheet("")
        self.browserTextLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.browserTextLabel.setObjectName("browserTextLabel")
        self.emptyBox = QtWidgets.QLabel(self.homePage)
        self.emptyBox.setGeometry(QtCore.QRect(410, 180, 241, 101))
        self.emptyBox.setStyleSheet("border: 1px solid rgb(165, 165, 165);\n"
"")
        self.emptyBox.setText("")
        self.emptyBox.setObjectName("emptyBox")
        self.dateComboBox = QtWidgets.QComboBox(self.homePage)
        self.dateComboBox.setGeometry(QtCore.QRect(430, 331, 199, 58))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.dateComboBox.sizePolicy().hasHeightForWidth())
        self.dateComboBox.setSizePolicy(sizePolicy)
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
        self.dateTextLabel = QtWidgets.QLabel(self.homePage)
        self.dateTextLabel.setGeometry(QtCore.QRect(430, 300, 199, 24))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.dateTextLabel.setFont(font)
        self.dateTextLabel.setStyleSheet("")
        self.dateTextLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.dateTextLabel.setObjectName("dateTextLabel")
        self.emotHeader = QtWidgets.QLabel(self.homePage)
        self.emotHeader.setGeometry(QtCore.QRect(390, 30, 279, 119))
        font = QtGui.QFont()
        font.setPointSize(40)
        font.setBold(False)
        font.setWeight(50)
        self.emotHeader.setFont(font)
        self.emotHeader.setAlignment(QtCore.Qt.AlignCenter)
        self.emotHeader.setObjectName("emotHeader")
        self.emptyBox_2 = QtWidgets.QLabel(self.homePage)
        self.emptyBox_2.setGeometry(QtCore.QRect(410, 310, 241, 101))
        self.emptyBox_2.setStyleSheet("border: 1px solid rgb(165, 165, 165);\n"
"")
        self.emptyBox_2.setText("")
        self.emptyBox_2.setObjectName("emptyBox_2")
        self.button = QtWidgets.QPushButton(self.homePage)
        self.button.setGeometry(QtCore.QRect(390, 450, 279, 99))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button.sizePolicy().hasHeightForWidth())
        self.button.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.button.setFont(font)
        self.button.setAutoFillBackground(False)
        self.button.setStyleSheet("color: rgb(255, 255, 255);\n"
"selection-color: rgb(0, 0, 0);\n"
"background-color: rgb(103, 171, 159);\n"
"selection-background-color: rgb(68, 112, 104);\n"
"border: 1px solid black;")
        self.button.setObjectName("button")
        self.browserComboBox = QtWidgets.QComboBox(self.homePage)
        self.browserComboBox.setGeometry(QtCore.QRect(430, 200, 199, 55))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(2)
        sizePolicy.setHeightForWidth(self.browserComboBox.sizePolicy().hasHeightForWidth())
        self.browserComboBox.setSizePolicy(sizePolicy)
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
        self.emotHeader2.setGeometry(QtCore.QRect(390, 50, 279, 81))
        font = QtGui.QFont()
        font.setPointSize(40)
        font.setBold(False)
        font.setWeight(50)
        self.emotHeader2.setFont(font)
        self.emotHeader2.setAlignment(QtCore.Qt.AlignCenter)
        self.emotHeader2.setObjectName("emotHeader2")
        self.textEdit = QtWidgets.QTextEdit(self.printPage)
        self.textEdit.setGeometry(QtCore.QRect(260, 130, 531, 281))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.textEdit.setFont(font)
        self.textEdit.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustIgnored)
        self.textEdit.setReadOnly(True)
        self.textEdit.setObjectName("textEdit")
        self.results_button = QtWidgets.QPushButton(self.printPage)
        self.results_button.setGeometry(QtCore.QRect(390, 450, 281, 101))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.results_button.setFont(font)
        self.results_button.setAutoFillBackground(False)
        self.results_button.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(255, 125, 102);\n"
"border: 1px solid black;")
        self.results_button.setObjectName("results_button")
        self.stackedWidget.addWidget(self.printPage)
        self.reportsPage = QtWidgets.QWidget()
        self.reportsPage.setStyleSheet("background-color: rgb(236, 236, 236);")
        self.reportsPage.setObjectName("reportsPage")
        self.frame = QtWidgets.QFrame(self.reportsPage)
        self.frame.setGeometry(QtCore.QRect(30, 40, 241, 91))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.frame.setFont(font)
        self.frame.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.frame.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.commonTextEdit = QtWidgets.QTextEdit(self.frame)
        self.commonTextEdit.setGeometry(QtCore.QRect(10, 40, 221, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.commonTextEdit.setFont(font)
        self.commonTextEdit.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.commonTextEdit.setReadOnly(True)
        self.commonTextEdit.setObjectName("commonTextEdit")
        self.commonLabel = QtWidgets.QLabel(self.frame)
        self.commonLabel.setGeometry(QtCore.QRect(10, 15, 221, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.commonLabel.setFont(font)
        self.commonLabel.setStatusTip("")
        self.commonLabel.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.commonLabel.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.commonLabel.setObjectName("commonLabel")
        self.frame_2 = QtWidgets.QFrame(self.reportsPage)
        self.frame_2.setGeometry(QtCore.QRect(280, 40, 251, 91))
        self.frame_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.frame_2.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.websiteTextEdit = QtWidgets.QTextEdit(self.frame_2)
        self.websiteTextEdit.setGeometry(QtCore.QRect(10, 40, 231, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.websiteTextEdit.setFont(font)
        self.websiteTextEdit.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.websiteTextEdit.setReadOnly(True)
        self.websiteTextEdit.setObjectName("websiteTextEdit")
        self.websiteLabel = QtWidgets.QLabel(self.frame_2)
        self.websiteLabel.setGeometry(QtCore.QRect(10, 10, 231, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.websiteLabel.setFont(font)
        self.websiteLabel.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.websiteLabel.setObjectName("websiteLabel")
        self.frame_3 = QtWidgets.QFrame(self.reportsPage)
        self.frame_3.setGeometry(QtCore.QRect(550, 40, 501, 91))
        self.frame_3.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.frame_3.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.positiveTextEdit = QtWidgets.QTextEdit(self.frame_3)
        self.positiveTextEdit.setGeometry(QtCore.QRect(10, 40, 481, 41))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.positiveTextEdit.setFont(font)
        self.positiveTextEdit.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.positiveTextEdit.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.positiveTextEdit.setReadOnly(True)
        self.positiveTextEdit.setObjectName("positiveTextEdit")
        self.positiveLabel = QtWidgets.QLabel(self.frame_3)
        self.positiveLabel.setGeometry(QtCore.QRect(10, 10, 181, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.positiveLabel.setFont(font)
        self.positiveLabel.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.positiveLabel.setWordWrap(True)
        self.positiveLabel.setObjectName("positiveLabel")
        self.nextPageButton = QtWidgets.QPushButton(self.reportsPage)
        self.nextPageButton.setGeometry(QtCore.QRect(450, 550, 191, 81))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.nextPageButton.setFont(font)
        self.nextPageButton.setStyleSheet("background-color: rgb(85, 195, 255);\n"
"color: rgb(255, 255, 255);")
        self.nextPageButton.setObjectName("nextPageButton")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.reportsPage)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(29, 159, 501, 351))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.lineChartLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.lineChartLayout.setContentsMargins(0, 0, 0, 0)
        self.lineChartLayout.setObjectName("lineChartLayout")
        self.wordCloud = QtWidgets.QLabel(self.reportsPage)
        self.wordCloud.setGeometry(QtCore.QRect(550, 160, 501, 351))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.wordCloud.setFont(font)
        self.wordCloud.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 255, 255, 255), stop:1 rgba(103, 171, 159,255));")
        self.wordCloud.setAlignment(QtCore.Qt.AlignCenter)
        self.wordCloud.setObjectName("wordCloud")
        self.stackedWidget.addWidget(self.reportsPage)
        self.reportsPage2 = QtWidgets.QWidget()
        self.reportsPage2.setStyleSheet("background-color: rgb(236, 236, 236);")
        self.reportsPage2.setObjectName("reportsPage2")
        self.previousPageButton = QtWidgets.QPushButton(self.reportsPage2)
        self.previousPageButton.setGeometry(QtCore.QRect(450, 550, 191, 81))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.previousPageButton.setFont(font)
        self.previousPageButton.setStyleSheet("background-color: rgb(85, 195, 255);\n"
"background-color: rgb(255, 94, 105);\n"
"color: rgb(255, 255, 255);")
        self.previousPageButton.setObjectName("previousPageButton")
        self.frame_4 = QtWidgets.QFrame(self.reportsPage2)
        self.frame_4.setGeometry(QtCore.QRect(30, 40, 501, 91))
        self.frame_4.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.frame_4.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.fearTextEdit = QtWidgets.QTextEdit(self.frame_4)
        self.fearTextEdit.setGeometry(QtCore.QRect(10, 40, 481, 41))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.fearTextEdit.setFont(font)
        self.fearTextEdit.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.fearTextEdit.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.fearTextEdit.setReadOnly(True)
        self.fearTextEdit.setObjectName("fearTextEdit")
        self.fearLabel = QtWidgets.QLabel(self.frame_4)
        self.fearLabel.setGeometry(QtCore.QRect(10, 10, 201, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.fearLabel.setFont(font)
        self.fearLabel.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.fearLabel.setWordWrap(True)
        self.fearLabel.setObjectName("fearLabel")
        self.frame_5 = QtWidgets.QFrame(self.reportsPage2)
        self.frame_5.setGeometry(QtCore.QRect(550, 40, 161, 91))
        self.frame_5.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.frame_5.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.angerLabel = QtWidgets.QLabel(self.frame_5)
        self.angerLabel.setGeometry(QtCore.QRect(10, 10, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.angerLabel.setFont(font)
        self.angerLabel.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.angerLabel.setObjectName("angerLabel")
        self.angerTextEdit = QtWidgets.QTextEdit(self.frame_5)
        self.angerTextEdit.setGeometry(QtCore.QRect(10, 40, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.angerTextEdit.setFont(font)
        self.angerTextEdit.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.angerTextEdit.setReadOnly(True)
        self.angerTextEdit.setObjectName("angerTextEdit")
        self.frame_6 = QtWidgets.QFrame(self.reportsPage2)
        self.frame_6.setGeometry(QtCore.QRect(730, 40, 161, 91))
        self.frame_6.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.frame_6.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.browserUsedTextEdit = QtWidgets.QTextEdit(self.frame_6)
        self.browserUsedTextEdit.setGeometry(QtCore.QRect(10, 40, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.browserUsedTextEdit.setFont(font)
        self.browserUsedTextEdit.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.browserUsedTextEdit.setReadOnly(True)
        self.browserUsedTextEdit.setObjectName("browserUsedTextEdit")
        self.browserUsedLabel = QtWidgets.QLabel(self.frame_6)
        self.browserUsedLabel.setGeometry(QtCore.QRect(10, 10, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.browserUsedLabel.setFont(font)
        self.browserUsedLabel.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.browserUsedLabel.setObjectName("browserUsedLabel")
        self.frame_7 = QtWidgets.QFrame(self.reportsPage2)
        self.frame_7.setGeometry(QtCore.QRect(910, 40, 141, 91))
        self.frame_7.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.frame_7.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_7.setObjectName("frame_7")
        self.dateFilterLabel = QtWidgets.QLabel(self.frame_7)
        self.dateFilterLabel.setGeometry(QtCore.QRect(10, 10, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.dateFilterLabel.setFont(font)
        self.dateFilterLabel.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.dateFilterLabel.setObjectName("dateFilterLabel")
        self.dateFiltrTextEdit = QtWidgets.QTextEdit(self.frame_7)
        self.dateFiltrTextEdit.setGeometry(QtCore.QRect(10, 40, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.dateFiltrTextEdit.setFont(font)
        self.dateFiltrTextEdit.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.dateFiltrTextEdit.setReadOnly(True)
        self.dateFiltrTextEdit.setObjectName("dateFiltrTextEdit")
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.reportsPage2)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(29, 159, 501, 351))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.pieChartLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.pieChartLayout.setContentsMargins(0, 0, 0, 0)
        self.pieChartLayout.setObjectName("pieChartLayout")
        self.verticalLayoutWidget_4 = QtWidgets.QWidget(self.reportsPage2)
        self.verticalLayoutWidget_4.setGeometry(QtCore.QRect(550, 160, 501, 351))
        self.verticalLayoutWidget_4.setObjectName("verticalLayoutWidget_4")
        self.barChartLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_4)
        self.barChartLayout.setContentsMargins(0, 0, 0, 0)
        self.barChartLayout.setObjectName("barChartLayout")
        self.stackedWidget.addWidget(self.reportsPage2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1081, 26))
        self.menubar.setStyleSheet("")
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setStyleSheet("selection-background-color: rgb(103, 171, 159);\n"
"selection-color: rgb(255, 255, 255);")
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
        self.stackedWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "eMot"))
        self.browserTextLabel.setText(_translate("MainWindow", "Choose Your Browser"))
        self.dateComboBox.setStatusTip(_translate("MainWindow", "Choose a date filter"))
        self.dateComboBox.setItemText(0, _translate("MainWindow", "All"))
        self.dateComboBox.setItemText(1, _translate("MainWindow", "Hour"))
        self.dateComboBox.setItemText(2, _translate("MainWindow", "Day"))
        self.dateComboBox.setItemText(3, _translate("MainWindow", "Week"))
        self.dateComboBox.setItemText(4, _translate("MainWindow", "Month"))
        self.dateComboBox.setItemText(5, _translate("MainWindow", "Year"))
        self.dateTextLabel.setText(_translate("MainWindow", "Choose A Date Filter"))
        self.emotHeader.setText(_translate("MainWindow", "eMot"))
        self.button.setStatusTip(_translate("MainWindow", "Click to start the sentiment analysis"))
        self.button.setText(_translate("MainWindow", "Go!"))
        self.browserComboBox.setStatusTip(_translate("MainWindow", "Choose the browser you want to use"))
        self.browserComboBox.setCurrentText(_translate("MainWindow", "Select Browser"))
        self.browserComboBox.setItemText(0, _translate("MainWindow", "Select Browser"))
        self.browserComboBox.setItemText(1, _translate("MainWindow", "Chrome"))
        self.browserComboBox.setItemText(2, _translate("MainWindow", "Edge"))
        self.browserComboBox.setItemText(3, _translate("MainWindow", "Firefox"))
        self.browserComboBox.setItemText(4, _translate("MainWindow", "Safari"))
        self.browserComboBox.setItemText(5, _translate("MainWindow", "Brave"))
        self.browserComboBox.setItemText(6, _translate("MainWindow", "Opera"))
        self.emotHeader2.setText(_translate("MainWindow", "eMot"))
        self.results_button.setStatusTip(_translate("MainWindow", "Click to start the sentiment analysis"))
        self.results_button.setText(_translate("MainWindow", "Show Results!"))
        self.frame.setStatusTip(_translate("MainWindow", "Most Common Emotion"))
        self.commonTextEdit.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:10pt; font-weight:600; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.commonLabel.setText(_translate("MainWindow", "Most Common Emotion"))
        self.frame_2.setStatusTip(_translate("MainWindow", "Most Negative Website"))
        self.websiteTextEdit.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:10pt; font-weight:600; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.websiteLabel.setText(_translate("MainWindow", "Most Negative Website"))
        self.frame_3.setStatusTip(_translate("MainWindow", "Most Positive Sentence"))
        self.positiveTextEdit.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:9pt; font-weight:600; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.positiveLabel.setText(_translate("MainWindow", "Most Positive Sentence"))
        self.nextPageButton.setStatusTip(_translate("MainWindow", "Look at the next page of results"))
        self.nextPageButton.setText(_translate("MainWindow", "Next Page"))
        self.wordCloud.setText(_translate("MainWindow", "Loading WordCloud.."))
        self.previousPageButton.setText(_translate("MainWindow", "Previous Page"))
        self.frame_4.setStatusTip(_translate("MainWindow", "The sentence that showed the most fear"))
        self.fearTextEdit.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:9pt; font-weight:600; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:10pt;\"><br /></p></body></html>"))
        self.fearLabel.setText(_translate("MainWindow", "Most Fearful Sentence"))
        self.frame_5.setStatusTip(_translate("MainWindow", "The total amount of anger in all the sentences"))
        self.angerLabel.setText(_translate("MainWindow", "Anger Total"))
        self.angerTextEdit.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:10pt; font-weight:600; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.frame_6.setStatusTip(_translate("MainWindow", "The browser you chose"))
        self.browserUsedTextEdit.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:10pt; font-weight:600; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.browserUsedLabel.setText(_translate("MainWindow", "Browser Used"))
        self.dateFilterLabel.setStatusTip(_translate("MainWindow", "Bar Chart"))
        self.dateFilterLabel.setText(_translate("MainWindow", "Date Filter"))
        self.dateFiltrTextEdit.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:10pt; font-weight:600; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.actionpreferences.setText(_translate("MainWindow", "Preferences"))
        self.actionabout.setText(_translate("MainWindow", "about"))
        self.actionNew.setText(_translate("MainWindow", "New"))
        self.actionPreferences.setText(_translate("MainWindow", "Preferences"))
        self.actionAbout.setText(_translate("MainWindow", "About"))
import pyqt.resource_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
