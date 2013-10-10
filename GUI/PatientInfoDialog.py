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

		#The order of calling following functions is important.setupUi should be called first to create all attr.
		self.setupUi(self)
		self.setGroupButton()
		self.updateUi()
		#The updateUi() method called at the end is our own custom method;we use it to 
		#enable or disable the buttons depending on whether the user has entered any text to find.
		
	def setGroupButton(self):
		'''There is no GroupBox in QT Designer,we have to create them by codes.'''
		self.buttonGroup_fare = QButtonGroup()
		self.buttonGroup_fare.addButton(self.fare1RadioButton,1)
		self.buttonGroup_fare.addButton(self.fare2RadioButton,2)
		self.buttonGroup_fare.addButton(self.fare3RadioButton,3)
		
		self.buttonGroup_kesou = QButtonGroup()
		self.buttonGroup_kesou .addButton(self.kesou1RadioButton,4)
		self.buttonGroup_kesou .addButton(self.kesou2RadioButton,5)
		
		self.buttonGroup_tzdx = QButtonGroup()
		self.buttonGroup_tzdx.addButton(self.tanzhongdaixue1RadioButton,6)
		self.buttonGroup_tzdx.addButton(self.tanzhongdaixue2RadioButton,7)
		
		self.buttonGroup_kexue = QButtonGroup()
		self.buttonGroup_kexue.addButton(self.kexue1RadioButton,8)
		self.buttonGroup_kexue.addButton(self.kexue2RadioButton,9)
		
		self.buttonGroup_xiongmen = QButtonGroup()
		self.buttonGroup_xiongmen.addButton(self.xiongmen1RadioButton,10)
		self.buttonGroup_xiongmen.addButton(self.xiongmen2RadioButton,11)
		
		self.buttonGroup_xiongtong = QButtonGroup()
		self.buttonGroup_xiongtong.addButton(self.xiongtong1RadioButton,12)
		self.buttonGroup_xiongtong.addButton(self.xiongtong2RadioButton,13)		
		
		self.buttonGroup_sysy= QButtonGroup()
		self.buttonGroup_sysy.addButton(self.shengyinsiya1RadioButton,14)
		self.buttonGroup_sysy.addButton(self.shengyinsiya2RadioButton,15)

	@pyqtSignature("QString")
	def on_nameLineEdit_textEdited(self, text):
		'''#Slot# : Once nameLienEdit is being edited,call this function'''
		self.updateUi()
		
	def updateUi(self):
		enable = not self.nameLineEdit.text().isEmpty()
		self.acceptButton.setEnabled(enable)
		
	def getDiagnosisInfo(self):
		'''Return the info filled by doctor'''
		diagonosis = UI_Diagnosis()
		
		#Tab1's content
		diagonosis.name = str(self.nameLineEdit.text().toUtf8())#LineEdit
		diagonosis.sex = str(self.sexComboBox.currentText().toUtf8())#ComboBox
		diagonosis.job = str(self.jobLineEdit.text().toUtf8())
		diagonosis.nation = str(self.nationLineEdit.text().toUtf8())
		diagonosis.address = str(self.addressLineEdit.text().toUtf8())
		diagonosis.eduDegree = str(self.degreeComboBox.currentText().toUtf8())
		
		return diagonosis
		