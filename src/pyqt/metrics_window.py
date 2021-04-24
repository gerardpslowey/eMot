# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'metrics.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MetricsDashboard(object):
    def setupUi(self, MetricsDashboard):
        MetricsDashboard.setObjectName("MetricsDashboard")
        MetricsDashboard.resize(1144, 849)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MetricsDashboard.sizePolicy().hasHeightForWidth())
        MetricsDashboard.setSizePolicy(sizePolicy)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/newPrefix/icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MetricsDashboard.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MetricsDashboard)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.stackedWidget.sizePolicy().hasHeightForWidth())
        self.stackedWidget.setSizePolicy(sizePolicy)
        self.stackedWidget.setStyleSheet("background-color: rgb(255, 255, 255);")
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
        self.verticalLayout_6.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, -1)
        self.verticalLayout_6.setSpacing(7)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.nextPageButton = QtWidgets.QPushButton(self.chartPage)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.nextPageButton.sizePolicy().hasHeightForWidth())
        self.nextPageButton.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.nextPageButton.setFont(font)
        self.nextPageButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
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
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.wordCloudPage)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.cloudTextLayout = QtWidgets.QHBoxLayout()
        self.cloudTextLayout.setObjectName("cloudTextLayout")
        self.cloudLayout = QtWidgets.QVBoxLayout()
        self.cloudLayout.setContentsMargins(-1, -1, -1, 50)
        self.cloudLayout.setObjectName("cloudLayout")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label = QtWidgets.QLabel(self.wordCloudPage)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout_5.addWidget(self.label)
        self.cloudLayout.addLayout(self.verticalLayout_5)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.wordCloud = QtWidgets.QLabel(self.wordCloudPage)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.wordCloud.sizePolicy().hasHeightForWidth())
        self.wordCloud.setSizePolicy(sizePolicy)
        self.wordCloud.setMaximumSize(QtCore.QSize(1050, 750))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.wordCloud.setFont(font)
        self.wordCloud.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.wordCloud.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 255, 255, 255), stop:1 rgba(103, 171, 159,255));\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 10px;")
        self.wordCloud.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.wordCloud.setScaledContents(True)
        self.wordCloud.setAlignment(QtCore.Qt.AlignCenter)
        self.wordCloud.setIndent(4)
        self.wordCloud.setObjectName("wordCloud")
        self.horizontalLayout_3.addWidget(self.wordCloud)
        self.horizontalLayout_3.setStretch(0, 6)
        self.cloudLayout.addLayout(self.horizontalLayout_3)
        self.cloudLayout.setStretch(0, 1)
        self.cloudLayout.setStretch(1, 4)
        self.cloudTextLayout.addLayout(self.cloudLayout)
        self.textLayout = QtWidgets.QVBoxLayout()
        self.textLayout.setContentsMargins(-1, 100, -1, -1)
        self.textLayout.setObjectName("textLayout")
        self.bLayout = QtWidgets.QVBoxLayout()
        self.bLayout.setObjectName("bLayout")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout()
        self.verticalLayout_10.setContentsMargins(-1, 0, -1, 0)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.browserUsed = QtWidgets.QLabel(self.wordCloudPage)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.browserUsed.setFont(font)
        self.browserUsed.setAlignment(QtCore.Qt.AlignCenter)
        self.browserUsed.setObjectName("browserUsed")
        self.verticalLayout_10.addWidget(self.browserUsed)
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
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_11.addItem(spacerItem)
        self.verticalLayout_10.addLayout(self.verticalLayout_11)
        self.bLayout.addLayout(self.verticalLayout_10)
        self.textLayout.addLayout(self.bLayout)
        self.dLayout = QtWidgets.QVBoxLayout()
        self.dLayout.setObjectName("dLayout")
        self.verticalLayout_13 = QtWidgets.QVBoxLayout()
        self.verticalLayout_13.setObjectName("verticalLayout_13")
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
        self.verticalLayout_13.addLayout(self.verticalLayout_20)
        self.dateUsedEdit = QtWidgets.QLabel(self.wordCloudPage)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.dateUsedEdit.setFont(font)
        self.dateUsedEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.dateUsedEdit.setObjectName("dateUsedEdit")
        self.verticalLayout_13.addWidget(self.dateUsedEdit)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_13.addItem(spacerItem1)
        self.dLayout.addLayout(self.verticalLayout_13)
        self.textLayout.addLayout(self.dLayout)
        self.sLayout = QtWidgets.QVBoxLayout()
        self.sLayout.setObjectName("sLayout")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout()
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.sitesLabel = QtWidgets.QLabel(self.wordCloudPage)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.sitesLabel.setFont(font)
        self.sitesLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.sitesLabel.setObjectName("sitesLabel")
        self.verticalLayout_9.addWidget(self.sitesLabel)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.sitesVisitedEdit = QtWidgets.QLabel(self.wordCloudPage)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.sitesVisitedEdit.setFont(font)
        self.sitesVisitedEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.sitesVisitedEdit.setObjectName("sitesVisitedEdit")
        self.verticalLayout.addWidget(self.sitesVisitedEdit)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem2)
        self.verticalLayout_9.addLayout(self.verticalLayout)
        self.sLayout.addLayout(self.verticalLayout_9)
        self.textLayout.addLayout(self.sLayout)
        self.cloudTextLayout.addLayout(self.textLayout)
        self.cloudTextLayout.setStretch(0, 4)
        self.cloudTextLayout.setStretch(1, 1)
        self.verticalLayout_3.addLayout(self.cloudTextLayout)
        self.buttonLayout = QtWidgets.QVBoxLayout()
        self.buttonLayout.setContentsMargins(0, 0, 0, 0)
        self.buttonLayout.setObjectName("buttonLayout")
        self.previousPageButton = QtWidgets.QPushButton(self.wordCloudPage)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.previousPageButton.sizePolicy().hasHeightForWidth())
        self.previousPageButton.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.previousPageButton.setFont(font)
        self.previousPageButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.previousPageButton.setStyleSheet("background-color: rgb(255, 125, 102);\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 10px;")
        self.previousPageButton.setObjectName("previousPageButton")
        self.buttonLayout.addWidget(self.previousPageButton)
        self.verticalLayout_3.addLayout(self.buttonLayout)
        self.verticalLayout_3.setStretch(0, 6)
        self.verticalLayout_3.setStretch(1, 1)
        self.verticalLayout_4.addLayout(self.verticalLayout_3)
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
        self.stackedWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MetricsDashboard)

    def retranslateUi(self, MetricsDashboard):
        _translate = QtCore.QCoreApplication.translate
        MetricsDashboard.setWindowTitle(_translate("MetricsDashboard", "Metrics Dashboard"))
        self.nextPageButton.setStatusTip(_translate("MetricsDashboard", "Go to the next page"))
        self.nextPageButton.setText(_translate("MetricsDashboard", "Next Page"))
        self.label.setText(_translate("MetricsDashboard", "Strongest Emotions WordCloud"))
        self.wordCloud.setText(_translate("MetricsDashboard", "Loading WordCloud..."))
        self.browserUsed.setText(_translate("MetricsDashboard", "Browser Used"))
        self.browserUsedEdit.setText(_translate("MetricsDashboard", "Opera"))
        self.dateUsed.setText(_translate("MetricsDashboard", "Date Filter Used"))
        self.dateUsedEdit.setText(_translate("MetricsDashboard", "All"))
        self.sitesLabel.setText(_translate("MetricsDashboard", "Sites Visited"))
        self.sitesVisitedEdit.setText(_translate("MetricsDashboard", "6 Sites"))
        self.previousPageButton.setStatusTip(_translate("MetricsDashboard", "Go to the previous page"))
        self.previousPageButton.setText(_translate("MetricsDashboard", "Previous Page"))
from PyQt5.QtChart import QChartView
import pyqt.resource_rc
# flake8: noqa


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MetricsDashboard = QtWidgets.QMainWindow()
    ui = Ui_MetricsDashboard()
    ui.setupUi(MetricsDashboard)
    MetricsDashboard.show()
    sys.exit(app.exec_())
