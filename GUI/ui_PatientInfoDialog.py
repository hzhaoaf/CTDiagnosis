# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'DesignWindow.ui'
#
# Created: Thu Oct 10 09:54:22 2013
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

class Ui_PatientInfoDialog(object):
    def setupUi(self, PatientInfoDialog):
        PatientInfoDialog.setObjectName(_fromUtf8("PatientInfoDialog"))
        PatientInfoDialog.setWindowModality(QtCore.Qt.ApplicationModal)
        PatientInfoDialog.resize(810, 625)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(10)
        PatientInfoDialog.setFont(font)
        PatientInfoDialog.setAcceptDrops(False)
        self.tabWidget = QtGui.QTabWidget(PatientInfoDialog)
        self.tabWidget.setGeometry(QtCore.QRect(70, 10, 711, 491))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(11)
        self.tabWidget.setFont(font)
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.splitter = QtGui.QSplitter(self.tab)
        self.splitter.setGeometry(QtCore.QRect(110, 100, 501, 211))
        self.splitter.setOrientation(QtCore.Qt.Vertical)
        self.splitter.setObjectName(_fromUtf8("splitter"))
        self.layoutWidget = QtGui.QWidget(self.splitter)
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.gridLayout = QtGui.QGridLayout(self.layoutWidget)
        self.gridLayout.setMargin(0)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label = QtGui.QLabel(self.layoutWidget)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.nameLineEdit = QtGui.QLineEdit(self.layoutWidget)
        self.nameLineEdit.setObjectName(_fromUtf8("nameLineEdit"))
        self.gridLayout.addWidget(self.nameLineEdit, 0, 1, 1, 1)
        self.label_5 = QtGui.QLabel(self.layoutWidget)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.gridLayout.addWidget(self.label_5, 0, 2, 1, 1)
        self.sexComboBox = QtGui.QComboBox(self.layoutWidget)
        self.sexComboBox.setObjectName(_fromUtf8("sexComboBox"))
        self.sexComboBox.addItem(_fromUtf8(""))
        self.sexComboBox.addItem(_fromUtf8(""))
        self.gridLayout.addWidget(self.sexComboBox, 0, 3, 1, 1)
        self.label_2 = QtGui.QLabel(self.layoutWidget)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.jobLineEdit = QtGui.QLineEdit(self.layoutWidget)
        self.jobLineEdit.setObjectName(_fromUtf8("jobLineEdit"))
        self.gridLayout.addWidget(self.jobLineEdit, 1, 1, 1, 1)
        self.label_3 = QtGui.QLabel(self.layoutWidget)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout.addWidget(self.label_3, 1, 2, 1, 1)
        self.nationLineEdit = QtGui.QLineEdit(self.layoutWidget)
        self.nationLineEdit.setObjectName(_fromUtf8("nationLineEdit"))
        self.gridLayout.addWidget(self.nationLineEdit, 1, 3, 1, 1)
        self.layoutWidget1 = QtGui.QWidget(self.splitter)
        self.layoutWidget1.setObjectName(_fromUtf8("layoutWidget1"))
        self.gridLayout_2 = QtGui.QGridLayout(self.layoutWidget1)
        self.gridLayout_2.setMargin(0)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.label_4 = QtGui.QLabel(self.layoutWidget1)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout_2.addWidget(self.label_4, 0, 0, 1, 1)
        self.addressLineEdit = QtGui.QLineEdit(self.layoutWidget1)
        self.addressLineEdit.setObjectName(_fromUtf8("addressLineEdit"))
        self.gridLayout_2.addWidget(self.addressLineEdit, 0, 1, 1, 1)
        self.label_6 = QtGui.QLabel(self.layoutWidget1)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.gridLayout_2.addWidget(self.label_6, 1, 0, 1, 1)
        self.degreeComboBox = QtGui.QComboBox(self.layoutWidget1)
        self.degreeComboBox.setObjectName(_fromUtf8("degreeComboBox"))
        self.degreeComboBox.addItem(_fromUtf8(""))
        self.degreeComboBox.addItem(_fromUtf8(""))
        self.degreeComboBox.addItem(_fromUtf8(""))
        self.degreeComboBox.addItem(_fromUtf8(""))
        self.degreeComboBox.addItem(_fromUtf8(""))
        self.degreeComboBox.addItem(_fromUtf8(""))
        self.gridLayout_2.addWidget(self.degreeComboBox, 1, 1, 1, 1)
        self.tabWidget.addTab(self.tab, _fromUtf8(""))
        self.tab_2 = QtGui.QWidget()
        font = QtGui.QFont()
        font.setPointSize(10)
        self.tab_2.setFont(font)
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.layoutWidget2 = QtGui.QWidget(self.tab_2)
        self.layoutWidget2.setGeometry(QtCore.QRect(80, 10, 551, 431))
        self.layoutWidget2.setObjectName(_fromUtf8("layoutWidget2"))
        self.verticalLayout = QtGui.QVBoxLayout(self.layoutWidget2)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.gridLayout_5 = QtGui.QGridLayout()
        self.gridLayout_5.setObjectName(_fromUtf8("gridLayout_5"))
        self.zhongliuPlainTextEdit = QtGui.QPlainTextEdit(self.layoutWidget2)
        self.zhongliuPlainTextEdit.setObjectName(_fromUtf8("zhongliuPlainTextEdit"))
        self.gridLayout_5.addWidget(self.zhongliuPlainTextEdit, 0, 2, 2, 1)
        self.label_7 = QtGui.QLabel(self.layoutWidget2)
        self.label_7.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.gridLayout_5.addWidget(self.label_7, 0, 0, 1, 1)
        self.zhongliuComboBox = QtGui.QComboBox(self.layoutWidget2)
        self.zhongliuComboBox.setObjectName(_fromUtf8("zhongliuComboBox"))
        self.zhongliuComboBox.addItem(_fromUtf8(""))
        self.zhongliuComboBox.addItem(_fromUtf8(""))
        self.zhongliuComboBox.addItem(_fromUtf8(""))
        self.gridLayout_5.addWidget(self.zhongliuComboBox, 0, 1, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout_5)
        self.line = QtGui.QFrame(self.layoutWidget2)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.verticalLayout.addWidget(self.line)
        self.gridLayout_9 = QtGui.QGridLayout()
        self.gridLayout_9.setObjectName(_fromUtf8("gridLayout_9"))
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_9.addItem(spacerItem, 2, 2, 1, 1)
        self.label_28 = QtGui.QLabel(self.layoutWidget2)
        self.label_28.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_28.setObjectName(_fromUtf8("label_28"))
        self.gridLayout_9.addWidget(self.label_28, 0, 0, 1, 1)
        self.feijiehePlainTextEdit = QtGui.QPlainTextEdit(self.layoutWidget2)
        self.feijiehePlainTextEdit.setObjectName(_fromUtf8("feijiehePlainTextEdit"))
        self.gridLayout_9.addWidget(self.feijiehePlainTextEdit, 0, 2, 2, 1)
        self.feijiheComboBox = QtGui.QComboBox(self.layoutWidget2)
        self.feijiheComboBox.setObjectName(_fromUtf8("feijiheComboBox"))
        self.feijiheComboBox.addItem(_fromUtf8(""))
        self.feijiheComboBox.addItem(_fromUtf8(""))
        self.feijiheComboBox.addItem(_fromUtf8(""))
        self.gridLayout_9.addWidget(self.feijiheComboBox, 0, 1, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout_9)
        self.line_2 = QtGui.QFrame(self.layoutWidget2)
        self.line_2.setFrameShape(QtGui.QFrame.HLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName(_fromUtf8("line_2"))
        self.verticalLayout.addWidget(self.line_2)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label_17 = QtGui.QLabel(self.layoutWidget2)
        self.label_17.setObjectName(_fromUtf8("label_17"))
        self.horizontalLayout.addWidget(self.label_17)
        self.fenchenComboBox = QtGui.QComboBox(self.layoutWidget2)
        self.fenchenComboBox.setObjectName(_fromUtf8("fenchenComboBox"))
        self.fenchenComboBox.addItem(_fromUtf8(""))
        self.fenchenComboBox.addItem(_fromUtf8(""))
        self.fenchenComboBox.addItem(_fromUtf8(""))
        self.horizontalLayout.addWidget(self.fenchenComboBox)
        self.label_18 = QtGui.QLabel(self.layoutWidget2)
        self.label_18.setObjectName(_fromUtf8("label_18"))
        self.horizontalLayout.addWidget(self.label_18)
        self.xirunianxianLineEdit = QtGui.QLineEdit(self.layoutWidget2)
        self.xirunianxianLineEdit.setMaximumSize(QtCore.QSize(30, 16777215))
        self.xirunianxianLineEdit.setObjectName(_fromUtf8("xirunianxianLineEdit"))
        self.horizontalLayout.addWidget(self.xirunianxianLineEdit)
        self.label_19 = QtGui.QLabel(self.layoutWidget2)
        self.label_19.setObjectName(_fromUtf8("label_19"))
        self.horizontalLayout.addWidget(self.label_19)
        self.label_20 = QtGui.QLabel(self.layoutWidget2)
        self.label_20.setObjectName(_fromUtf8("label_20"))
        self.horizontalLayout.addWidget(self.label_20)
        self.gongzhongLineEdit = QtGui.QLineEdit(self.layoutWidget2)
        self.gongzhongLineEdit.setObjectName(_fromUtf8("gongzhongLineEdit"))
        self.horizontalLayout.addWidget(self.gongzhongLineEdit)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.line_3 = QtGui.QFrame(self.layoutWidget2)
        self.line_3.setFrameShape(QtGui.QFrame.HLine)
        self.line_3.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_3.setObjectName(_fromUtf8("line_3"))
        self.verticalLayout.addWidget(self.line_3)
        self.gridLayout_6 = QtGui.QGridLayout()
        self.gridLayout_6.setObjectName(_fromUtf8("gridLayout_6"))
        spacerItem2 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_6.addItem(spacerItem2, 2, 2, 1, 1)
        self.label_21 = QtGui.QLabel(self.layoutWidget2)
        self.label_21.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_21.setObjectName(_fromUtf8("label_21"))
        self.gridLayout_6.addWidget(self.label_21, 0, 0, 1, 1)
        self.yichuanPlainTextEdit = QtGui.QPlainTextEdit(self.layoutWidget2)
        self.yichuanPlainTextEdit.setObjectName(_fromUtf8("yichuanPlainTextEdit"))
        self.gridLayout_6.addWidget(self.yichuanPlainTextEdit, 0, 2, 2, 1)
        self.yichuanComboBox = QtGui.QComboBox(self.layoutWidget2)
        self.yichuanComboBox.setObjectName(_fromUtf8("yichuanComboBox"))
        self.yichuanComboBox.addItem(_fromUtf8(""))
        self.yichuanComboBox.addItem(_fromUtf8(""))
        self.yichuanComboBox.addItem(_fromUtf8(""))
        self.gridLayout_6.addWidget(self.yichuanComboBox, 0, 1, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout_6)
        self.line_4 = QtGui.QFrame(self.layoutWidget2)
        self.line_4.setFrameShape(QtGui.QFrame.HLine)
        self.line_4.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_4.setObjectName(_fromUtf8("line_4"))
        self.verticalLayout.addWidget(self.line_4)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.label_22 = QtGui.QLabel(self.layoutWidget2)
        self.label_22.setObjectName(_fromUtf8("label_22"))
        self.horizontalLayout_2.addWidget(self.label_22)
        self.xiyanComboBox = QtGui.QComboBox(self.layoutWidget2)
        self.xiyanComboBox.setObjectName(_fromUtf8("xiyanComboBox"))
        self.xiyanComboBox.addItem(_fromUtf8(""))
        self.xiyanComboBox.addItem(_fromUtf8(""))
        self.xiyanComboBox.addItem(_fromUtf8(""))
        self.horizontalLayout_2.addWidget(self.xiyanComboBox)
        self.label_23 = QtGui.QLabel(self.layoutWidget2)
        self.label_23.setObjectName(_fromUtf8("label_23"))
        self.horizontalLayout_2.addWidget(self.label_23)
        self.xiyannianLineEdit = QtGui.QLineEdit(self.layoutWidget2)
        self.xiyannianLineEdit.setMaximumSize(QtCore.QSize(30, 16777215))
        self.xiyannianLineEdit.setObjectName(_fromUtf8("xiyannianLineEdit"))
        self.horizontalLayout_2.addWidget(self.xiyannianLineEdit)
        self.label_24 = QtGui.QLabel(self.layoutWidget2)
        self.label_24.setObjectName(_fromUtf8("label_24"))
        self.horizontalLayout_2.addWidget(self.label_24)
        self.label_25 = QtGui.QLabel(self.layoutWidget2)
        self.label_25.setObjectName(_fromUtf8("label_25"))
        self.horizontalLayout_2.addWidget(self.label_25)
        self.xiyanzhiLineEdit = QtGui.QLineEdit(self.layoutWidget2)
        self.xiyanzhiLineEdit.setMaximumSize(QtCore.QSize(30, 30))
        self.xiyanzhiLineEdit.setObjectName(_fromUtf8("xiyanzhiLineEdit"))
        self.horizontalLayout_2.addWidget(self.xiyanzhiLineEdit)
        self.label_26 = QtGui.QLabel(self.layoutWidget2)
        self.label_26.setObjectName(_fromUtf8("label_26"))
        self.horizontalLayout_2.addWidget(self.label_26)
        spacerItem3 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem3)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.line_5 = QtGui.QFrame(self.layoutWidget2)
        self.line_5.setFrameShape(QtGui.QFrame.HLine)
        self.line_5.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_5.setObjectName(_fromUtf8("line_5"))
        self.verticalLayout.addWidget(self.line_5)
        self.gridLayout_7 = QtGui.QGridLayout()
        self.gridLayout_7.setObjectName(_fromUtf8("gridLayout_7"))
        self.huxiPlainTextEdit = QtGui.QPlainTextEdit(self.layoutWidget2)
        self.huxiPlainTextEdit.setObjectName(_fromUtf8("huxiPlainTextEdit"))
        self.gridLayout_7.addWidget(self.huxiPlainTextEdit, 0, 2, 2, 1)
        self.huxiComboBox = QtGui.QComboBox(self.layoutWidget2)
        self.huxiComboBox.setObjectName(_fromUtf8("huxiComboBox"))
        self.huxiComboBox.addItem(_fromUtf8(""))
        self.huxiComboBox.addItem(_fromUtf8(""))
        self.huxiComboBox.addItem(_fromUtf8(""))
        self.gridLayout_7.addWidget(self.huxiComboBox, 0, 1, 1, 1)
        self.label_27 = QtGui.QLabel(self.layoutWidget2)
        self.label_27.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_27.setObjectName(_fromUtf8("label_27"))
        self.gridLayout_7.addWidget(self.label_27, 0, 0, 2, 1)
        self.verticalLayout.addLayout(self.gridLayout_7)
        self.tabWidget.addTab(self.tab_2, _fromUtf8(""))
        self.tab_3 = QtGui.QWidget()
        self.tab_3.setObjectName(_fromUtf8("tab_3"))
        self.layoutWidget3 = QtGui.QWidget(self.tab_3)
        self.layoutWidget3.setGeometry(QtCore.QRect(60, 30, 611, 401))
        self.layoutWidget3.setObjectName(_fromUtf8("layoutWidget3"))
        self.gridLayout_12 = QtGui.QGridLayout(self.layoutWidget3)
        self.gridLayout_12.setMargin(0)
        self.gridLayout_12.setObjectName(_fromUtf8("gridLayout_12"))
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.label_32 = QtGui.QLabel(self.layoutWidget3)
        self.label_32.setAlignment(QtCore.Qt.AlignCenter)
        self.label_32.setObjectName(_fromUtf8("label_32"))
        self.horizontalLayout_5.addWidget(self.label_32)
        self.linchuang_PlainTextEdit = QtGui.QPlainTextEdit(self.layoutWidget3)
        self.linchuang_PlainTextEdit.setObjectName(_fromUtf8("linchuang_PlainTextEdit"))
        self.horizontalLayout_5.addWidget(self.linchuang_PlainTextEdit)
        self.gridLayout_12.addLayout(self.horizontalLayout_5, 6, 0, 1, 2)
        self.gridLayout_11 = QtGui.QGridLayout()
        self.gridLayout_11.setObjectName(_fromUtf8("gridLayout_11"))
        self.label_37 = QtGui.QLabel(self.layoutWidget3)
        self.label_37.setAlignment(QtCore.Qt.AlignCenter)
        self.label_37.setObjectName(_fromUtf8("label_37"))
        self.gridLayout_11.addWidget(self.label_37, 0, 0, 1, 2)
        self.label_38 = QtGui.QLabel(self.layoutWidget3)
        self.label_38.setAlignment(QtCore.Qt.AlignCenter)
        self.label_38.setObjectName(_fromUtf8("label_38"))
        self.gridLayout_11.addWidget(self.label_38, 2, 0, 1, 2)
        self.label_39 = QtGui.QLabel(self.layoutWidget3)
        self.label_39.setAlignment(QtCore.Qt.AlignCenter)
        self.label_39.setObjectName(_fromUtf8("label_39"))
        self.gridLayout_11.addWidget(self.label_39, 1, 0, 1, 2)
        self.kesou1RadioButton = QtGui.QRadioButton(self.layoutWidget3)
        self.kesou1RadioButton.setObjectName(_fromUtf8("kesou1RadioButton"))
        self.gridLayout_11.addWidget(self.kesou1RadioButton, 0, 2, 1, 2)
        self.xiongtong1RadioButton = QtGui.QRadioButton(self.layoutWidget3)
        self.xiongtong1RadioButton.setObjectName(_fromUtf8("xiongtong1RadioButton"))
        self.gridLayout_11.addWidget(self.xiongtong1RadioButton, 2, 2, 1, 2)
        self.xiongtong2RadioButton = QtGui.QRadioButton(self.layoutWidget3)
        self.xiongtong2RadioButton.setObjectName(_fromUtf8("xiongtong2RadioButton"))
        self.gridLayout_11.addWidget(self.xiongtong2RadioButton, 2, 4, 1, 1)
        self.kexue2RadioButton = QtGui.QRadioButton(self.layoutWidget3)
        self.kexue2RadioButton.setObjectName(_fromUtf8("kexue2RadioButton"))
        self.gridLayout_11.addWidget(self.kexue2RadioButton, 1, 4, 1, 1)
        self.kexue1RadioButton = QtGui.QRadioButton(self.layoutWidget3)
        self.kexue1RadioButton.setObjectName(_fromUtf8("kexue1RadioButton"))
        self.gridLayout_11.addWidget(self.kexue1RadioButton, 1, 2, 1, 2)
        self.kesou2RadioButton = QtGui.QRadioButton(self.layoutWidget3)
        self.kesou2RadioButton.setObjectName(_fromUtf8("kesou2RadioButton"))
        self.gridLayout_11.addWidget(self.kesou2RadioButton, 0, 4, 1, 1)
        spacerItem4 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_11.addItem(spacerItem4, 0, 5, 1, 1)
        self.gridLayout_12.addLayout(self.gridLayout_11, 3, 0, 1, 1)
        self.horizontalLayout_6 = QtGui.QHBoxLayout()
        self.horizontalLayout_6.setObjectName(_fromUtf8("horizontalLayout_6"))
        self.label_29 = QtGui.QLabel(self.layoutWidget3)
        self.label_29.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.label_29.setObjectName(_fromUtf8("label_29"))
        self.horizontalLayout_6.addWidget(self.label_29)
        self.zhusu_PlainTextEdit = QtGui.QPlainTextEdit(self.layoutWidget3)
        self.zhusu_PlainTextEdit.setObjectName(_fromUtf8("zhusu_PlainTextEdit"))
        self.horizontalLayout_6.addWidget(self.zhusu_PlainTextEdit)
        self.gridLayout_12.addLayout(self.horizontalLayout_6, 0, 0, 1, 2)
        self.fareHorizontalLayout = QtGui.QHBoxLayout()
        self.fareHorizontalLayout.setObjectName(_fromUtf8("fareHorizontalLayout"))
        self.label_30 = QtGui.QLabel(self.layoutWidget3)
        self.label_30.setObjectName(_fromUtf8("label_30"))
        self.fareHorizontalLayout.addWidget(self.label_30)
        self.fare1RadioButton = QtGui.QRadioButton(self.layoutWidget3)
        self.fare1RadioButton.setObjectName(_fromUtf8("fare1RadioButton"))
        self.fareHorizontalLayout.addWidget(self.fare1RadioButton)
        self.fare2RadioButton = QtGui.QRadioButton(self.layoutWidget3)
        self.fare2RadioButton.setObjectName(_fromUtf8("fare2RadioButton"))
        self.fareHorizontalLayout.addWidget(self.fare2RadioButton)
        self.fare3RadioButton = QtGui.QRadioButton(self.layoutWidget3)
        self.fare3RadioButton.setObjectName(_fromUtf8("fare3RadioButton"))
        self.fareHorizontalLayout.addWidget(self.fare3RadioButton)
        self.gridLayout_12.addLayout(self.fareHorizontalLayout, 2, 0, 1, 1)
        self.line_6 = QtGui.QFrame(self.layoutWidget3)
        self.line_6.setLineWidth(2)
        self.line_6.setFrameShape(QtGui.QFrame.HLine)
        self.line_6.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_6.setObjectName(_fromUtf8("line_6"))
        self.gridLayout_12.addWidget(self.line_6, 4, 0, 1, 2)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.label_31 = QtGui.QLabel(self.layoutWidget3)
        self.label_31.setAlignment(QtCore.Qt.AlignCenter)
        self.label_31.setObjectName(_fromUtf8("label_31"))
        self.horizontalLayout_4.addWidget(self.label_31)
        self.qita_PlainTextEdit = QtGui.QPlainTextEdit(self.layoutWidget3)
        self.qita_PlainTextEdit.setObjectName(_fromUtf8("qita_PlainTextEdit"))
        self.horizontalLayout_4.addWidget(self.qita_PlainTextEdit)
        self.gridLayout_12.addLayout(self.horizontalLayout_4, 5, 0, 1, 2)
        self.line_7 = QtGui.QFrame(self.layoutWidget3)
        self.line_7.setFrameShape(QtGui.QFrame.HLine)
        self.line_7.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_7.setObjectName(_fromUtf8("line_7"))
        self.gridLayout_12.addWidget(self.line_7, 1, 0, 1, 2)
        self.gridLayout_10 = QtGui.QGridLayout()
        self.gridLayout_10.setObjectName(_fromUtf8("gridLayout_10"))
        self.tanzhongdaixue1RadioButton = QtGui.QRadioButton(self.layoutWidget3)
        self.tanzhongdaixue1RadioButton.setObjectName(_fromUtf8("tanzhongdaixue1RadioButton"))
        self.gridLayout_10.addWidget(self.tanzhongdaixue1RadioButton, 0, 2, 1, 2)
        self.tanzhongdaixue2RadioButton = QtGui.QRadioButton(self.layoutWidget3)
        self.tanzhongdaixue2RadioButton.setObjectName(_fromUtf8("tanzhongdaixue2RadioButton"))
        self.gridLayout_10.addWidget(self.tanzhongdaixue2RadioButton, 0, 4, 1, 1)
        spacerItem5 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_10.addItem(spacerItem5, 0, 5, 1, 1)
        self.label_34 = QtGui.QLabel(self.layoutWidget3)
        self.label_34.setAlignment(QtCore.Qt.AlignCenter)
        self.label_34.setObjectName(_fromUtf8("label_34"))
        self.gridLayout_10.addWidget(self.label_34, 0, 0, 1, 2)
        self.xiongmen2RadioButton = QtGui.QRadioButton(self.layoutWidget3)
        self.xiongmen2RadioButton.setObjectName(_fromUtf8("xiongmen2RadioButton"))
        self.gridLayout_10.addWidget(self.xiongmen2RadioButton, 1, 4, 1, 1)
        self.label_35 = QtGui.QLabel(self.layoutWidget3)
        self.label_35.setAlignment(QtCore.Qt.AlignCenter)
        self.label_35.setObjectName(_fromUtf8("label_35"))
        self.gridLayout_10.addWidget(self.label_35, 1, 0, 1, 2)
        self.shengyinsiya1RadioButton = QtGui.QRadioButton(self.layoutWidget3)
        self.shengyinsiya1RadioButton.setObjectName(_fromUtf8("shengyinsiya1RadioButton"))
        self.gridLayout_10.addWidget(self.shengyinsiya1RadioButton, 2, 2, 1, 2)
        self.label_36 = QtGui.QLabel(self.layoutWidget3)
        self.label_36.setAlignment(QtCore.Qt.AlignCenter)
        self.label_36.setObjectName(_fromUtf8("label_36"))
        self.gridLayout_10.addWidget(self.label_36, 2, 0, 1, 2)
        self.xiongmen1RadioButton = QtGui.QRadioButton(self.layoutWidget3)
        self.xiongmen1RadioButton.setObjectName(_fromUtf8("xiongmen1RadioButton"))
        self.gridLayout_10.addWidget(self.xiongmen1RadioButton, 1, 2, 1, 2)
        self.shengyinsiya2RadioButton = QtGui.QRadioButton(self.layoutWidget3)
        self.shengyinsiya2RadioButton.setObjectName(_fromUtf8("shengyinsiya2RadioButton"))
        self.gridLayout_10.addWidget(self.shengyinsiya2RadioButton, 2, 4, 1, 1)
        self.gridLayout_12.addLayout(self.gridLayout_10, 3, 1, 1, 1)
        self.tabWidget.addTab(self.tab_3, _fromUtf8(""))
        self.tab_4 = QtGui.QWidget()
        self.tab_4.setObjectName(_fromUtf8("tab_4"))
        self.tabWidget.addTab(self.tab_4, _fromUtf8(""))
        self.acceptButton = QtGui.QPushButton(PatientInfoDialog)
        self.acceptButton.setGeometry(QtCore.QRect(600, 520, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.acceptButton.setFont(font)
        self.acceptButton.setObjectName(_fromUtf8("acceptButton"))
        self.cancelButton = QtGui.QPushButton(PatientInfoDialog)
        self.cancelButton.setGeometry(QtCore.QRect(700, 520, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.cancelButton.setFont(font)
        self.cancelButton.setObjectName(_fromUtf8("cancelButton"))
        self.label.setBuddy(self.nameLineEdit)
        self.label_5.setBuddy(self.sexComboBox)
        self.label_2.setBuddy(self.jobLineEdit)
        self.label_3.setBuddy(self.nationLineEdit)
        self.label_4.setBuddy(self.addressLineEdit)
        self.label_6.setBuddy(self.degreeComboBox)

        self.retranslateUi(PatientInfoDialog)
        self.tabWidget.setCurrentIndex(2)
        QtCore.QObject.connect(self.cancelButton, QtCore.SIGNAL(_fromUtf8("clicked()")), PatientInfoDialog.reject)
        QtCore.QObject.connect(self.acceptButton, QtCore.SIGNAL(_fromUtf8("clicked()")), PatientInfoDialog.accept)
        QtCore.QMetaObject.connectSlotsByName(PatientInfoDialog)
        PatientInfoDialog.setTabOrder(self.nameLineEdit, self.sexComboBox)
        PatientInfoDialog.setTabOrder(self.sexComboBox, self.jobLineEdit)
        PatientInfoDialog.setTabOrder(self.jobLineEdit, self.nationLineEdit)
        PatientInfoDialog.setTabOrder(self.nationLineEdit, self.addressLineEdit)
        PatientInfoDialog.setTabOrder(self.addressLineEdit, self.degreeComboBox)
        PatientInfoDialog.setTabOrder(self.degreeComboBox, self.zhongliuComboBox)
        PatientInfoDialog.setTabOrder(self.zhongliuComboBox, self.zhongliuPlainTextEdit)
        PatientInfoDialog.setTabOrder(self.zhongliuPlainTextEdit, self.feijiheComboBox)
        PatientInfoDialog.setTabOrder(self.feijiheComboBox, self.feijiehePlainTextEdit)
        PatientInfoDialog.setTabOrder(self.feijiehePlainTextEdit, self.fenchenComboBox)
        PatientInfoDialog.setTabOrder(self.fenchenComboBox, self.xirunianxianLineEdit)
        PatientInfoDialog.setTabOrder(self.xirunianxianLineEdit, self.gongzhongLineEdit)
        PatientInfoDialog.setTabOrder(self.gongzhongLineEdit, self.yichuanComboBox)
        PatientInfoDialog.setTabOrder(self.yichuanComboBox, self.yichuanPlainTextEdit)
        PatientInfoDialog.setTabOrder(self.yichuanPlainTextEdit, self.xiyanComboBox)
        PatientInfoDialog.setTabOrder(self.xiyanComboBox, self.xiyannianLineEdit)
        PatientInfoDialog.setTabOrder(self.xiyannianLineEdit, self.xiyanzhiLineEdit)
        PatientInfoDialog.setTabOrder(self.xiyanzhiLineEdit, self.huxiComboBox)
        PatientInfoDialog.setTabOrder(self.huxiComboBox, self.huxiPlainTextEdit)
        PatientInfoDialog.setTabOrder(self.huxiPlainTextEdit, self.tabWidget)
        PatientInfoDialog.setTabOrder(self.tabWidget, self.acceptButton)
        PatientInfoDialog.setTabOrder(self.acceptButton, self.cancelButton)

    def retranslateUi(self, PatientInfoDialog):
        PatientInfoDialog.setWindowTitle(_translate("PatientInfoDialog", "患者信息", None))
        self.label.setText(_translate("PatientInfoDialog", "姓名", None))
        self.label_5.setText(_translate("PatientInfoDialog", "性别", None))
        self.sexComboBox.setItemText(0, _translate("PatientInfoDialog", "男", None))
        self.sexComboBox.setItemText(1, _translate("PatientInfoDialog", "女", None))
        self.label_2.setText(_translate("PatientInfoDialog", "职业", None))
        self.label_3.setText(_translate("PatientInfoDialog", "民族", None))
        self.label_4.setText(_translate("PatientInfoDialog", "家庭住址", None))
        self.label_6.setText(_translate("PatientInfoDialog", "文化程度", None))
        self.degreeComboBox.setItemText(0, _translate("PatientInfoDialog", "大学以上", None))
        self.degreeComboBox.setItemText(1, _translate("PatientInfoDialog", "大学", None))
        self.degreeComboBox.setItemText(2, _translate("PatientInfoDialog", "高中", None))
        self.degreeComboBox.setItemText(3, _translate("PatientInfoDialog", "初中", None))
        self.degreeComboBox.setItemText(4, _translate("PatientInfoDialog", "小学", None))
        self.degreeComboBox.setItemText(5, _translate("PatientInfoDialog", "文盲或半文盲", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("PatientInfoDialog", "个人信息", None))
        self.label_7.setText(_translate("PatientInfoDialog", "肿 瘤 病 史", None))
        self.zhongliuComboBox.setItemText(0, _translate("PatientInfoDialog", "无", None))
        self.zhongliuComboBox.setItemText(1, _translate("PatientInfoDialog", "有", None))
        self.zhongliuComboBox.setItemText(2, _translate("PatientInfoDialog", "不详", None))
        self.label_28.setText(_translate("PatientInfoDialog", "肺结核病史", None))
        self.feijiheComboBox.setItemText(0, _translate("PatientInfoDialog", "无", None))
        self.feijiheComboBox.setItemText(1, _translate("PatientInfoDialog", "有", None))
        self.feijiheComboBox.setItemText(2, _translate("PatientInfoDialog", "不详", None))
        self.label_17.setText(_translate("PatientInfoDialog", "粉尘吸入史", None))
        self.fenchenComboBox.setItemText(0, _translate("PatientInfoDialog", "无", None))
        self.fenchenComboBox.setItemText(1, _translate("PatientInfoDialog", "有", None))
        self.fenchenComboBox.setItemText(2, _translate("PatientInfoDialog", "不详", None))
        self.label_18.setText(_translate("PatientInfoDialog", "吸入工作年限", None))
        self.label_19.setText(_translate("PatientInfoDialog", "年   ", None))
        self.label_20.setText(_translate("PatientInfoDialog", "工种：", None))
        self.label_21.setText(_translate("PatientInfoDialog", "遗 传 病 史", None))
        self.yichuanComboBox.setItemText(0, _translate("PatientInfoDialog", "无", None))
        self.yichuanComboBox.setItemText(1, _translate("PatientInfoDialog", "有", None))
        self.yichuanComboBox.setItemText(2, _translate("PatientInfoDialog", "不详", None))
        self.label_22.setText(_translate("PatientInfoDialog", "吸 烟 史    ", None))
        self.xiyanComboBox.setItemText(0, _translate("PatientInfoDialog", "无", None))
        self.xiyanComboBox.setItemText(1, _translate("PatientInfoDialog", "有", None))
        self.xiyanComboBox.setItemText(2, _translate("PatientInfoDialog", "不详", None))
        self.label_23.setText(_translate("PatientInfoDialog", "吸烟年限", None))
        self.label_24.setText(_translate("PatientInfoDialog", "年    ", None))
        self.label_25.setText(_translate("PatientInfoDialog", "每天吸烟数", None))
        self.label_26.setText(_translate("PatientInfoDialog", "支", None))
        self.huxiComboBox.setItemText(0, _translate("PatientInfoDialog", "无", None))
        self.huxiComboBox.setItemText(1, _translate("PatientInfoDialog", "有", None))
        self.huxiComboBox.setItemText(2, _translate("PatientInfoDialog", "不详", None))
        self.label_27.setText(_translate("PatientInfoDialog", "呼 吸 病 史\n"
"或 其 他  ", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("PatientInfoDialog", "既往史", None))
        self.label_32.setText(_translate("PatientInfoDialog", "临床诊断意见：", None))
        self.label_37.setText(_translate("PatientInfoDialog", "咳嗽", None))
        self.label_38.setText(_translate("PatientInfoDialog", "胸痛", None))
        self.label_39.setText(_translate("PatientInfoDialog", "咳血", None))
        self.kesou1RadioButton.setText(_translate("PatientInfoDialog", "无", None))
        self.xiongtong1RadioButton.setText(_translate("PatientInfoDialog", "无", None))
        self.xiongtong2RadioButton.setText(_translate("PatientInfoDialog", "有", None))
        self.kexue2RadioButton.setText(_translate("PatientInfoDialog", "有", None))
        self.kexue1RadioButton.setText(_translate("PatientInfoDialog", "无", None))
        self.kesou2RadioButton.setText(_translate("PatientInfoDialog", "有", None))
        self.label_29.setText(_translate("PatientInfoDialog", "主诉：", None))
        self.label_30.setText(_translate("PatientInfoDialog", "发热", None))
        self.fare1RadioButton.setText(_translate("PatientInfoDialog", "无", None))
        self.fare2RadioButton.setText(_translate("PatientInfoDialog", "37.5-38摄氏度", None))
        self.fare3RadioButton.setText(_translate("PatientInfoDialog", "38摄氏度以上", None))
        self.label_31.setText(_translate("PatientInfoDialog", "其它与呼吸有关\n"
"的临床表现：", None))
        self.tanzhongdaixue1RadioButton.setText(_translate("PatientInfoDialog", "无", None))
        self.tanzhongdaixue2RadioButton.setText(_translate("PatientInfoDialog", "有", None))
        self.label_34.setText(_translate("PatientInfoDialog", "痰中带血", None))
        self.xiongmen2RadioButton.setText(_translate("PatientInfoDialog", "有", None))
        self.label_35.setText(_translate("PatientInfoDialog", "胸闷", None))
        self.shengyinsiya1RadioButton.setText(_translate("PatientInfoDialog", "无", None))
        self.label_36.setText(_translate("PatientInfoDialog", "声音嘶哑", None))
        self.xiongmen1RadioButton.setText(_translate("PatientInfoDialog", "无", None))
        self.shengyinsiya2RadioButton.setText(_translate("PatientInfoDialog", "有", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("PatientInfoDialog", "就诊信息", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("PatientInfoDialog", "影响查看结果", None))
        self.acceptButton.setText(_translate("PatientInfoDialog", "确定", None))
        self.cancelButton.setText(_translate("PatientInfoDialog", "取消", None))

