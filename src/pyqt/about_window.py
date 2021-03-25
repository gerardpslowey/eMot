# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'about_window.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(510, 460)
        Form.setMinimumSize(QtCore.QSize(510, 460))
        Form.setMaximumSize(QtCore.QSize(510, 460))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/newPrefix/resources/icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Form.setWindowIcon(icon)
        Form.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.emotHeader_2 = QtWidgets.QLabel(Form)
        self.emotHeader_2.setGeometry(QtCore.QRect(150, 20, 221, 100))
        font = QtGui.QFont()
        font.setPointSize(40)
        font.setBold(False)
        font.setWeight(50)
        self.emotHeader_2.setFont(font)
        self.emotHeader_2.setAlignment(QtCore.Qt.AlignCenter)
        self.emotHeader_2.setObjectName("emotHeader_2")
        self.aboutText_2 = QtWidgets.QLabel(Form)
        self.aboutText_2.setGeometry(QtCore.QRect(100, 150, 311, 251))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.aboutText_2.setFont(font)
        self.aboutText_2.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.aboutText_2.setWordWrap(False)
        self.aboutText_2.setOpenExternalLinks(False)
        self.aboutText_2.setObjectName("aboutText_2")
        self.gitlabLink_2 = QtWidgets.QLabel(Form)
        self.gitlabLink_2.setGeometry(QtCore.QRect(40, 380, 431, 31))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.gitlabLink_2.setFont(font)
        self.gitlabLink_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.gitlabLink_2.setAlignment(QtCore.Qt.AlignCenter)
        self.gitlabLink_2.setOpenExternalLinks(True)
        self.gitlabLink_2.setObjectName("gitlabLink_2")
        self.emptyBox_3 = QtWidgets.QLabel(Form)
        self.emptyBox_3.setGeometry(QtCore.QRect(20, 80, 471, 341))
        self.emptyBox_3.setStyleSheet("border: 1px solid rgb(165, 165, 165);\n"
"background-color: rgb(255, 255, 255);\n"
"")
        self.emptyBox_3.setText("")
        self.emptyBox_3.setObjectName("emptyBox_3")
        self.emptyBox_3.raise_()
        self.emotHeader_2.raise_()
        self.aboutText_2.raise_()
        self.gitlabLink_2.raise_()

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "AboutWindow"))
        self.emotHeader_2.setText(_translate("Form", "About"))
        self.aboutText_2.setText(_translate("Form", "eMot is a sentiment analyis application that \n"
"takes your browsing history and extracts the \n"
" negativity and positivity of the different URLs visited.\n"
"\n"
"All browsing history is never stored anywhere. \n"
"We scrape the text from these websites and \n"
"give you a indication of what sort of material \n"
"you are reading.\n"
"\n"
"It is beneficial to know whether you are \n"
"consuming media that has hateful emotions, \n"
"sad emotions, or happy emotions.\n"
"\n"
"Find out more at: "))
        self.gitlabLink_2.setText(_translate("Form", "<a href =\"https://gitlab.computing.dcu.ie/sloweyg2/2021-ca400-gslowey-msavage\">https://gitlab.computing.dcu.ie/sloweyg2/2021-ca400-gslowey-msavage</a>"))
import pyqt.resource_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
