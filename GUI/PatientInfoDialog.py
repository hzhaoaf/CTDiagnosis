# -*- coding: utf-8 -*-
import re
from PyQt4.QtCore import *
from PyQt4.QtGui import *
import PyQt4.QtGui
import ui_PatientInfoDialog
MAC = hasattr(PyQt4.QtGui, "qt_mac_set_native_menubar")
#Normally,we inherit the class created by QT Designer,not use it directly
from  gui_model_diagnosis import UI_Diagnosis
from append import qs2ps

class PatientInfoDialog(QDialog,ui_PatientInfoDialog.Ui_PatientInfoDialog):
	def __init__(self,text=None,parent=None):
		super(PatientInfoDialog,self).__init__(parent)
		self.__text = text
		#self.__index = 0
		self.setupUi(self)
		self.updateUi()
		#The updateUi() method called at the end is our own custom method;we use it to 
		#enable or disable the buttons depending on whether the user has entered any text to find.
	@pyqtSignature("QString")
	def on_nameLineEdit_textEdited(self, text):
		'''#Slot# : Once nameLienEdit is being edited,call this function'''
		self.updateUi()
		
	def updateUi(self):
		enable = not self.nameLineEdit.text().isEmpty()
		self.acceptButton.setEnabled(enable)
		
	def getDiagnosisInfo(self):
		diagonosis = UI_Diagnosis()
		
		#Tab1's content
		diagonosis.name = str(self.nameLineEdit.text().toUtf8())#LineEdit
		diagonosis.sex = str(self.sexComboBox.currentText().toUtf8())#ComboBox
		diagonosis.job = str(self.jobLineEdit.text().toUtf8())
		diagonosis.nation = str(self.nationLineEdit.text().toUtf8())
		diagonosis.address = str(self.addressLineEdit.text().toUtf8())
		diagonosis.eduDegree = str(self.degreeComboBox.currentText().toUtf8())
		
		return diagonosis
		