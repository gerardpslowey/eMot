import sys

from PyQt5 import QtCore, QtGui, QtWidgets

import pyqt.resource_rc

# flake8: noqa


class Ui_Form:
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(554, 441)
        icon = QtGui.QIcon()
        icon.addPixmap(
            QtGui.QPixmap(":/newPrefix/icon.png"),
            QtGui.QIcon.Normal,
            QtGui.QIcon.Off)
        Form.setWindowIcon(icon)
        Form.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.tagLabel = QtWidgets.QLabel(Form)
        self.tagLabel.setGeometry(QtCore.QRect(50, 205, 251, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.tagLabel.setFont(font)
        self.tagLabel.setObjectName("tagLabel")
        self.urlLabel = QtWidgets.QLabel(Form)
        self.urlLabel.setGeometry(QtCore.QRect(50, 310, 251, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.urlLabel.setFont(font)
        self.urlLabel.setObjectName("urlLabel")
        self.blacklistInfo = QtWidgets.QLabel(Form)
        self.blacklistInfo.setGeometry(QtCore.QRect(50, 100, 441, 71))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.blacklistInfo.setFont(font)
        self.blacklistInfo.setStyleSheet("")
        self.blacklistInfo.setAlignment(QtCore.Qt.AlignCenter)
        self.blacklistInfo.setWordWrap(True)
        self.blacklistInfo.setObjectName("blacklistInfo")
        self.blacklistHeader = QtWidgets.QLabel(Form)
        self.blacklistHeader.setGeometry(QtCore.QRect(140, 20, 271, 71))
        font = QtGui.QFont()
        font.setPointSize(40)
        self.blacklistHeader.setFont(font)
        self.blacklistHeader.setStyleSheet("")
        self.blacklistHeader.setObjectName("blacklistHeader")
        self.emptyBox_3 = QtWidgets.QLabel(Form)
        self.emptyBox_3.setGeometry(QtCore.QRect(30, 60, 491, 351))
        self.emptyBox_3.setStyleSheet("border: 1px solid rgb(165, 165, 165);\n"
                                      "")
        self.emptyBox_3.setText("")
        self.emptyBox_3.setObjectName("emptyBox_3")
        self.tagEdit = QtWidgets.QPlainTextEdit(Form)
        self.tagEdit.setGeometry(QtCore.QRect(50, 230, 321, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.tagEdit.setFont(font)
        self.tagEdit.setObjectName("tagEdit")
        self.addTagButton = QtWidgets.QPushButton(Form)
        self.addTagButton.setGeometry(QtCore.QRect(380, 230, 51, 41))
        self.addTagButton.setCursor(
            QtGui.QCursor(
                QtCore.Qt.PointingHandCursor))
        self.addTagButton.setStyleSheet("background-color: rgb(103, 171, 159);\n"
                                        "color: rgb(255, 255, 255);")
        self.addTagButton.setObjectName("addTagButton")
        self.deleteTagButton = QtWidgets.QPushButton(Form)
        self.deleteTagButton.setGeometry(QtCore.QRect(440, 230, 51, 41))
        self.deleteTagButton.setCursor(
            QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.deleteTagButton.setStyleSheet("background-color: rgb(255, 125, 102);\n"
                                           "color: rgb(255, 255, 255);")
        self.deleteTagButton.setObjectName("deleteTagButton")
        self.urlEdit = QtWidgets.QPlainTextEdit(Form)
        self.urlEdit.setGeometry(QtCore.QRect(50, 340, 321, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.urlEdit.setFont(font)
        self.urlEdit.setObjectName("urlEdit")
        self.addUrlButton = QtWidgets.QPushButton(Form)
        self.addUrlButton.setGeometry(QtCore.QRect(380, 340, 51, 41))
        self.addUrlButton.setCursor(
            QtGui.QCursor(
                QtCore.Qt.PointingHandCursor))
        self.addUrlButton.setStyleSheet("background-color: rgb(103, 171, 159);\n"
                                        "color: rgb(255, 255, 255);")
        self.addUrlButton.setObjectName("addUrlButton")
        self.deleteUrlButton = QtWidgets.QPushButton(Form)
        self.deleteUrlButton.setGeometry(QtCore.QRect(440, 340, 51, 41))
        self.deleteUrlButton.setCursor(
            QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.deleteUrlButton.setStyleSheet("background-color: rgb(255, 125, 102);\n"
                                           "color: rgb(255, 255, 255);")
        self.deleteUrlButton.setObjectName("deleteUrlButton")
        self.emptyBox_3.raise_()
        self.tagLabel.raise_()
        self.urlLabel.raise_()
        self.blacklistInfo.raise_()
        self.blacklistHeader.raise_()
        self.tagEdit.raise_()
        self.addTagButton.raise_()
        self.deleteTagButton.raise_()
        self.urlEdit.raise_()
        self.addUrlButton.raise_()
        self.deleteUrlButton.raise_()

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Preferences"))
        self.tagLabel.setText(
            _translate(
                "Form",
                "Add a HTML Tag to the blacklist "))
        self.urlLabel.setText(
            _translate(
                "Form",
                "Add a URL to the blacklist "))
        self.blacklistInfo.setText(
            _translate(
                "Form",
                "Add a URL so that it is not scraped from your browsing history. Or add a HTML tag so that it is not scraped!"))
        self.blacklistHeader.setText(_translate("Form", "Blacklists"))
        self.addTagButton.setText(_translate("Form", "Add"))
        self.deleteTagButton.setText(_translate("Form", "Delete"))
        self.addUrlButton.setText(_translate("Form", "Add"))
        self.deleteUrlButton.setText(_translate("Form", "Delete"))


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
