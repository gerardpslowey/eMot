import sys

# flake8: noqa
from PyQt5 import QtCore, QtGui, QtWidgets

import pyqt.resource_rc


class Ui_Form:
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(510, 460)
        Form.setMinimumSize(QtCore.QSize(510, 460))
        Form.setMaximumSize(QtCore.QSize(510, 460))
        icon = QtGui.QIcon()
        icon.addPixmap(
            QtGui.QPixmap(":/newPrefix/icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off
        )
        Form.setWindowIcon(icon)
        Form.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.emotHeader_2 = QtWidgets.QLabel(Form)
        self.emotHeader_2.setGeometry(QtCore.QRect(130, 20, 241, 100))
        font = QtGui.QFont()
        font.setPointSize(40)
        font.setBold(False)
        font.setWeight(50)
        self.emotHeader_2.setFont(font)
        self.emotHeader_2.setAlignment(QtCore.Qt.AlignCenter)
        self.emotHeader_2.setObjectName("emotHeader_2")
        self.emptyBox_3 = QtWidgets.QLabel(Form)
        self.emptyBox_3.setGeometry(QtCore.QRect(20, 80, 471, 341))
        self.emptyBox_3.setStyleSheet("border: 1px solid rgb(165, 165, 165);")
        self.emptyBox_3.setText("")
        self.emptyBox_3.setObjectName("emptyBox_3")
        self.textEdit = QtWidgets.QTextEdit(Form)
        self.textEdit.setGeometry(QtCore.QRect(40, 120, 431, 251))
        self.textEdit.setReadOnly(True)
        self.textEdit.setObjectName("textEdit")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(40, 380, 431, 31))
        self.label.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.label.setStyleSheet("color: rgb(0, 0, 255);")
        self.label.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setWordWrap(False)
        self.label.setOpenExternalLinks(True)
        self.label.setObjectName("label")
        self.emptyBox_3.raise_()
        self.emotHeader_2.raise_()
        self.textEdit.raise_()
        self.label.raise_()

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "About"))
        self.emotHeader_2.setText(_translate("Form", "About"))
        self.textEdit.setHtml(
            _translate(
                "Form",
                '<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0//EN" "http://www.w3.org/TR/REC-html40/strict.dtd">\n'
                '<html><head><meta name="qrichtext" content="1" /><style type="text/css">\n'
                "p, li { white-space: pre-wrap; }\n"
                "</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
                '<p align="justify" style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-size:8pt;">eMot aims to provide users with insight into the material they have viewed online. This is achieved by collecting the users browsing history based on their browser choice and date filter choice. The browsers supported by eMot include Chrome, Edge, Firefox, Safari, Brave, and Opera. Each URL of the browsing history is then rendered in a lightweight browser and the textual material is scraped (extracted) from the web page. </span></p>\n'
                '<p align="justify" style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8pt;"><br /></p>\n'
                '<p align="justify" style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-size:8pt;">The text from these websites are processed and classified to give you an indication of what sort of material you are reading. It is beneficial to know whether you are consuming media that has primarily angry emotions or happy emotions. Your browsing history is never stored at any point.</span></p>\n'
                '<p align="justify" style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8pt;"><br /></p>\n'
                '<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">Find out more at: </p></body></html>',
            )
        )
        self.label.setStatusTip(_translate("Form", "Open gitlab repository"))
        self.label.setText(
            _translate(
                "Form",
                '<a href="https://gitlab.computing.dcu.ie/sloweyg2/2021-ca400-gslowey-msavage"> https://gitlab.computing.dcu.ie/sloweyg2/2021-ca400-gslowey-msavage </a>',
            )
        )


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
