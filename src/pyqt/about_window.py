import sys

from PyQt5 import QtCore, QtGui, QtWidgets

import pyqt.resource_rc

# flake8: noqa


class Ui_About:
    def setupUi(self, About):
        About.setObjectName("About")
        About.resize(510, 460)
        About.setMinimumSize(QtCore.QSize(510, 460))
        icon = QtGui.QIcon()
        icon.addPixmap(
            QtGui.QPixmap(":/newPrefix/icon.png"),
            QtGui.QIcon.Normal,
            QtGui.QIcon.Off)
        About.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(About)
        self.centralwidget.setStyleSheet(
            "background-color: rgb(255, 255, 255);")
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        spacerItem = QtWidgets.QSpacerItem(
            20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.emotHeader_2 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(40)
        font.setBold(False)
        font.setWeight(50)
        self.emotHeader_2.setFont(font)
        self.emotHeader_2.setAlignment(QtCore.Qt.AlignCenter)
        self.emotHeader_2.setObjectName("emotHeader_2")
        self.verticalLayout.addWidget(self.emotHeader_2)
        self.verticalLayout_4.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setScaledContents(True)
        self.label_2.setWordWrap(True)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        self.verticalLayout_4.addLayout(self.verticalLayout_2)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.label.setStyleSheet("color: rgb(0, 0, 255);")
        self.label.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setWordWrap(False)
        self.label.setOpenExternalLinks(True)
        self.label.setObjectName("label")
        self.verticalLayout_3.addWidget(self.label)
        self.verticalLayout_4.addLayout(self.verticalLayout_3)
        self.verticalLayout_4.setStretch(0, 1)
        self.verticalLayout_4.setStretch(1, 2)
        self.verticalLayout_4.setStretch(2, 1)
        self.verticalLayout_5.addLayout(self.verticalLayout_4)
        About.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(About)
        self.statusbar.setObjectName("statusbar")
        About.setStatusBar(self.statusbar)

        self.retranslateUi(About)
        QtCore.QMetaObject.connectSlotsByName(About)

    def retranslateUi(self, About):
        _translate = QtCore.QCoreApplication.translate
        About.setWindowTitle(_translate("About", "About eMot"))
        self.emotHeader_2.setText(_translate("About", "About"))
        self.label_2.setText(_translate("About", "eMot aims to provide users with insight into the material they have viewed online. This is achieved by collecting the users browsing history based on their browser choice and date filter choice. The browsers supported by eMot include Chrome, Edge, Firefox, Safari, Brave, and Opera. Each URL of the browsing history is then rendered in a lightweight browser and the textual material is scraped (extracted) from the web page. \n"
                                        "\n"
                                        "\n"
                                        "The text from these websites are processed and classified to give you an indication of what sort of material you are reading. It is beneficial to know whether you are consuming media that has primarily angry emotions or happy emotions. Your browsing history is never stored at any point.\n"
                                        "\n"
                                        "\n"
                                        "Find out more at:"))
        self.label.setStatusTip(_translate("About", "Open the user manual."))
        self.label.setText(
            _translate(
                "About",
                "<html><head/><body><p align=\"center\"><a href=\"https://docs.google.com/document/d/1qBCJQA-CYdJfvuIIAPbABQMXIWXqyd_84ktYM9sTRZs/edit?usp=sharing\"><span style=\" text-decoration: underline; color:#0000ff;\">eMot User Manual </span></a></p></body></html>"))


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    About = QtWidgets.QMainWindow()
    ui = Ui_About()
    ui.setupUi(About)
    About.show()
    sys.exit(app.exec_())
