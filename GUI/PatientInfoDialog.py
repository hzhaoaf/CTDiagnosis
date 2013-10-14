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
		
		self.buttonGroup_linbajiezhong= QButtonGroup()
		self.buttonGroup_linbajiezhong.addButton(self.linbajiezhong_wu_RadioButton,16)
		self.buttonGroup_linbajiezhong.addButton(self.linbajiezhong_you_RadioButton,17)
		
		self.buttonGroup_jiejiemidu= QButtonGroup()
		self.buttonGroup_jiejiemidu.addButton(self.jiejiemidu_bujunyun_RadioButton,18)
		self.buttonGroup_jiejiemidu.addButton(self.jiejiemidu_junyun_RadioButton,19)
		
		self.buttonGroup_maobolimi= QButtonGroup()
		self.buttonGroup_maobolimi.addButton(self.maobolimi_wu_RadioButton,20)
		self.buttonGroup_maobolimi.addButton(self.maobolimi_shi_RadioButton,21)
		
		self.buttonGroup_shixingjiejie= QButtonGroup()
		self.buttonGroup_shixingjiejie.addButton(self.shixingjiejie_wu_RadioButton,22)
		self.buttonGroup_shixingjiejie.addButton(self.shixingjiejie_shi_RadioButton,23)
		
		self.buttonGroup_jiejiebianyuan= QButtonGroup()
		self.buttonGroup_jiejiebianyuan.addButton(self.jiejiebianyuan_guanghua_RadioButton,24)
		self.buttonGroup_jiejiebianyuan.addButton(self.jiejiebianyuan_maocao_RadioButton,25)
		
		self.buttonGroup_youyunzheng= QButtonGroup()
		self.buttonGroup_youyunzheng.addButton(self.youyunzheng_wu_RadioButton,26)
		self.buttonGroup_youyunzheng.addButton(self.youyunzheng_you_RadioButton,27)
		
		self.buttonGroup_jiejiekongpao= QButtonGroup()
		self.buttonGroup_jiejiekongpao.addButton(self.jiejiekongpao_wu_RadioButton,28)
		self.buttonGroup_jiejiekongpao.addButton(self.jiejiekongpao_you_RadioButton,29)
		
		self.buttonGroup_jiejiefenye= QButtonGroup()
		self.buttonGroup_jiejiefenye.addButton(self.jiejiefenye_wu_RadioButton,30)
		self.buttonGroup_jiejiefenye.addButton(self.jiejiefenye_you_RadioButton,31)
		
		self.buttonGroup_kongdong= QButtonGroup()
		self.buttonGroup_kongdong.addButton(self.kongdong_wu_RadioButton,32)
		self.buttonGroup_kongdong.addButton(self.kongdong_you_RadioButton,33)
		
		self.buttonGroup_jiejiegaihua= QButtonGroup()
		self.buttonGroup_jiejiegaihua.addButton(self.jiejiegaihua_wu_RadioButton,34)
		self.buttonGroup_jiejiegaihua.addButton(self.jiejiegaihua_you_RadioButton,35)
		
		self.buttonGroup_xiongshui= QButtonGroup()
		self.buttonGroup_xiongshui.addButton(self.xiongshui_wu_RadioButton,36)
		self.buttonGroup_xiongshui.addButton(self.xiongshui_you_RadioButton,37)
		
		self.buttonGroup_xiongmoaoxian= QButtonGroup()
		self.buttonGroup_xiongmoaoxian.addButton(self.xiongmoaoxian_wuu_RadioButton,38)
		self.buttonGroup_xiongmoaoxian.addButton(self.xiongmoaoxian_you_RadioButton,39)			
		
	@pyqtSignature("QString")
	def on_xingming_LineEdit_textEdited(self, text):
		'''#Slot# : Once nameLienEdit is being edited,call this function'''
		self.updateUi()
		
	def updateUi(self):
		enable = not self.xingming_LineEdit.text().isEmpty()
		self.acceptButton.setEnabled(enable)
		
	def getDiagnosisInfo(self):
		'''Return the info filled by doctor'''
		diagonosis = UI_Diagnosis()
		
		#Tab1's content 个人信息
		diagonosis.xingming = str(self.xingming_LineEdit.text().toUtf8())#LineEdit
		diagonosis.xingbie = str(self.xingbie_ComboBox.currentText().toUtf8())#ComboBox
		diagonosis.zhiye = str(self.zhiye_LineEdit.text().toUtf8())
		diagonosis.minzu = str(self.minzu_LineEdit.text().toUtf8())
		diagonosis.jiatingzhuzhi = str(self.jiatingzhuzhi_LineEdit.text().toUtf8())
		diagonosis.wenhuachengdu = str(self.wenhuachengdu_ComboBox.currentText().toUtf8())
		#Tab2's content 既往史
		diagonosis.zhongliubingshicunzai = str(self.zhongliubingshi_ComboBox.currentText().toUtf8())
		diagonosis.zhongliubingshineirong = str(self.zhongliubingshi_PlainTextEdit.toPlainText().toUtf8())
		diagonosis.feijiehebingshicunzai = str(self.feijihebingshi_ComboBox.currentText().toUtf8())
		diagonosis.feijiehebingshineirong = str(self.feijiehebingshi_PlainTextEdit.toPlainText().toUtf8())
		diagonosis.fenchenxirushicunzai = str(self.fenchenxirushi_ComboBox.currentText().toUtf8())
		diagonosis.xirugongzuonianxian = str(self.xirugongzuonianxian_LineEdit.text().toUtf8())
		diagonosis.gongzhong = str(self.gongzhong_LineEdit.text().toUtf8())
		diagonosis.yichuanbingshicunzai = str(self.yichuanbingshi_ComboBox.currentText().toUtf8())
		diagonosis.yichuanbingshineirong = str(self.yichuanbingshi_PlainTextEdit.toPlainText().toUtf8())
		diagonosis.xiyanshicunzai = str(self.xiyanshi_ComboBox.currentText().toUtf8())
		diagonosis.xiyannianxian = str(self.xiyannianxian_LineEdit.text().toUtf8())
		diagonosis.meitianxiyanzhishu = str(self.meitianxiyanshu_LineEdit.text().toUtf8())
		diagonosis.huxibingshihuoqitacunzai = str(self.huxibingshihuoqita_ComboBox.currentText().toUtf8())
		diagonosis.huxibingshihuoqitaneirong = str(self.huxibingshihuoqita_PlainTextEdit.toPlainText().toUtf8())
		#Tab3's content 就诊信息
		diagonosis.zhusu = str(self.zhusu_PlainTextEdit.toPlainText().toUtf8())
		if self.fare_wu_RadioButton.isChecked():
			diagonosis.fare = "0" 
		elif self.fare_3738_RadioButton.isChecked():
			diagonosis.fare = '1'
		elif self.fare_38yishang_RadioButton.isChecked():
			diagonosis.fare = '2'
		diagonosis.kesou = "0" * self.kesou_wu_RadioButton.isChecked() + "1" * self.kesou_you_RadioButton.isChecked()
		diagonosis.tanzhongdaixue =  "0" * self.tanzhongdaixue_wu_RadioButton.isChecked() +\
		        "1" * self.tanzhongdaixue_you_RadioButton.isChecked()
		diagonosis.kexue  = "0" * self.kexue_wu_RadioButton.isChecked() + "1" * self.kexue_you_RadioButton.isChecked()
		diagonosis.xiongmen = "0" * self.xiongmen_wu_RadioButton.isChecked() + "1" * self.xiongmen_you_RadioButton.isChecked()
		diagonosis.xiongtong = "0" * self.xiongtong_wu_RadioButton.isChecked() + "1" * self.xiongtong_you_RadioButton.isChecked()
		diagonosis.shengyinsiya = "0" * self.shengyinsiya_wu_RadioButton.isChecked() + \
		        "1" * self.shengyinsiya_you_RadioButton.isChecked()
		diagonosis.qitayuhuxiyouguandelinchuangbiaoxian = str(self.qitayuhuxiyouguan_PlainTextEdit.toPlainText().toUtf8())
		diagonosis.linchuangzhenduanyijian = str(self.linchuangzhenduanyijian_PlainTextEdit.toPlainText().toUtf8())
		
		#Tab4's content 影像查看结果
		diagonosis.CThao = str(self.CThao_lineEdit.text().toUtf8())
		diagonosis.jianchafangshi = str(self.jianchafangshi_comboBox.currentText().toUtf8())
		diagonosis.jianchariqi = str(self.jianchariqi_dateEdit.text().toUtf8())
		diagonosis.jiejiedaxiao = str(self.jiejiedaxiao_lineEdit.text().toUtf8())
		diagonosis.jiejiebuwei = "|zuo_shang" * self.zuofeishangye_checkBox.isChecked() + \
		        "|zuo_xia" * self.zuofeixiaye_checkBox.isChecked() + \
		        "|you_shang" * self.youfeishangye_checkBox.isChecked() + \
		        "|you_zhong" * self.youfeizhongye_checkBox.isChecked() + \
		        "|you_xia" * self.youfeixiaye_checkBox.isChecked()
		diagonosis.linbajiezhong = "0" * self.linbajiezhong_wu_RadioButton.isChecked() +\
		        "1" * self.linbajiezhong_you_RadioButton.isChecked()
		diagonosis.jiejiemidu = "0" * self.jiejiemidu_junyun_RadioButton.isChecked() +\
		        "1" * self.jiejiemidu_bujunyun_RadioButton.isChecked()
		diagonosis.maobolimi = "0" * self.maobolimi_wu_RadioButton.isChecked() +\
		        "1" * self.maobolimi_shi_RadioButton.isChecked()
		diagonosis.shixingjiejie = "0" * self.shixingjiejie_wu_RadioButton.isChecked() +\
				        "1" * self.shixingjiejie_shi_RadioButton.isChecked()
		diagonosis.jiejiebianyuan = "0" * self.jiejiebianyuan_guanghua_RadioButton.isChecked() +\
				        "1" * self.jiejiebianyuan_maocao_RadioButton.isChecked()
		diagonosis.youyunzheng = "0" * self.youyunzheng_wu_RadioButton.isChecked() +\
				                        "1" * self.youyunzheng_you_RadioButton.isChecked()
		diagonosis.jiejiekongpao = "0" * self.jiejiekongpao_wu_RadioButton.isChecked() +\
		                                        "1" * self.jiejiekongpao_you_RadioButton.isChecked()
		diagonosis.jiejiefenye = "0" * self.jiejiefenye_wu_RadioButton.isChecked() +\
		                                        "1" * self.jiejiefenye_you_RadioButton.isChecked()			
		diagonosis.kongdong = "0" * self.kongdong_wu_RadioButton.isChecked() +\
		                                        "1" * self.kongdong_you_RadioButton.isChecked()
		diagonosis.jiejiegaihua = "0" * self.jiejiegaihua_wu_RadioButton.isChecked() +\
		                                        "1" * self.jiejiegaihua_you_RadioButton.isChecked()
		diagonosis.xiongshui = "0" * self.xiongshui_wu_RadioButton.isChecked() +\
		                                        "1" * self.xiongshui_you_RadioButton.isChecked()
		diagonosis.xiongmoaoxian = "0" * self.xiongmoaoxian_wuu_RadioButton.isChecked() +\
		                                        "1" * self.xiongmoaoxian_you_RadioButton.isChecked()
		diagonosis.CTzhenduan = str(self.CTzhenduan_plainTextEdit.toPlainText().toUtf8())

		return diagonosis