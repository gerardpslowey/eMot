import sys

from PyQt5 import QtCore, QtGui, QtWidgets

import pyqt.resource_rc

# flake8: noqa


class Ui_browserDialog:
    def setupUi(self, browserDialog):
        browserDialog.setObjectName("browserDialog")
        browserDialog.resize(417, 161)
        browserDialog.setMinimumSize(QtCore.QSize(417, 161))
        browserDialog.setMaximumSize(QtCore.QSize(417, 161))
        icon = QtGui.QIcon()
        icon.addPixmap(
            QtGui.QPixmap(":/newPrefix/icon.png"),
            QtGui.QIcon.Normal,
            QtGui.QIcon.Off)
        browserDialog.setWindowIcon(icon)
        browserDialog.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label = QtWidgets.QLabel(browserDialog)
        self.label.setGeometry(QtCore.QRect(30, 60, 351, 51))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(browserDialog)
        self.label_2.setGeometry(QtCore.QRect(70, 20, 271, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.emptyBox_3 = QtWidgets.QLabel(browserDialog)
        self.emptyBox_3.setGeometry(QtCore.QRect(20, 30, 371, 101))
        self.emptyBox_3.setStyleSheet("border: 1px solid rgb(165, 165, 165);\n"
                                      "")
        self.emptyBox_3.setText("")
        self.emptyBox_3.setObjectName("emptyBox_3")
        self.emptyBox_3.raise_()
        self.label.raise_()
        self.label_2.raise_()

        self.retranslateUi(browserDialog)
        QtCore.QMetaObject.connectSlotsByName(browserDialog)

    def retranslateUi(self, browserDialog):
        _translate = QtCore.QCoreApplication.translate
        browserDialog.setWindowTitle(_translate("browserDialog", "Dialog"))
        self.label.setText(_translate("browserDialog", "Choose a browser from\n"
                                      " the dropdown menu"))
        self.label_2.setText(
            _translate(
                "browserDialog",
                "You Must Choose A Browser"))


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    browserDialog = QtWidgets.QDialog()
    ui = Ui_browserDialog()
    ui.setupUi(browserDialog)
    browserDialog.show()
    sys.exit(app.exec_())
