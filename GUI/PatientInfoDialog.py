# -*- coding: utf-8 -*-
import re
from PyQt4.QtCore import *
from PyQt4.QtGui import *
import PyQt4.QtGui
import ui_PatientInfoDialog
MAC = hasattr(PyQt4.QtGui, "qt_mac_set_native_menubar")
#Normally,we inherit the class created by QT Designer,not use it directly
from  gui_model_diagnosis import UI_Diagnosis
from append import qs2ps,ps2qs

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
		'''
		#Slot# : Once nameLienEdit is being edited,call this function
		'''
		self.updateUi()
		
	def updateUi(self):
		'''
		Always check if the necessary infos have been filled. If True,enable the accept button
		'''

		enable = not self.xingming_LineEdit.text().isEmpty()
		self.acceptButton.setEnabled(enable)
		
	def getDiagnosisInfo(self):
		'''
		Return the info filled by doctor
		'''
		diag = UI_Diagnosis()
		
		#Tab1's content 个人信息
		diag.xingming = str(self.xingming_LineEdit.text().toUtf8())#LineEdit
		diag.xingbie = str(self.xingbie_ComboBox.currentText().toUtf8())#ComboBox
		diag.zhiye = str(self.zhiye_LineEdit.text().toUtf8())
		diag.minzu = str(self.minzu_LineEdit.text().toUtf8())
		diag.jiatingzhuzhi = str(self.jiatingzhuzhi_LineEdit.text().toUtf8())
		diag.wenhuachengdu = str(self.wenhuachengdu_ComboBox.currentText().toUtf8())
		#Tab2's content 既往史
		diag.zhongliubingshicunzai = str(self.zhongliubingshi_ComboBox.currentText().toUtf8())
		diag.zhongliubingshineirong = str(self.zhongliubingshi_PlainTextEdit.toPlainText().toUtf8())
		diag.feijiehebingshicunzai = str(self.feijihebingshi_ComboBox.currentText().toUtf8())
		diag.feijiehebingshineirong = str(self.feijiehebingshi_PlainTextEdit.toPlainText().toUtf8())
		diag.fenchenxirushicunzai = str(self.fenchenxirushi_ComboBox.currentText().toUtf8())
		diag.xirugongzuonianxian = str(self.xirugongzuonianxian_LineEdit.text().toUtf8())
		diag.gongzhong = str(self.gongzhong_LineEdit.text().toUtf8())
		diag.yichuanbingshicunzai = str(self.yichuanbingshi_ComboBox.currentText().toUtf8())
		diag.yichuanbingshineirong = str(self.yichuanbingshi_PlainTextEdit.toPlainText().toUtf8())
		diag.xiyanshicunzai = str(self.xiyanshi_ComboBox.currentText().toUtf8())
		diag.xiyannianxian = str(self.xiyannianxian_LineEdit.text().toUtf8())
		diag.meitianxiyanzhishu = str(self.meitianxiyanshu_LineEdit.text().toUtf8())
		diag.huxibingshihuoqitacunzai = str(self.huxibingshihuoqita_ComboBox.currentText().toUtf8())
		diag.huxibingshihuoqitaneirong = str(self.huxibingshihuoqita_PlainTextEdit.toPlainText().toUtf8())
		#Tab3's content 就诊信息
		diag.zhusu = str(self.zhusu_PlainTextEdit.toPlainText().toUtf8())
		if self.fare_wu_RadioButton.isChecked():
			diag.fare = "0" 
		elif self.fare_3738_RadioButton.isChecked():
			diag.fare = '1'
		elif self.fare_38yishang_RadioButton.isChecked():
			diag.fare = '2'
		diag.kesou = "0" * self.kesou_wu_RadioButton.isChecked() + "1" * self.kesou_you_RadioButton.isChecked()
		diag.tanzhongdaixue =  "0" * self.tanzhongdaixue_wu_RadioButton.isChecked() +\
		        "1" * self.tanzhongdaixue_you_RadioButton.isChecked()
		diag.kexue  = "0" * self.kexue_wu_RadioButton.isChecked() + "1" * self.kexue_you_RadioButton.isChecked()
		diag.xiongmen = "0" * self.xiongmen_wu_RadioButton.isChecked() + "1" * self.xiongmen_you_RadioButton.isChecked()
		diag.xiongtong = "0" * self.xiongtong_wu_RadioButton.isChecked() + "1" * self.xiongtong_you_RadioButton.isChecked()
		diag.shengyinsiya = "0" * self.shengyinsiya_wu_RadioButton.isChecked() + \
		        "1" * self.shengyinsiya_you_RadioButton.isChecked()
		diag.qitayuhuxiyouguandelinchuangbiaoxian = str(self.qitayuhuxiyouguan_PlainTextEdit.toPlainText().toUtf8())
		diag.linchuangzhenduanyijian = str(self.linchuangzhenduanyijian_PlainTextEdit.toPlainText().toUtf8())
		
		#Tab4's content 影像查看结果
		diag.CThao = str(self.CThao_lineEdit.text().toUtf8())
		diag.jianchafangshi = str(self.jianchafangshi_comboBox.currentText().toUtf8())
		diag.jianchariqi = str(self.jianchariqi_dateEdit.text().toUtf8())
		diag.jiejiedaxiao = str(self.jiejiedaxiao_lineEdit.text().toUtf8())
		diag.jiejiebuwei = "|zuo_shang" * self.zuofeishangye_checkBox.isChecked() + \
		        "|zuo_xia" * self.zuofeixiaye_checkBox.isChecked() + \
		        "|you_shang" * self.youfeishangye_checkBox.isChecked() + \
		        "|you_zhong" * self.youfeizhongye_checkBox.isChecked() + \
		        "|you_xia" * self.youfeixiaye_checkBox.isChecked()
		diag.linbajiezhong = "0" * self.linbajiezhong_wu_RadioButton.isChecked() +\
		        "1" * self.linbajiezhong_you_RadioButton.isChecked()
		diag.jiejiemidu = "0" * self.jiejiemidu_junyun_RadioButton.isChecked() +\
		        "1" * self.jiejiemidu_bujunyun_RadioButton.isChecked()
		diag.maobolimi = "0" * self.maobolimi_wu_RadioButton.isChecked() +\
		        "1" * self.maobolimi_shi_RadioButton.isChecked()
		diag.shixingjiejie = "0" * self.shixingjiejie_wu_RadioButton.isChecked() +\
				        "1" * self.shixingjiejie_shi_RadioButton.isChecked()
		diag.jiejiebianyuan = "0" * self.jiejiebianyuan_guanghua_RadioButton.isChecked() +\
				        "1" * self.jiejiebianyuan_maocao_RadioButton.isChecked()
		diag.youyunzheng = "0" * self.youyunzheng_wu_RadioButton.isChecked() +\
				                        "1" * self.youyunzheng_you_RadioButton.isChecked()
		diag.jiejiekongpao = "0" * self.jiejiekongpao_wu_RadioButton.isChecked() +\
		                                        "1" * self.jiejiekongpao_you_RadioButton.isChecked()
		diag.jiejiefenye = "0" * self.jiejiefenye_wu_RadioButton.isChecked() +\
		                                        "1" * self.jiejiefenye_you_RadioButton.isChecked()			
		diag.kongdong = "0" * self.kongdong_wu_RadioButton.isChecked() +\
		                                        "1" * self.kongdong_you_RadioButton.isChecked()
		diag.jiejiegaihua = "0" * self.jiejiegaihua_wu_RadioButton.isChecked() +\
		                                        "1" * self.jiejiegaihua_you_RadioButton.isChecked()
		diag.xiongshui = "0" * self.xiongshui_wu_RadioButton.isChecked() +\
		                                        "1" * self.xiongshui_you_RadioButton.isChecked()
		diag.xiongmoaoxian = "0" * self.xiongmoaoxian_wuu_RadioButton.isChecked() +\
		                                        "1" * self.xiongmoaoxian_you_RadioButton.isChecked()
		diag.CTzhenduan = str(self.CTzhenduan_plainTextEdit.toPlainText().toUtf8())

		return diag
	
