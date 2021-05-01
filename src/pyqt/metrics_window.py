import sys

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtChart import QChartView

import pyqt.resource_rc

# flake8: noqa


class Ui_MetricsDashboard:
    def setupUi(self, MetricsDashboard):
        MetricsDashboard.setObjectName("MetricsDashboard")
        MetricsDashboard.resize(1150, 746)
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
        self.verticalLayout_18 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_18.setObjectName("verticalLayout_18")
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
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.chartPage)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.page1Layout = QtWidgets.QVBoxLayout()
        self.page1Layout.setObjectName("page1Layout")
        self.chartTextLayout = QtWidgets.QHBoxLayout()
        self.chartTextLayout.setObjectName("chartTextLayout")
        self.page1ChartsLayout = QtWidgets.QVBoxLayout()
        self.page1ChartsLayout.setObjectName("page1ChartsLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.splitChart = QChartView(self.chartPage)
        self.splitChart.setObjectName("splitChart")
        self.verticalLayout_2.addWidget(self.splitChart)
        self.page1ChartsLayout.addLayout(self.verticalLayout_2)
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.lineChart = QChartView(self.chartPage)
        self.lineChart.setObjectName("lineChart")
        self.verticalLayout_6.addWidget(self.lineChart)
        self.page1ChartsLayout.addLayout(self.verticalLayout_6)
        self.chartTextLayout.addLayout(self.page1ChartsLayout)
        self.page1TextLayout = QtWidgets.QVBoxLayout()
        self.page1TextLayout.setContentsMargins(-1, 30, -1, -1)
        self.page1TextLayout.setObjectName("page1TextLayout")
        self.posSentencesLayout = QtWidgets.QVBoxLayout()
        self.posSentencesLayout.setObjectName("posSentencesLayout")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.posSentencesLabel = QtWidgets.QLabel(self.chartPage)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.posSentencesLabel.setFont(font)
        self.posSentencesLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.posSentencesLabel.setObjectName("posSentencesLabel")
        self.verticalLayout_7.addWidget(self.posSentencesLabel)
        self.posSentencesLayout.addLayout(self.verticalLayout_7)
        self.verticalLayout_8 = QtWidgets.QVBoxLayout()
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.scrollArea = QtWidgets.QScrollArea(self.chartPage)
        self.scrollArea.setHorizontalScrollBarPolicy(
            QtCore.Qt.ScrollBarAlwaysOff)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 360, 499))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout_19 = QtWidgets.QVBoxLayout(
            self.scrollAreaWidgetContents)
        self.verticalLayout_19.setObjectName("verticalLayout_19")
        self.positiveSentEdit = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.positiveSentEdit.setFont(font)
        self.positiveSentEdit.setText("")
        self.positiveSentEdit.setAlignment(
            QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)
        self.positiveSentEdit.setWordWrap(True)
        self.positiveSentEdit.setObjectName("positiveSentEdit")
        self.verticalLayout_19.addWidget(self.positiveSentEdit)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout_8.addWidget(self.scrollArea)
        self.posSentencesLayout.addLayout(self.verticalLayout_8)
        self.page1TextLayout.addLayout(self.posSentencesLayout)
        self.page1TextLayout.setStretch(0, 3)
        self.chartTextLayout.addLayout(self.page1TextLayout)
        self.chartTextLayout.setStretch(0, 2)
        self.chartTextLayout.setStretch(1, 1)
        self.page1Layout.addLayout(self.chartTextLayout)
        self.buttonLayout = QtWidgets.QHBoxLayout()
        self.buttonLayout.setObjectName("buttonLayout")
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
        self.buttonLayout.addWidget(self.nextPageButton)
        self.page1Layout.addLayout(self.buttonLayout)
        self.horizontalLayout_4.addLayout(self.page1Layout)
        self.stackedWidget.addWidget(self.chartPage)
        self.chartPage2 = QtWidgets.QWidget()
        self.chartPage2.setObjectName("chartPage2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.chartPage2)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.page2Layout = QtWidgets.QVBoxLayout()
        self.page2Layout.setObjectName("page2Layout")
        self.page2TextChartLayout = QtWidgets.QHBoxLayout()
        self.page2TextChartLayout.setObjectName("page2TextChartLayout")
        self.page2ChartsLayout = QtWidgets.QVBoxLayout()
        self.page2ChartsLayout.setObjectName("page2ChartsLayout")
        self.verticalLayout_23 = QtWidgets.QVBoxLayout()
        self.verticalLayout_23.setObjectName("verticalLayout_23")
        self.pieChart = QChartView(self.chartPage2)
        self.pieChart.setObjectName("pieChart")
        self.verticalLayout_23.addWidget(self.pieChart)
        self.page2ChartsLayout.addLayout(self.verticalLayout_23)
        self.verticalLayout_24 = QtWidgets.QVBoxLayout()
        self.verticalLayout_24.setObjectName("verticalLayout_24")
        self.barChart = QChartView(self.chartPage2)
        self.barChart.setObjectName("barChart")
        self.verticalLayout_24.addWidget(self.barChart)
        self.page2ChartsLayout.addLayout(self.verticalLayout_24)
        self.page2ChartsLayout.setStretch(0, 1)
        self.page2ChartsLayout.setStretch(1, 1)
        self.page2TextChartLayout.addLayout(self.page2ChartsLayout)
        self.page2TextLayout = QtWidgets.QVBoxLayout()
        self.page2TextLayout.setContentsMargins(-1, 25, -1, -1)
        self.page2TextLayout.setObjectName("page2TextLayout")
        self.verticalLayout_21 = QtWidgets.QVBoxLayout()
        self.verticalLayout_21.setObjectName("verticalLayout_21")
        self.negSentenceLabel = QtWidgets.QLabel(self.chartPage2)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.negSentenceLabel.setFont(font)
        self.negSentenceLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.negSentenceLabel.setObjectName("negSentenceLabel")
        self.verticalLayout_21.addWidget(self.negSentenceLabel)
        self.page2TextLayout.addLayout(self.verticalLayout_21)
        self.verticalLayout_22 = QtWidgets.QVBoxLayout()
        self.verticalLayout_22.setObjectName("verticalLayout_22")
        self.scrollArea_2 = QtWidgets.QScrollArea(self.chartPage2)
        self.scrollArea_2.setHorizontalScrollBarPolicy(
            QtCore.Qt.ScrollBarAlwaysOff)
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollArea_2.setObjectName("scrollArea_2")
        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(
            QtCore.QRect(0, 0, 362, 504))
        self.scrollAreaWidgetContents_2.setObjectName(
            "scrollAreaWidgetContents_2")
        self.verticalLayout_25 = QtWidgets.QVBoxLayout(
            self.scrollAreaWidgetContents_2)
        self.verticalLayout_25.setObjectName("verticalLayout_25")
        self.negativeSentEdit = QtWidgets.QLabel(
            self.scrollAreaWidgetContents_2)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.negativeSentEdit.setFont(font)
        self.negativeSentEdit.setText("")
        self.negativeSentEdit.setAlignment(
            QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)
        self.negativeSentEdit.setWordWrap(True)
        self.negativeSentEdit.setObjectName("negativeSentEdit")
        self.verticalLayout_25.addWidget(self.negativeSentEdit)
        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)
        self.verticalLayout_22.addWidget(self.scrollArea_2)
        self.page2TextLayout.addLayout(self.verticalLayout_22)
        self.page2TextChartLayout.addLayout(self.page2TextLayout)
        self.page2TextChartLayout.setStretch(0, 2)
        self.page2TextChartLayout.setStretch(1, 1)
        self.page2Layout.addLayout(self.page2TextChartLayout)
        self.buttonLayout2 = QtWidgets.QHBoxLayout()
        self.buttonLayout2.setObjectName("buttonLayout2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.previousPage2Button = QtWidgets.QPushButton(self.chartPage2)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred,
            QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.previousPage2Button.sizePolicy().hasHeightForWidth())
        self.previousPage2Button.setSizePolicy(sizePolicy)
        self.previousPage2Button.setMinimumSize(QtCore.QSize(200, 75))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.previousPage2Button.setFont(font)
        self.previousPage2Button.setCursor(
            QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.previousPage2Button.setStyleSheet("background-color: rgb(255, 125, 102);\n"
                                               "color: rgb(255, 255, 255);\n"
                                               "border-radius: 10px;")
        self.previousPage2Button.setObjectName("previousPage2Button")
        self.horizontalLayout_3.addWidget(self.previousPage2Button)
        self.buttonLayout2.addLayout(self.horizontalLayout_3)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.nextPage2Button = QtWidgets.QPushButton(self.chartPage2)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred,
            QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.nextPage2Button.sizePolicy().hasHeightForWidth())
        self.nextPage2Button.setSizePolicy(sizePolicy)
        self.nextPage2Button.setMinimumSize(QtCore.QSize(200, 75))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.nextPage2Button.setFont(font)
        self.nextPage2Button.setCursor(
            QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.nextPage2Button.setStyleSheet("background-color: rgb(103, 171, 159);\n"
                                           "color: rgb(255, 255, 255);\n"
                                           "border-radius: 10px;")
        self.nextPage2Button.setObjectName("nextPage2Button")
        self.horizontalLayout.addWidget(self.nextPage2Button)
        self.buttonLayout2.addLayout(self.horizontalLayout)
        self.page2Layout.addLayout(self.buttonLayout2)
        self.horizontalLayout_2.addLayout(self.page2Layout)
        self.stackedWidget.addWidget(self.chartPage2)
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
        self.verticalLayout_10.setContentsMargins(25, 0, 25, 0)
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
        self.verticalLayout_14.setContentsMargins(25, 0, 25, 0)
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
        self.textButtonLayout = QtWidgets.QVBoxLayout()
        self.textButtonLayout.setObjectName("textButtonLayout")
        self.paramsLayout = QtWidgets.QHBoxLayout()
        self.paramsLayout.setObjectName("paramsLayout")
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
        self.paramsLayout.addLayout(self.pLayout)
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
        self.paramsLayout.addLayout(self.nLayout)
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
        self.paramsLayout.addLayout(self.bLayout)
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
        self.paramsLayout.addLayout(self.dLayout)
        self.textButtonLayout.addLayout(self.paramsLayout)
        self.buttonLayout3 = QtWidgets.QVBoxLayout()
        self.buttonLayout3.setContentsMargins(0, 0, 0, 0)
        self.buttonLayout3.setObjectName("buttonLayout3")
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
        self.buttonLayout3.addWidget(self.previousPageButton)
        self.textButtonLayout.addLayout(self.buttonLayout3)
        self.verticalLayout_13.addLayout(self.textButtonLayout)
        self.verticalLayout_15.addLayout(self.verticalLayout_13)
        self.stackedWidget.addWidget(self.wordCloudPage)
        self.verticalLayout_18.addWidget(self.stackedWidget)
        MetricsDashboard.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MetricsDashboard)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1150, 26))
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
        self.lineChart.setStatusTip(
            _translate(
                "MetricsDashboard",
                "Line Chart showing the largest confidence level agreed on by the two classifiers."))
        self.posSentencesLabel.setText(
            _translate(
                "MetricsDashboard",
                "Most Positive Sentence Examples"))
        self.nextPageButton.setStatusTip(
            _translate(
                "MetricsDashboard",
                "Go to the next page"))
        self.nextPageButton.setText(
            _translate(
                "MetricsDashboard",
                "Next Page"))
        self.pieChart.setStatusTip(
            _translate(
                "MetricsDashboard",
                "Pie Chart showing the total amount of each emotion seen while scraping."))
        self.barChart.setStatusTip(
            _translate(
                "MetricsDashboard",
                "Bar Chart showing the most visited sites."))
        self.negSentenceLabel.setText(
            _translate(
                "MetricsDashboard",
                "Most Negative Sentence Examples"))
        self.previousPage2Button.setStatusTip(_translate(
            "MetricsDashboard", "Go to the previous page"))
        self.previousPage2Button.setText(
            _translate("MetricsDashboard", "Previous Page"))
        self.nextPage2Button.setStatusTip(
            _translate(
                "MetricsDashboard",
                "Go to the next page"))
        self.nextPage2Button.setText(
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
        self.posSiteLabel.setText(
            _translate(
                "MetricsDashboard",
                "Most Positive Site"))
        self.posSiteEdit.setStatusTip(
            _translate(
                "MetricsDashboard",
                "Click here to open the most positive website in your browser."))
        self.posSiteEdit.setText(_translate("MetricsDashboard", "Here"))
        self.negSiteLabel.setText(
            _translate(
                "MetricsDashboard",
                "Most Negative Site"))
        self.negSiteEdit.setStatusTip(
            _translate(
                "MetricsDashboard",
                "Click here to open the most negative website in your browser."))
        self.negSiteEdit.setText(_translate("MetricsDashboard", "Here"))
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
