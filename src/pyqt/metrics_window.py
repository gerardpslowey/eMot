import sys

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtChart import QChartView

import pyqt.resource_rc

# flake8: noqa


class Ui_MetricsDashboard:
    def setupUi(self, MetricsDashboard):
        MetricsDashboard.setObjectName("MetricsDashboard")
        MetricsDashboard.resize(1144, 849)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred,
            QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            MetricsDashboard.sizePolicy().hasHeightForWidth())
        MetricsDashboard.setSizePolicy(sizePolicy)
        icon = QtGui.QIcon()
        icon.addPixmap(
            QtGui.QPixmap(":/newPrefix/icon.png"),
            QtGui.QIcon.Normal,
            QtGui.QIcon.Off)
        MetricsDashboard.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MetricsDashboard)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred,
            QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.stackedWidget.sizePolicy().hasHeightForWidth())
        self.stackedWidget.setSizePolicy(sizePolicy)
        self.stackedWidget.setStyleSheet(
            "background-color: rgb(255, 255, 255);")
        self.stackedWidget.setObjectName("stackedWidget")
        self.chartPage = QtWidgets.QWidget()
        self.chartPage.setObjectName("chartPage")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.chartPage)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(50, 0, 50, -1)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.splitChart = QChartView(self.chartPage)
        self.splitChart.setObjectName("splitChart")
        self.horizontalLayout.addWidget(self.splitChart)
        self.pieChart = QChartView(self.chartPage)
        self.pieChart.setObjectName("pieChart")
        self.horizontalLayout.addWidget(self.pieChart)
        self.verticalLayout_7.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setContentsMargins(50, -1, 50, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.lineChart = QChartView(self.chartPage)
        self.lineChart.setObjectName("lineChart")
        self.horizontalLayout_2.addWidget(self.lineChart)
        self.barChart = QChartView(self.chartPage)
        self.barChart.setObjectName("barChart")
        self.horizontalLayout_2.addWidget(self.barChart)
        self.verticalLayout_7.addLayout(self.horizontalLayout_2)
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setSizeConstraint(
            QtWidgets.QLayout.SetDefaultConstraint)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, -1)
        self.verticalLayout_6.setSpacing(7)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.nextPageButton = QtWidgets.QPushButton(self.chartPage)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred,
            QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.nextPageButton.sizePolicy().hasHeightForWidth())
        self.nextPageButton.setSizePolicy(sizePolicy)
        self.nextPageButton.setMinimumSize(QtCore.QSize(200, 75))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.nextPageButton.setFont(font)
        self.nextPageButton.setCursor(
            QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.nextPageButton.setStyleSheet("background-color: rgb(103, 171, 159);\n"
                                          "color: rgb(255, 255, 255);\n"
                                          "border-radius: 10px;")
        self.nextPageButton.setObjectName("nextPageButton")
        self.verticalLayout_6.addWidget(self.nextPageButton)
        self.verticalLayout_7.addLayout(self.verticalLayout_6)
        self.verticalLayout_7.setStretch(0, 4)
        self.verticalLayout_7.setStretch(1, 4)
        self.verticalLayout_7.setStretch(2, 1)
        self.verticalLayout_8.addLayout(self.verticalLayout_7)
        self.stackedWidget.addWidget(self.chartPage)
        self.wordCloudPage = QtWidgets.QWidget()
        self.wordCloudPage.setObjectName("wordCloudPage")
        self.verticalLayout_15 = QtWidgets.QVBoxLayout(self.wordCloudPage)
        self.verticalLayout_15.setObjectName("verticalLayout_15")
        self.verticalLayout_13 = QtWidgets.QVBoxLayout()
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self.wordcloudLayouts = QtWidgets.QHBoxLayout()
        self.wordcloudLayouts.setObjectName("wordcloudLayouts")
        self.posWordLayout = QtWidgets.QVBoxLayout()
        self.posWordLayout.setObjectName("posWordLayout")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        spacerItem = QtWidgets.QSpacerItem(
            20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_5.addItem(spacerItem)
        self.positiveLabel = QtWidgets.QLabel(self.wordCloudPage)
        self.positiveLabel.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.positiveLabel.setFont(font)
        self.positiveLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.positiveLabel.setObjectName("positiveLabel")
        self.verticalLayout_5.addWidget(self.positiveLabel)
        self.posWordLayout.addLayout(self.verticalLayout_5)
        self.verticalLayout_10 = QtWidgets.QVBoxLayout()
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.positiveWordcloud = QtWidgets.QLabel(self.wordCloudPage)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding,
            QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.positiveWordcloud.sizePolicy().hasHeightForWidth())
        self.positiveWordcloud.setSizePolicy(sizePolicy)
        self.positiveWordcloud.setBaseSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.positiveWordcloud.setFont(font)
        self.positiveWordcloud.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.positiveWordcloud.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 255, 255, 255), stop:1 rgba(103, 171, 159,255));\n"
                                             "color: rgb(255, 255, 255);\n"
                                             "border: 1px solid black;\n"
                                             "border-radius: 10px;")
        self.positiveWordcloud.setFrameShape(QtWidgets.QFrame.Panel)
        self.positiveWordcloud.setFrameShadow(QtWidgets.QFrame.Raised)
        self.positiveWordcloud.setLineWidth(1)
        self.positiveWordcloud.setScaledContents(True)
        self.positiveWordcloud.setAlignment(QtCore.Qt.AlignCenter)
        self.positiveWordcloud.setIndent(4)
        self.positiveWordcloud.setObjectName("positiveWordcloud")
        self.verticalLayout_10.addWidget(self.positiveWordcloud)
        self.posWordLayout.addLayout(self.verticalLayout_10)
        self.posWordLayout.setStretch(0, 1)
        self.posWordLayout.setStretch(1, 5)
        self.wordcloudLayouts.addLayout(self.posWordLayout)
        self.negWordLayout = QtWidgets.QVBoxLayout()
        self.negWordLayout.setObjectName("negWordLayout")
        self.verticalLayout_12 = QtWidgets.QVBoxLayout()
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        spacerItem1 = QtWidgets.QSpacerItem(
            20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_12.addItem(spacerItem1)
        self.negativeLabel = QtWidgets.QLabel(self.wordCloudPage)
        self.negativeLabel.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.negativeLabel.setFont(font)
        self.negativeLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.negativeLabel.setObjectName("negativeLabel")
        self.verticalLayout_12.addWidget(self.negativeLabel)
        self.negWordLayout.addLayout(self.verticalLayout_12)
        self.verticalLayout_14 = QtWidgets.QVBoxLayout()
        self.verticalLayout_14.setObjectName("verticalLayout_14")
        self.negativeWordcloud = QtWidgets.QLabel(self.wordCloudPage)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.negativeWordcloud.setFont(font)
        self.negativeWordcloud.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 255, 255, 255), stop:1 rgba(103, 171, 159,255));\n"
                                             "color: rgb(255, 255, 255);\n"
                                             "border: 1px solid black;\n"
                                             "border-radius: 10px;")
        self.negativeWordcloud.setAlignment(QtCore.Qt.AlignCenter)
        self.negativeWordcloud.setObjectName("negativeWordcloud")
        self.verticalLayout_14.addWidget(self.negativeWordcloud)
        self.negWordLayout.addLayout(self.verticalLayout_14)
        self.negWordLayout.setStretch(0, 1)
        self.negWordLayout.setStretch(1, 5)
        self.wordcloudLayouts.addLayout(self.negWordLayout)
        self.wordcloudLayouts.setStretch(0, 1)
        self.wordcloudLayouts.setStretch(1, 1)
        self.verticalLayout_13.addLayout(self.wordcloudLayouts)
        spacerItem2 = QtWidgets.QSpacerItem(
            20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_13.addItem(spacerItem2)
        self.textButtonLayout = QtWidgets.QVBoxLayout()
        self.textButtonLayout.setObjectName("textButtonLayout")
        self.textLayout = QtWidgets.QHBoxLayout()
        self.textLayout.setObjectName("textLayout")
        self.bLayout = QtWidgets.QVBoxLayout()
        self.bLayout.setObjectName("bLayout")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.browserUsed = QtWidgets.QLabel(self.wordCloudPage)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.browserUsed.setFont(font)
        self.browserUsed.setAlignment(QtCore.Qt.AlignCenter)
        self.browserUsed.setObjectName("browserUsed")
        self.verticalLayout_3.addWidget(self.browserUsed)
        self.bLayout.addLayout(self.verticalLayout_3)
        self.verticalLayout_11 = QtWidgets.QVBoxLayout()
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.browserUsedEdit = QtWidgets.QLabel(self.wordCloudPage)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.browserUsedEdit.setFont(font)
        self.browserUsedEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.browserUsedEdit.setObjectName("browserUsedEdit")
        self.verticalLayout_11.addWidget(self.browserUsedEdit)
        self.bLayout.addLayout(self.verticalLayout_11)
        self.textLayout.addLayout(self.bLayout)
        self.dLayout = QtWidgets.QVBoxLayout()
        self.dLayout.setObjectName("dLayout")
        self.verticalLayout_20 = QtWidgets.QVBoxLayout()
        self.verticalLayout_20.setObjectName("verticalLayout_20")
        self.dateUsed = QtWidgets.QLabel(self.wordCloudPage)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.dateUsed.setFont(font)
        self.dateUsed.setAlignment(QtCore.Qt.AlignCenter)
        self.dateUsed.setObjectName("dateUsed")
        self.verticalLayout_20.addWidget(self.dateUsed)
        self.dLayout.addLayout(self.verticalLayout_20)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.dateUsedEdit = QtWidgets.QLabel(self.wordCloudPage)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.dateUsedEdit.setFont(font)
        self.dateUsedEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.dateUsedEdit.setObjectName("dateUsedEdit")
        self.verticalLayout_4.addWidget(self.dateUsedEdit)
        self.dLayout.addLayout(self.verticalLayout_4)
        self.textLayout.addLayout(self.dLayout)
        self.nLayout = QtWidgets.QVBoxLayout()
        self.nLayout.setObjectName("nLayout")
        self.verticalLayout_17 = QtWidgets.QVBoxLayout()
        self.verticalLayout_17.setObjectName("verticalLayout_17")
        self.negSiteLabel = QtWidgets.QLabel(self.wordCloudPage)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.negSiteLabel.setFont(font)
        self.negSiteLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.negSiteLabel.setObjectName("negSiteLabel")
        self.verticalLayout_17.addWidget(self.negSiteLabel)
        self.nLayout.addLayout(self.verticalLayout_17)
        self.verticalLayout_16 = QtWidgets.QVBoxLayout()
        self.verticalLayout_16.setObjectName("verticalLayout_16")
        self.negSiteEdit = QtWidgets.QLabel(self.wordCloudPage)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.negSiteEdit.setFont(font)
        self.negSiteEdit.setStyleSheet("color: rgb(0, 0, 0);")
        self.negSiteEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.negSiteEdit.setOpenExternalLinks(True)
        self.negSiteEdit.setObjectName("negSiteEdit")
        self.verticalLayout_16.addWidget(self.negSiteEdit)
        self.nLayout.addLayout(self.verticalLayout_16)
        self.textLayout.addLayout(self.nLayout)
        self.pLayout = QtWidgets.QVBoxLayout()
        self.pLayout.setObjectName("pLayout")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout()
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.posSiteLabel = QtWidgets.QLabel(self.wordCloudPage)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.posSiteLabel.setFont(font)
        self.posSiteLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.posSiteLabel.setObjectName("posSiteLabel")
        self.verticalLayout_9.addWidget(self.posSiteLabel)
        self.pLayout.addLayout(self.verticalLayout_9)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.posSiteEdit = QtWidgets.QLabel(self.wordCloudPage)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.posSiteEdit.setFont(font)
        self.posSiteEdit.setStyleSheet("color: rgb(0, 0, 0);")
        self.posSiteEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.posSiteEdit.setOpenExternalLinks(True)
        self.posSiteEdit.setObjectName("posSiteEdit")
        self.verticalLayout.addWidget(self.posSiteEdit)
        self.pLayout.addLayout(self.verticalLayout)
        self.textLayout.addLayout(self.pLayout)
        self.textButtonLayout.addLayout(self.textLayout)
        self.buttonLayout = QtWidgets.QVBoxLayout()
        self.buttonLayout.setContentsMargins(0, 0, 0, 0)
        self.buttonLayout.setObjectName("buttonLayout")
        self.previousPageButton = QtWidgets.QPushButton(self.wordCloudPage)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred,
            QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.previousPageButton.sizePolicy().hasHeightForWidth())
        self.previousPageButton.setSizePolicy(sizePolicy)
        self.previousPageButton.setMinimumSize(QtCore.QSize(200, 75))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.previousPageButton.setFont(font)
        self.previousPageButton.setCursor(
            QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.previousPageButton.setStyleSheet("background-color: rgb(255, 125, 102);\n"
                                              "color: rgb(255, 255, 255);\n"
                                              "border-radius: 10px;")
        self.previousPageButton.setObjectName("previousPageButton")
        self.buttonLayout.addWidget(self.previousPageButton)
        self.textButtonLayout.addLayout(self.buttonLayout)
        self.verticalLayout_13.addLayout(self.textButtonLayout)
        self.verticalLayout_13.setStretch(0, 4)
        self.verticalLayout_13.setStretch(2, 1)
        self.verticalLayout_15.addLayout(self.verticalLayout_13)
        self.stackedWidget.addWidget(self.wordCloudPage)
        self.verticalLayout_2.addWidget(self.stackedWidget)
        MetricsDashboard.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MetricsDashboard)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1144, 26))
        self.menubar.setObjectName("menubar")
        MetricsDashboard.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MetricsDashboard)
        self.statusbar.setObjectName("statusbar")
        MetricsDashboard.setStatusBar(self.statusbar)

        self.retranslateUi(MetricsDashboard)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MetricsDashboard)

    def retranslateUi(self, MetricsDashboard):
        _translate = QtCore.QCoreApplication.translate
        MetricsDashboard.setWindowTitle(
            _translate(
                "MetricsDashboard",
                "Metrics Dashboard"))
        self.splitChart.setStatusTip(
            _translate(
                "MetricsDashboard",
                "Split Chart showing the different emotions seen per site."))
        self.pieChart.setStatusTip(
            _translate(
                "MetricsDashboard",
                "Pie Chart showing the total amount of each emotion seen while scraping."))
        self.lineChart.setStatusTip(
            _translate(
                "MetricsDashboard",
                "Line Chart showing the largest confidence level agreed on by the two classifiers."))
        self.barChart.setStatusTip(
            _translate(
                "MetricsDashboard",
                "Bar Chart showing the most visited sites."))
        self.nextPageButton.setStatusTip(
            _translate(
                "MetricsDashboard",
                "Go to the next page"))
        self.nextPageButton.setText(
            _translate(
                "MetricsDashboard",
                "Next Page"))
        self.positiveLabel.setText(
            _translate(
                "MetricsDashboard",
                "Positive Sentences Wordcloud"))
        self.positiveWordcloud.setStatusTip(
            _translate(
                "MetricsDashboard",
                "Most positive words found in the scraped sentences."))
        self.positiveWordcloud.setText(
            _translate(
                "MetricsDashboard",
                "Loading Wordcloud"))
        self.negativeLabel.setText(
            _translate(
                "MetricsDashboard",
                "Negative Sentences Wordcloud"))
        self.negativeWordcloud.setStatusTip(
            _translate(
                "MetricsDashboard",
                "Most negative words found in the scraped sentences."))
        self.negativeWordcloud.setText(
            _translate(
                "MetricsDashboard",
                "Loading Wordcloud"))
        self.browserUsed.setText(
            _translate(
                "MetricsDashboard",
                "Browser Used"))
        self.browserUsedEdit.setStatusTip(
            _translate(
                "MetricsDashboard",
                "Chosen browser in the dropdown menu."))
        self.browserUsedEdit.setText(_translate("MetricsDashboard", "Opera"))
        self.dateUsed.setText(
            _translate(
                "MetricsDashboard",
                "Date Filter Used"))
        self.dateUsedEdit.setStatusTip(
            _translate(
                "MetricsDashboard",
                "Chosen filter in the dropdown menu."))
        self.dateUsedEdit.setText(_translate("MetricsDashboard", "All"))
        self.negSiteLabel.setText(
            _translate(
                "MetricsDashboard",
                "Most Negative Site"))
        self.negSiteEdit.setStatusTip(
            _translate(
                "MetricsDashboard",
                "Click here to open the most negative website in your browser."))
        self.negSiteEdit.setText(_translate("MetricsDashboard", "Here"))
        self.posSiteLabel.setText(
            _translate(
                "MetricsDashboard",
                "Most Positive Site"))
        self.posSiteEdit.setStatusTip(
            _translate(
                "MetricsDashboard",
                "Click here to open the most positive website in your browser."))
        self.posSiteEdit.setText(_translate("MetricsDashboard", "Here"))
        self.previousPageButton.setStatusTip(_translate(
            "MetricsDashboard", "Go to the previous page"))
        self.previousPageButton.setText(
            _translate(
                "MetricsDashboard",
                "Previous Page"))


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MetricsDashboard = QtWidgets.QMainWindow()
    ui = Ui_MetricsDashboard()
    ui.setupUi(MetricsDashboard)
    MetricsDashboard.show()
    sys.exit(app.exec_())
