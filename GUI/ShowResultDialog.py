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
	def __init__(self,predict_value1=0,predict_value2 = 0,parent=None):
		super(ShowResultDialog,self).__init__(parent)
		self._predict_value1 = predict_value1
		self._predict_value2 = predict_value2
		self.setupUi(self)
		self.updateUi()
			
	def updateUi(self):
		_pstring = str(self._predict_value1*100)+"%"
		self.predict_value1_label.setText(ps2qs(_pstring))
		
		_pstring = str(self._predict_value2*100)+"%"
		self.predict_value2_label.setText(ps2qs(_pstring))
	