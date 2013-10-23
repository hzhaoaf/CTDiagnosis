# -*- coding: utf-8 -*-

from PyQt4 import QtGui, QtCore
from PyQt4.QtCore import Qt
from PyQt4.QtCore import QRect,QString
from ImageView import ImageView
from Image import Image
from append import *
import sys
sys.path.append("..")
from svm.svm import SVM
from Curvelet import ccf
from scipy import misc
from PatientInfoDialog import PatientInfoDialog
from ShowResultDialog import ShowResultDialog
from gui_model_diagnosis import UI_Diagnosis
from ImageControlWidget import ImageControlWidget
from ImageHelper import ImageItemsList
from RegionGrow.reseg import RegionGrow

#class MainWindow(QtGui.QWidget):
class AbsWindow(QtGui.QMainWindow):
	def __init__(self,parent = None,img_save_path =  '../data/images/'):
		#Set up the style of the main window
		super(AbsWindow, self).__init__(parent)
		self.setGeometry(40,40,880,660)
		
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
		
		#Initialize attributes
		self.svmModel = SVM()
		self.region_grow_module = RegionGrow()
		self.image_item_list = ImageItemsList()#Hold all the images
		self.image_file_path = img_save_path#The path to save the image
		self.diagonosis = None#The info (patients info ,images,predictions)
		self.imgNameSuffix = 1#names of image starts from 001 to 999

	def setMouseStyleCross(self):
		self.main.setCursor(Qt.CrossCursor)
	def setMouseStyleNormal(self):
		self.main.setCursor(Qt.ArrowCursor)
	def createToolBar(self):
		exit = QtGui.QAction(QtGui.QIcon('icons/web.png'), 'Exit', self)
		
	def createMenus(self):
		fileOpenAction = self.createAction(u"打开", self.load,
				QtGui.QKeySequence.Open, "open",
				u"打开新的图像文件")
		cropImageAction = self.createAction(u"&裁剪...", self.crop,icon="crop",tip = u"裁剪图像")
		svmGuessAction = self.createAction(u"&Magic...", self.curveletExtract,tip = u"分析图像患病概率",
		                                   icon="svmPredict")
		shPaInfoDialAction = self.createAction(u"&输入患者信息...", \
		                                       self.showPatientInfoDialog,tip = u"输入患者信息",
		                                       icon="info")
		
		selectDiagonosisAction = self.createAction(u"&查询诊断信息...", \
				                                       self.show_select_diagonosis_dialog,tip = u"查询诊断信息",
		                                                       icon="zoom_in")		

		nextImageAction = self.createAction(u"&下一张...", 
		                                    self.nextImage,tip = u"下一张图像",
		                                    shortcut=QtGui.QKeySequence.MoveToNextChar,
		                                    icon="next")
		previousImageAction = self.createAction(u"&上一张...", 
		                                    self.previousImage,tip = u"上一张图像",
		                                    shortcut=QtGui.QKeySequence.MoveToPreviousChar,
		                                    icon = "prev")	
		
		self.toolbar = self.addToolBar("Tools")
		self.toolbar.addAction(fileOpenAction)
		self.toolbar.addAction(cropImageAction)
		self.toolbar.addAction(shPaInfoDialAction)
		self.toolbar.addAction(selectDiagonosisAction)
		self.toolbar.addAction(previousImageAction)
		self.toolbar.addAction(nextImageAction)
		self.toolbar.addAction(svmGuessAction)

		self.fileMenu = self.menuBar().addMenu(u"文件")
		self.imgMenu = self.menuBar().addMenu(u"图像")
		self.funcMenu = self.menuBar().addMenu(u"功能")
		
		self.fileMenuActions = [fileOpenAction,selectDiagonosisAction]
		self.imgMenuActions = [cropImageAction]
		self.funcMenuActions = [svmGuessAction,shPaInfoDialAction]
		
		self.addAction(fileOpenAction)
		self.addAction(cropImageAction)
		self.addAction(svmGuessAction)
		self.addAction(nextImageAction)
		self.addAction(previousImageAction)
		self.addAction(shPaInfoDialAction)
		self.addAction(selectDiagonosisAction)
		
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
		self.main.loadImage(name)
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
		file_path = self.image_item_list.get_current_image_file()
		if file_path:
			self.openFile(file_path)#Show first image
			
	def load(self):
		'''Action 1'''
		'''Open image without given name'''
		img_paths = openFileDialog(self,QString("Open Image"),QString(),self.filters(),QString())#TEmp
		if not img_paths:
			return
		
		self.image_item_list.init_list(img_paths)
		file_path = self.image_item_list.get_current_image_file()
		if file_path:
			self.openFile(file_path)#Show first image
			
		self.imgNamePrefix = "201309011030_001_"
		
	def previousImage(self):
		'''Show the last Image if there is'''
		prev_image_file_path = self.image_item_list.get_prev_image_file_name()
		if prev_image_file_path:
			self.openFile(prev_image_file_path)
		else:
			print('No previous image!')

	def nextImage(self):
		'''Show the next Image if there is'''
		next_image_file_path = self.image_item_list.get_next_image_file_name()
		if next_image_file_path:
			self.openFile(next_image_file_path)
		else:
			print('No next image!')
		
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
		
		self.main.saveImage(fileName)
		self.postOp(i,False)
		self.image_item_list.do_current_image_crop(fileName)#set the cropped image's name to the image_item_list

	def crop(self):
		#A rectangle is normally expressed as an upper-left corner and a size
		'''Crop image _QStringList param  Command parameters'''
		i=self.getImage()#param)
		if not i: 
			print("No image to crop & save")
			return
		rectan = self.main.getSelection()
		if not rectan:
			print("No selection for this image")
			return

		#print(QRect(rectan.left(), rectan.top(), rectan.width(), rectan.height()))
		i.crop(rectan.left(), rectan.top(), rectan.width(), rectan.height())
		
		self.save_after_crop()#Save immediately after crop
		#not filp to next image
		#self.reloadImageAfterCrop()
		self.reload_cur_image()
		self.postOp(i)
		
		
		
	def cleanAfterPredict(self):
		'''To do:Clean the context'''
		#cropped Images
		#curImgNo
		#imgSavedNumber
		pass
	
	def region_grow(self,point):
		i=self.getImage()
		if not i:
			print("No image to region_grow")
			return			
		
		_qcur_img_file = self.image_item_list.get_current_image_file()
		cur_img_file = qs2ps(_qcur_img_file)
		img = misc.imread(cur_img_file)
		if not len(img.shape) == 2:
			img= img[:,:,0] if img.shape[2] > 1 else img
		
		print "[Region Grow]\n[Image]%s\n[Shape]:%r\n[Pos]:%r:" % (_qcur_img_file,img.shape,point)
		img = self.region_grow_module.getRegionGrowImage(img,(point.x(),point.y()))
		self.save_after_regiongrow(img)
		
	def curveletExtract(self):
		'''Extract the curvelet from given image name'''
		all_image_paths = self.image_item_list.get_all_enable_images_path()
		if not all_image_paths:
			print("No images to extract curvelet features")
			return
		
		vecList = []
		for _qname in all_image_paths:
			name = qs2ps(_qname)
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
			vecList.append(vec)
		self.svmPredict(vecList)
		
		self.cleanAfterPredict()
		
	def svmPredict(self,vectorList):
		'''Predict the probability of a feature'''
		predict_value = self.svmModel.predict(vectorList)
		self.show_result_dialog(predict_value)
	
	def show_result_dialog(self,result):
		form = ShowResultDialog(parent=self,predict_value=result)
		if form.exec_():
			print("Finished show result")		

	def showPatientInfoDialog(self):
		#http://stackoverflow.com/questions/5874025/pyqt4-how-to-show-a-modeless-dialog
		#If you don't pass the self argument,it will be recycled by garbage collector!
		form = PatientInfoDialog(parent=self)
		if form.exec_():
			self.diagonosis = form.getDiagnosisInfo()
			print(self.diagonosis)
			
	def show_select_diagonosis_dialog(self):
		form = SelectDiagonosisDialog(parent = self)
		if form.exec_():
			print("Select a diagonosis")