# -*- coding: utf-8 -*-
import re
from PyQt4.QtCore import *
from PyQt4.QtGui import *
import PyQt4.QtGui
import ui_ShowResultDialog
MAC = hasattr(PyQt4.QtGui, "qt_mac_set_native_menubar")
#Normally,we inherit the class created by QT Designer,not use it directly

from append import qs2ps,ps2qs

class ShowResultDialog(QDialog,ui_ShowResultDialog.Ui_Dialog):
	def __init__(self,predict_value=None,parent=None):
		super(ShowResultDialog,self).__init__(parent)
		self._predict_value = predict_value
		self.setupUi(self)
		self.updateUi()
			
	def updateUi(self):
		_pstring = str(self._predict_value*100)+"%"
		self.percent_value_label.setText(ps2qs(_pstring))
	