# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'browser_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_browserDialog(object):
    def setupUi(self, browserDialog):
        browserDialog.setObjectName("browserDialog")
        browserDialog.resize(417, 161)
        browserDialog.setMinimumSize(QtCore.QSize(417, 161))
        browserDialog.setMaximumSize(QtCore.QSize(417, 161))
        self.label = QtWidgets.QLabel(browserDialog)
        self.label.setGeometry(QtCore.QRect(60, 60, 301, 51))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(browserDialog)
        self.label_2.setGeometry(QtCore.QRect(10, 30, 401, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")

        self.retranslateUi(browserDialog)
        QtCore.QMetaObject.connectSlotsByName(browserDialog)

    def retranslateUi(self, browserDialog):
        _translate = QtCore.QCoreApplication.translate
        browserDialog.setWindowTitle(_translate("browserDialog", "BrowserDialog"))
        self.label.setText(_translate("browserDialog", "Choose A Browser From \n"
"The Drop Down Menu"))
        self.label_2.setText(_translate("browserDialog", "You Must Choose A Browser"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    browserDialog = QtWidgets.QDialog()
    ui = Ui_browserDialog()
    ui.setupUi(browserDialog)
    browserDialog.show()
    sys.exit(app.exec_())