#Constant variables for select the item of combobutton
T_SEX = 0
T_CULDEGREE = 1
T_HISTORY = 2
T_SCANTYPE = 3
INDEXS_CONTENTS = [[u"男",u"女"],
          [u"大学以上",u"大学",u"高中",u"初中",u"小学","文盲或半文盲"],
          [u"无",u"有",u"不详"],
          [u"平扫",u"增强扫描",u"其他"]]

class PatientInfoReadOnlyDialog(PatientInfoDialog):
	def __init__(self,diagnosis,text=None,parent=None):
		#child inherits from father call the __init__ explicitly http://bestchenwu.iteye.com/blog/1044848
		super(PatientInfoReadOnlyDialog,self).__init__(text,parent)
		self._diagnosis = diagnosis
		self.set_dialog_info(self._diagnosis)
		
		self.acceptButton.setEnabled(True)
		
	def _set_check(self,value,radio_button_1,radio_button_2):
		if value.decode('utf8') == u"0":
			radio_button_1.setChecked(True)
		else:
			radio_button_2.setChecked(True)
		
	def _get_index(self,value,tag):
		for index,deg in enumerate(INDEXS_CONTENTS[tag]):
			if value.decode('utf8') == deg:
				return index
		return 0			
		
	def set_dialog_info(self,diagnosis):
		#Tab1's content 个人信息
		self.xingming_LineEdit.setText(diagnosis.xingming.decode('utf8'))
		
		xingbie_index = 0 + 1 * (diagnosis.xingbie.decode('utf8') == u"女")
		self.xingbie_ComboBox.setCurrentIndex(xingbie_index)
		
		self.zhiye_LineEdit.setText(diagnosis.zhiye.decode('utf8'))
		self.minzu_LineEdit.setText(diagnosis.minzu.decode('utf8'))
		self.jiatingzhuzhi_LineEdit.setText(diagnosis.jiatingzhuzhi.decode('utf8'))
		
		self.wenhuachengdu_ComboBox.setCurrentIndex(self._get_index(diagnosis.wenhuachengdu,T_CULDEGREE))
		
		#Tab2's content 既往史
		self.zhongliubingshi_ComboBox.setCurrentIndex(self._get_index(diagnosis.zhongliubingshicunzai,T_HISTORY))
		self.zhongliubingshi_PlainTextEdit.setPlainText(diagnosis.zhongliubingshineirong.decode('utf8'))
		
		self.feijihebingshi_ComboBox.setCurrentIndex(self._get_index(diagnosis.feijiehebingshicunzai,T_HISTORY))
		self.feijiehebingshi_PlainTextEdit.setPlainText(diagnosis.feijiehebingshineirong.decode('utf8'))

		self.fenchenxirushi_ComboBox.setCurrentIndex(self._get_index(diagnosis.fenchenxirushicunzai,T_HISTORY))
		self.xirugongzuonianxian_LineEdit.setText(diagnosis.xirugongzuonianxian.decode('utf8'))
		self.gongzhong_LineEdit.setText(diagnosis.gongzhong.decode('utf8'))
		
		self.yichuanbingshi_ComboBox.setCurrentIndex(self._get_index(diagnosis.yichuanbingshicunzai,T_HISTORY))
		self.yichuanbingshi_PlainTextEdit.setPlainText(diagnosis.yichuanbingshineirong.decode('utf8'))
		
		self.xiyanshi_ComboBox.setCurrentIndex(self._get_index(diagnosis.xiyanshicunzai,T_HISTORY))
		self.xiyannianxian_LineEdit.setText(diagnosis.xiyannianxian.decode('utf8'))	
		self.meitianxiyanshu_LineEdit.setText(diagnosis.meitianxiyanzhishu.decode('utf8'))	

		self.huxibingshihuoqita_ComboBox.setCurrentIndex(self._get_index(diagnosis.huxibingshihuoqitacunzai,T_HISTORY))
		self.huxibingshihuoqita_PlainTextEdit.setPlainText(diagnosis.huxibingshihuoqitaneirong.decode('utf8'))
		
		#Tab3's content 就诊信息
		self.zhusu_PlainTextEdit.setPlainText(diagnosis.zhusu.decode('utf8'))

		_fare = diagnosis.fare.decode('utf8')
		if  _fare == u"0" :
			self.fare_wu_RadioButton.setChecked(True)
		elif _fare == u"1" :
			self.fare_3738_RadioButton.setChecked(True)
		else :
			self.fare_38yishang_RadioButton.setChecked(True)
			
		self._set_check(diagnosis.kesou,self.kesou_wu_RadioButton,self.kesou_you_RadioButton)
		self._set_check(diagnosis.tanzhongdaixue,self.tanzhongdaixue_wu_RadioButton,self.tanzhongdaixue_you_RadioButton)
		self._set_check(diagnosis.kexue,self.kexue_wu_RadioButton,self.kexue_you_RadioButton)
		self._set_check(diagnosis.xiongmen,self.xiongmen_wu_RadioButton,self.xiongmen_you_RadioButton)
		self._set_check(diagnosis.xiongtong,self.xiongtong_wu_RadioButton,self.xiongtong_you_RadioButton)
		self._set_check(diagnosis.shengyinsiya,self.shengyinsiya_wu_RadioButton,self.shengyinsiya_you_RadioButton)		
		
		self.qitayuhuxiyouguan_PlainTextEdit.setPlainText(diagnosis.qitayuhuxiyouguandelinchuangbiaoxian.decode('utf8'))
		self.linchuangzhenduanyijian_PlainTextEdit.setPlainText(diagnosis.linchuangzhenduanyijian.decode('utf8'))
		
		#Tab4's content 影像查看结果
		self.CThao_lineEdit.setText(diagnosis.CThao.decode('utf8'))
		self.jianchafangshi_comboBox.setCurrentIndex(self._get_index(diagnosis.jianchafangshi,T_SCANTYPE))
		(year,month,day) = diagnosis.jianchariqi.decode('utf8').split()[0].split('/')
		self.jianchariqi_dateEdit.setDate(QDate(int(year),int(month),int(day)))
		
		self.jiejiedaxiao_lineEdit.setText(diagnosis.jiejiedaxiao.decode('utf8'))
		if diagnosis.jiejiebuwei.decode('utf8').find(u"zuo_shang"):
			self.zuofeishangye_checkBox.setChecked(True)
			#to do ,not finished yet
		
		self._set_check(diagnosis.linbajiezhong,self.linbajiezhong_wu_RadioButton,self.linbajiezhong_you_RadioButton)
		self._set_check(diagnosis.jiejiemidu,self.jiejiemidu_junyun_RadioButton,self.jiejiemidu_bujunyun_RadioButton)
		self._set_check(diagnosis.maobolimi,self.maobolimi_wu_RadioButton,self.maobolimi_shi_RadioButton)
		self._set_check(diagnosis.shixingjiejie,self.shixingjiejie_wu_RadioButton,self.shixingjiejie_shi_RadioButton)
		self._set_check(diagnosis.jiejiebianyuan,self.jiejiebianyuan_guanghua_RadioButton,self.jiejiebianyuan_maocao_RadioButton)		
		self._set_check(diagnosis.youyunzheng,self.youyunzheng_wu_RadioButton,self.youyunzheng_you_RadioButton)
		self._set_check(diagnosis.jiejiekongpao,self.jiejiekongpao_wu_RadioButton,self.jiejiekongpao_you_RadioButton)
		self._set_check(diagnosis.jiejiefenye,self.jiejiefenye_wu_RadioButton,self.jiejiefenye_you_RadioButton)			
		self._set_check(diagnosis.kongdong,self.kongdong_wu_RadioButton,self.kongdong_you_RadioButton)
		self._set_check(diagnosis.jiejiegaihua,self.jiejiegaihua_wu_RadioButton,self.jiejiegaihua_you_RadioButton)		
		self._set_check(diagnosis.xiongshui,self.xiongshui_wu_RadioButton,self.xiongshui_you_RadioButton)
		self._set_check(diagnosis.xiongmoaoxian,self.xiongmoaoxian_wuu_RadioButton,self.xiongmoaoxian_you_RadioButton)

		self.CTzhenduan_plainTextEdit.setPlainText(diagnosis.CTzhenduan.decode('utf8'))
				