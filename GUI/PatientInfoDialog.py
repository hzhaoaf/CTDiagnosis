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
		'''
		There is no GroupBox in QT Designer,we have to create them by codes.
		'''
		self.buttonGroup_fare = QButtonGroup()
		self.buttonGroup_fare.addButton(self.fare_wu_RadioButton,1)
		self.buttonGroup_fare.addButton(self.fare_3738_RadioButton,2)
		self.buttonGroup_fare.addButton(self.fare_38yishang_RadioButton,3)
		
		self.buttonGroup_kesou = QButtonGroup()
		self.buttonGroup_kesou .addButton(self.kesou_wu_RadioButton,4)
		self.buttonGroup_kesou .addButton(self.kesou_you_RadioButton,5)
		
		self.buttonGroup_tzdx = QButtonGroup()
		self.buttonGroup_tzdx.addButton(self.tanzhongdaixue_wu_RadioButton,6)
		self.buttonGroup_tzdx.addButton(self.tanzhongdaixue_you_RadioButton,7)
		
		self.buttonGroup_kexue = QButtonGroup()
		self.buttonGroup_kexue.addButton(self.kexue_wu_RadioButton,8)
		self.buttonGroup_kexue.addButton(self.kexue_you_RadioButton,9)
		
		self.buttonGroup_xiongmen = QButtonGroup()
		self.buttonGroup_xiongmen.addButton(self.xiongmen_wu_RadioButton,10)
		self.buttonGroup_xiongmen.addButton(self.xiongmen_you_RadioButton,11)
		
		self.buttonGroup_xiongtong = QButtonGroup()
		self.buttonGroup_xiongtong.addButton(self.xiongtong_wu_RadioButton,12)
		self.buttonGroup_xiongtong.addButton(self.xiongtong_you_RadioButton,13)		
		
		self.buttonGroup_sysy= QButtonGroup()
		
		self.buttonGroup_sysy.addButton(self.shengyinsiya_wu_RadioButton,14)
		self.buttonGroup_sysy.addButton(self.shengyinsiya_you_RadioButton,15)

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
		diagonosis.xingming = str(self.xingming_LineEdit.text().toUtf8())#LineEdit
		diagonosis.xingbie = str(self.xingbie_ComboBox.currentText().toUtf8())#ComboBox
		diagonosis.zhiye = str(self.zhiye_LineEdit.text().toUtf8())
		diagonosis.minzu = str(self.minzu_LineEdit.text().toUtf8())
		diagonosis.jiatingzhuzhi = str(self.jiatingzhuzhi_LineEdit.text().toUtf8())
		diagonosis.wenhuachengdu = str(self.wenhuachengdu_ComboBox.currentText().toUtf8())
		
		return diagonosis
		