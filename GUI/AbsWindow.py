# -*- coding: utf-8 -*-

import os
import sys

from sklearn.utils import weight_vector,lgamma
from sklearn.decomposition import PCA, FastICA
from sklearn.pls import PLSRegression

from skimage import transform,graph,draw
from skimage._shared import geometry,interpolation,transform
from skimage._shared import *

import time
from PyQt4 import QtGui, QtCore
from PyQt4.QtCore import Qt
from PyQt4.QtCore import QRect,QString
from ImageView import ImageView

from Image import Image
from append import *
from svm import SVM
sys.path.append("..")
from Curvelet import ccf
from scipy import misc
from PatientInfoDialog import PatientInfoDialog,PatientInfoReadOnlyDialog
from ShowResultDialog import ShowResultDialog
from DiagnosisListDialog import DiagnosisListDlg

from gui_model_diagnosis import UI_Diagnosis
from ImageControlWidget import ImageControlWidget
from ImageHelper import ImageItemsList
from RegionGrow.reseg import RegionGrow
from gui_constants import *
from gui_dal import GUIDAL
import traceback


#class MainWindow(QtGui.QWidget):
class AbsWindow(QtGui.QMainWindow):
	def __init__(self,parent = None,img_save_path =  '../data/images/'):
		#Set up the style of the main window
		super(AbsWindow, self).__init__(parent)
		self.setGeometry(40,40,960,720)
		self.setWindowTitle(WINDOWTITLE)
		icon = u"plus_24x24"
		self.setWindowIcon(QtGui.QIcon("./icon/%s.png" % icon))
		self.status_bar = self.statusBar()
		self.status_bar.showMessage(WELCOME)
		self.busy_indicator = QtGui.QProgressDialog(labelText=u'计算中，请等待...',minimum = 0, maximum = 100)
		
		#上下结构，上面是imageview，下面是imagecontrolwidget
		#-abswindow 
		#   --spliter
		#      --imageview
		#      --imagecontrolwidget
		self.main=ImageView(self)
		self.image_control_widget = ImageControlWidget(parent=self)
		splitter = QtGui.QSplitter(self)
		splitter.addWidget(self.main)
		splitter.addWidget(self.image_control_widget)
		splitter.setOrientation(Qt.Vertical)
		self.setCentralWidget(splitter)
		self.createMenus()#创建菜单
		self.setMouseStyleCross()#将鼠标设置成十字的
		self.image_file_path = img_save_path#The path to save the image
		#Initialize attributes
		self.guidal = GUIDAL()
		self.svmModel = SVM()
		self.region_grow_module = RegionGrow()
		self.reset_attribute()#Initialize
		
	def reset_attribute(self):
		self.image_item_list = ImageItemsList()#Hold all the images
		self.diagonosis_info = None#The info (patients info ,images,predictions)
		self.imgNameSuffix = 1#names of image starts from 001 to 999
		#self.reload_cur_image()
		
	def setMouseStyleCross(self):
		'''Set the mouse style to cross +'''
		self.main.setCursor(Qt.CrossCursor)
	def setMouseStyleNormal(self):
		'''Set the mouse style to normal'''
		self.main.setCursor(Qt.ArrowCursor)
		
	#def createToolBar(self):
		#exit = QtGui.QAction(QtGui.QIcon('icons/web.png'), 'Exit', self)
		
	def createMenus(self):
		'''Initialize and create menus,actions,toolbar'''
		fileOpenAction = self.createAction(u"导入图像", self.load,
				QtGui.QKeySequence.Open, "document_stroke_24x24",
				u"导入图像文件")
		cropImageAction = self.createAction(u"&裁剪...", self.crop,icon="fullscreen_alt_24x24",tip = u"裁剪图像")
		svmGuessAction = self.createAction(u"预测", self.curveletExtract,tip = u"分析图像患病概率",
		                                   icon="check_alt_24x24")
		shPaInfoDialAction = self.createAction(u"输入患者信息...", \
		                                       self.showPatientInfoDialog,tip = u"输入患者信息",
		                                       icon="user_18x24")
		
		selectDiagonosisAction = self.createAction(u"查询诊断信息...", \
				                                       self.show_select_diagonosis_dialog,tip = u"查询诊断信息",
		                                                       icon="magnifying_glass_alt_24x24")		

		nextImageAction = self.createAction(u"&下一张...", 
		                                    self.nextImage,tip = u"下一张图像",
		                                    shortcut=QtGui.QKeySequence.MoveToNextChar,
		                                    icon="arrow_right_24x24")
		previousImageAction = self.createAction(u"&上一张...", 
		                                    self.previousImage,tip = u"上一张图像",
		                                    shortcut=QtGui.QKeySequence.MoveToPreviousChar,
		                                    icon = "arrow_left_24x24")	
		
		resetImageAction = self.createAction(u"重置图像...", 
		                                    self.reset_current_image,tip = u"重置图像",
		                                    icon = "reload_24x28")	
		
		
		self.toolbar = self.addToolBar("Tools")
		self.toolbar.addAction(fileOpenAction)
		
		self.toolbar.addAction(shPaInfoDialAction)
		self.toolbar.addAction(selectDiagonosisAction)
		self.toolbar.addSeparator()

		self.toolbar.addAction(previousImageAction)
		self.toolbar.addAction(nextImageAction)
		self.toolbar.addAction(cropImageAction)
		self.toolbar.addAction(resetImageAction)
		self.toolbar.addSeparator()
		
		self.toolbar.addAction(svmGuessAction)

		self.fileMenu = self.menuBar().addMenu(u"文件")
		self.imgMenu = self.menuBar().addMenu(u"图像")
		self.funcMenu = self.menuBar().addMenu(u"功能")
		
		self.fileMenuActions = [fileOpenAction,shPaInfoDialAction,selectDiagonosisAction]
		self.imgMenuActions = [previousImageAction,nextImageAction,cropImageAction,resetImageAction]
		self.funcMenuActions = [svmGuessAction]
		
		self.addAction(fileOpenAction)
		self.addAction(cropImageAction)
		self.addAction(svmGuessAction)
		self.addAction(nextImageAction)
		self.addAction(previousImageAction)
		self.addAction(shPaInfoDialAction)
		self.addAction(selectDiagonosisAction)
		self.addAction(resetImageAction)
		
		self.fileMenu.clear()
		self.imgMenu.clear()
		self.funcMenu.clear()
		
		self.addActions(self.fileMenu, self.fileMenuActions[:])
		self.addActions(self.imgMenu, self.imgMenuActions[:])
		self.addActions(self.funcMenu, self.funcMenuActions[:])
		
		
	def addActions(self, target, actions):
		'''Reload the function'''
		for action in actions:
			if action is None:
				target.addSeparator()
			else:
				target.addAction(action)	
				
	def createAction(self, text, slot=None, shortcut=None, icon=None,tip=None, checkable=False, signal="triggered()"):
		'''A helper function to create an GUI action'''
		action = QtGui.QAction(text, self)
		if icon is not None:
			action.setIcon(QtGui.QIcon("./icon/%s.png" % icon))
		if shortcut is not None:
			action.setShortcut(shortcut)
		if tip is not None:
			action.setToolTip(tip)
			action.setStatusTip(tip)
		if slot is not None:
			self.connect(action, QtCore.SIGNAL(signal), slot)
		if checkable:
			action.setCheckable(True)
		#if icon:
			#action.setIcon(icon)
		return action
	
	def getImage(self):
		'''Return displayed image'''
		i = self.main.getImage()
		return i

	def openFile(self,name):
		'''Open image with given name'''
		if not self.main.loadImage(name):
			print("[Abswindow]:Image null %s "% name)
			return
		#self.setTitle() 
		self.postOp(self.getImage(),False)
		
	def postOp(self,i,doUpdate= True):
		'''Function to call after performing an operation.Redraw the image and handle any errors'''
		'''i Image that was processed'''
		'''doUpdate If true, update image on screen.
				 In some operations it may be unnecessary to update, like if the image was not modified,
				 or if the update is done in other way. Default is to update'''
		self.main.cancelRect()#Will ensure that updateMenus() will be called in the process
		if  doUpdate:self.main.update()
		self.update_image_control_state()
		
	#def reloadImageAfterCrop(self):
		#'''After Crop,set the image to None'''
		#del self.images_tuple[self.curImgNo][0]
		#if not self.iamgePaths:
			#if self.main.image: del self.main.image
			#self.main.image = None
			#return
		#else:
			#self.openFile(self.images_tuple[0][0])#Show first image
			#self.curImgNo = 0
		
	def reload_cur_image(self):
		'''
		Reload the image.Ask for which image to show and open that image.
		call this in crop,region grow and reset
		'''
		file_path = self.image_item_list.get_current_image_file()
		if file_path:
			self.openFile(file_path)#Show first image
			
	def load(self):
		'''Action 1'''
		'''Open image without given name'''
		img_paths = openFileDialog(self,QString(u"打开图片"),QString(),self.filters(),QString())#TEmp
		if not img_paths:
			return
		
		self.image_item_list.init_list(img_paths)
		file_path = self.image_item_list.get_current_image_file()
		if file_path:
			self.openFile(file_path)#Show first image
			
		self.imgNamePrefix = qs2ps(QtCore.QDateTime.currentDateTime().toString("yyMMdd_hhmmss"))
		#PyQt4.QtCore.QString(u'131029_143236')
		
	def previousImage(self):
		'''Show the last Image if there is'''
		prev_image_file_path = self.image_item_list.get_prev_image_file_name()
		if prev_image_file_path:
			self.openFile(prev_image_file_path)
		else:
			print('No previous image!')
			self.status_bar.showMessage(u"没有上一张图像",5000)

	def nextImage(self):
		'''Show the next Image if there is'''
		next_image_file_path = self.image_item_list.get_next_image_file_name()
		if next_image_file_path:
			self.openFile(next_image_file_path)
		else:
			print('No next image!')
			self.status_bar.showMessage(u"没有下一张图像",5000)
		
	def filters(self,useGeneric = None,useBareFormat=None):
		'''Return suggested filters to use in a save/load dialog'''
		out = QtCore.QStringList()
		out << "Dicom (*.dcm *.dicom)"
		out << "PNG (*.png)"
		out << "BMP (*.bmp)"
		out << "JPEG (*.jpg *.jpeg)"
		return out
	
	def getImage(self):
		'''Return displayed image Print out error message if no image is loaded'''
		i=self.main.getImage()
		if not i:
			pass
			#cmdLine->addError(tr("No image is loaded"));
		return i
	
	def change_image_in_use_state(self,able):
		self.image_item_list.do_enable_current_image(able)
		
	def update_image_control_state(self):
		able = self.image_item_list.is_current_image_in_use()
		self.image_control_widget.set_in_use_checked(able)
		
	def save_after_regiongrow(self,img):
		'''Save image after regiongrow.'''
		i=self.getImage()
		if not i: return
		_pfileName="%s%s%03d_croped_regiongrowed.png" % (self.image_file_path,self.imgNamePrefix,self.imgNameSuffix)
		fileName = ps2qs(_pfileName)
		self.imgNameSuffix+=1
		#self.main.saveImage(fileName)
		misc.imsave(_pfileName,img)
		
		self.image_item_list.do_current_image_regiongrow(fileName)#set the cropped image's name to the image_item_list
		self.reload_cur_image()
		self.postOp(i,False)
		
	def save_after_crop(self):
		'''Save image after cropped.'''
		i=self.getImage()
		if not i: return
		_pfileName="%s%s%03d_cropped.png" % (self.image_file_path,self.imgNamePrefix,self.imgNameSuffix)
		fileName = ps2qs(_pfileName)
		self.imgNameSuffix+=1
		
		if not self.main.saveImage(fileName):
			_showed_message =u"[保存失败]%s 文件" % (_pfileName)
			self.status_bar.showMessage(_showed_message,5000)
			return False
		
		self.postOp(i,False)
		self.image_item_list.do_current_image_crop(fileName)#set the cropped image's name to the image_item_list
		
		_showed_message =u"裁剪成功，保存到 %s 文件" % (_pfileName)
		self.status_bar.showMessage(_showed_message,5000)
		return True

	def crop(self):
		#A rectangle is normally expressed as an upper-left corner and a size
		'''Crop image _QStringList param  Command parameters'''
		i=self.getImage()#param)
		if not i: 
			print("No image to crop & save")
			self.status_bar.showMessage(u"当前没有图像，不能进行裁剪操作",5000)
			return
		rectan = self.main.getSelection()
		if not rectan:
			print("No selection for this image")
			self.status_bar.showMessage(u"没有选择矩形区域，不能进行裁剪操作",5000)
			return

		#print(QRect(rectan.left(), rectan.top(), rectan.width(), rectan.height()))
		i.crop(rectan.left(), rectan.top(), rectan.width(), rectan.height())
		
		if not self.save_after_crop():#Save immediately after crop
			return
		#not filp to next image
		#self.reloadImageAfterCrop()
		self.reload_cur_image()
		self.postOp(i)
		self.status_bar.showMessage(u"按住alt键，选择种子点，对图像进行区域生长算法")
		
		
		
	def cleanAfterPredict(self):
		'''To do:Clean the context'''
		#cropped Images
		#curImgNo
		#imgSavedNumber
		pass
	
	def region_grow(self,point):
		'''Doctor push the region grow button'''
		i=self.getImage()
		if not i:
			print("No image to region_grow")
			self.status_bar.showMessage(u"没有图像来进行区域生长")
			return
		
		_threshold = self.image_control_widget.get_threshold_value()#Get the current user setting of the threshold
		
		self.show_busy_indicator_progress()#---------------------Start- Compute---------------------------
		
		_qcur_img_file = self.image_item_list.get_current_image_file()
		cur_img_file = qs2ps(_qcur_img_file)
		img = misc.imread(cur_img_file)
		if not len(img.shape) == 2:
			img= img[:,:,0] if img.shape[2] > 1 else img
		
		print "[Region Grow]\n[Image]%s\n[Shape]:%r\n[Pos]:%r:" % (_qcur_img_file,img.shape,point)
		img = self.region_grow_module.getRegionGrowImage(img,(point.x(),point.y()),_threshold)
		self.save_after_regiongrow(img)
		
		self.cancel_busy_indicator_progress()#-------------------ENd---Compute---------------------------
	
		
	def curveletExtract(self):
		'''Extract the curvelet from given image name'''
		all_image_paths = self.image_item_list.get_all_enable_images_path()
		if not all_image_paths:
			print("No images to extract curvelet features")
			self.status_bar.showMessage(u"没有图像来进行预测")
			return
		
		if not self.diagonosis_info:
			print("No Info to extract curvelet features")
			self.status_bar.showMessage(u"没有输入患者信息来进行预测")			
			return
		
		image_features_dic = {}#{'../data/images/131102_110830004_croped_regiongrowed.png':[6.9639934,2,23]}
		for _qname in all_image_paths:
			name = qs2ps_for_path(_qname)
			#name = qs2ps(_qname)
			XX = misc.imread(name)
			#If it's a gray image, shape of XX would be 2d ,sth like (73,63)
			if len(XX.shape) == 2:
				pass
			else:
				XX= XX[:,:,0] if XX.shape[2] > 1 else XX#if RGB,only tackle R
			[MEAN,SD,CT,HG,MP,ENG,INE,IDM,ENT,COR,SM,DM,SE,DE,ANGLES] = ccf.ccf(XX)
			results = ccf.ccf(XX)
			vec = []
			for r in results[:-1]:#The last item has 3 cells
				vec+= r
			
			image_features_dic[name] = vec
			
		self.svmPredict(image_features_dic)

	def svmPredict(self,image_features_dic):
		'''Predict the probability of a feature'''
		patient_info_feature_list = self.diagonosis_info.convert_to_predictDiagnosis().convert_to_list()
		(p_with,p_without) = self.svmModel.predict(patient_info_feature_list,image_features_dic)
		#p_with,p_without = 1,0
		self.diagonosis_info.set_probability(str(p_with),str(p_without))#set the probability attribute
		patien_info_dic = self.diagonosis_info.convert_to_dict()
		
		self.show_result_dialog_and_savetodatavase(p_with,p_without,patien_info_dic,patient_info_feature_list,image_features_dic)

	def show_result_dialog_and_savetodatavase(self,p_with,p_without,patien_info_dic,patient_info_feature_list,image_features_dic):
		'''Show the prediction result,with buttons the confirm the result'''
		form = ShowResultDialog(parent=self,predict_value1=p_with,predict_value2=p_without)
		if form.exec_():
			#If doctor confirms the diagnosis,add new test cases and save .else, just save 
			label = -1
			add_to_traning = False
			sure_value = form.get_sure_value()
			if sure_value == 1:#Yes,youbing
				label = 1
				add_to_traning = True
			elif sure_value == 2:#No,meibing
				label = 0
				add_to_traning = True
				
			#save it into database		
			try:
				self.guidal.save_diagnosis_record(patien_info_dic,
					                          patient_info_feature_list,
					                          image_features_dic,
					                          (p_with,p_without),
					                          label,
					                          add_to_traning)
			except Exception as e:
				print "Database save error %s" % e
				traceback.print_exc()			
		self.cleanAfterPredict()

	def showPatientInfoDialog(self):
		#http://stackoverflow.com/questions/5874025/pyqt4-how-to-show-a-modeless-dialog
		#If you don't pass the self argument,it will be recycled by garbage collector!
		'''Show the disgnosis input window and let the doctor to type in infos'''
		form = PatientInfoDialog(parent=self)
		if form.exec_():
			self.diagonosis_info = form.getDiagnosisInfo()
			print(self.diagonosis_info)
		
	def show_select_diagonosis_dialog(self):
		'''Just for test'''
		all_diagnosis = self.guidal.get_all_diagnosis_info()# [[id,张三，13-02-01，98%，100%],[],[]]
		form = DiagnosisListDlg( u"过往诊断", all_diagnosis)
		if form.exec_():
			pass
			#print "\n".join([unicode(x) for x in form.stringlist])		
			
	def show_patientinfo_readonly_dialog(self,diagnosis_to_show):
		'''Create and show readonly diagnosis info Dialog window'''
		form = PatientInfoReadOnlyDialog(diagnosis_to_show)
		if form.exec_():
			print("finish showing the read only diagnosis")
			
	def show_busy_indicator_progress(self):
		'''Show the loading window'''
		self.busy_indicator.reset()
		self.busy_indicator.show()
		for i in range(30):
			self.busy_indicator.setValue(i)
			time.sleep(0.02)
	
	def cancel_busy_indicator_progress(self):
		'''Close the loading... window'''
		for i in range(70,100):
			self.busy_indicator.setValue(i)
			time.sleep(0.05)
		self.busy_indicator.cancel()
		
	def reset_current_image(self):
		'''
		Reset the image,change the cropped or region growed image to the original image.
		'''
		i=self.getImage()#param)
		if not i: 
			print("No image reset")
			self.status_bar.showMessage(u"当前没有图像，无需重置",5000)
			return
		
		self.image_item_list.do_reset_current_image()#set the current image to original one.
		self.reload_cur_image()
		self.postOp(None,False)
