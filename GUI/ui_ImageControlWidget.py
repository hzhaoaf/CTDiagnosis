# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ImageControlWidget.ui'
#
# Created: Tue Oct 15 16:32:04 2013
#      by: PyQt4 UI code generator 4.10.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_OriginImageControl(object):
    def setupUi(self, OriginImageControl):
        OriginImageControl.setObjectName(_fromUtf8("OriginImageControl"))
        OriginImageControl.resize(745, 78)
        self.prevImage_button = QtGui.QPushButton(OriginImageControl)
        self.prevImage_button.setGeometry(QtCore.QRect(130, 10, 61, 61))
        self.prevImage_button.setText(_fromUtf8(""))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("icon/svmPredict.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.prevImage_button.setIcon(icon)
        self.prevImage_button.setIconSize(QtCore.QSize(50, 50))
        self.prevImage_button.setObjectName(_fromUtf8("prevImage_button"))
        self.nextImage_button = QtGui.QPushButton(OriginImageControl)
        self.nextImage_button.setGeometry(QtCore.QRect(550, 10, 61, 61))
        self.nextImage_button.setText(_fromUtf8(""))
        self.nextImage_button.setIcon(icon)
        self.nextImage_button.setIconSize(QtCore.QSize(50, 50))
        self.nextImage_button.setObjectName(_fromUtf8("nextImage_button"))

        self.retranslateUi(OriginImageControl)
        QtCore.QMetaObject.connectSlotsByName(OriginImageControl)

    def retranslateUi(self, OriginImageControl):
        OriginImageControl.setWindowTitle(_translate("OriginImageControl", "Form", None))

