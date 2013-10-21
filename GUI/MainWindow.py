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
from gui_model_diagnosis import UI_Diagnosis

image_path = '../data/images/'

#class MainWindow(QtGui.QWidget):
class MainWindow(QtGui.QMainWindow):
	def __init__(self,parent = None):
		#QtGui.QWidget.__init__(self)
		super(MainWindow, self).__init__(parent)
		self.setGeometry(40,40,880,660)
		self.diagonosis = None
		self.imgNameSuffix = 1#starts from 001 to 999
		self.curImgNo = -1
		self.croppedImages = []
		#self.splCmd=QtGui.QSplitter(Qt.Vertical,self)
		#self.splTop=QtGui.QSplitter(Qt.Horizontal,self.splCmd)
		self.main=ImageView(self)
		#self.main=ImageView(self.splTop)
		self.setCentralWidget(self.main)
		#self.main.setAlignment(Qt.AlignHCenter)
		#self.splTop.addWidget(self.main)
		#self.splCmd=QtGui.QSplitter(Qt.Vertical,self)
		#self.main=ImageView(self.splCmd)
		#self.main.setAlignment(Qt.AlignHCenter)
		#self.splCmd.addWidget(self.main)
		self.createMenus()
		self.setMouseStyleCross()
		
		#This is wrong with SVM, comment it temp.. 
		#self.svmModel = SVM()	
	
	def setMouseStyleCross(self):
		self.main.setCursor(Qt.CrossCursor)
	def setMouseStyleNormal(self):
		self.main.setCursor(Qt.ArrowCursor)
	def createMenus(self):
		fileOpenAction = self.createAction(u"打开", self.load,
				QtGui.QKeySequence.Open, "fileopen",
				u"打开新的图像文件")
		cropImageAction = self.createAction(u"&裁剪...", self.crop,tip = u"裁剪图像")
		svmGuessAction = self.createAction(u"&Magic...", self.curveletExtract,tip = u"分析图像患病概率")
		shPaInfoDialAction = self.createAction(u"&输入患者信息...", \
		                                       self.showPatientInfoDialog,tip = u"输入患者信息")

		nextImageAction = self.createAction(u"&下一张...", 
		                                    self.nextImage,tip = u"下一张图像",
		                                    shortcut=QtGui.QKeySequence.MoveToNextChar)
		lastImageAction = self.createAction(u"&上一张...", 
		                                    self.lastImage,tip = u"上一张图像",
		                                    shortcut=QtGui.QKeySequence.MoveToPreviousChar)	
		
		self.fileMenu = self.menuBar().addMenu(u"文件")
		self.imgMenu = self.menuBar().addMenu(u"图像")
		self.funcMenu = self.menuBar().addMenu(u"功能")
		
		self.fileMenuActions = [fileOpenAction]
		self.imgMenuActions = [cropImageAction]
		self.funcMenuActions = [svmGuessAction,shPaInfoDialAction]
		
		self.addAction(fileOpenAction)
		self.addAction(cropImageAction)
		self.addAction(svmGuessAction)
		self.addAction(nextImageAction)
		self.addAction(lastImageAction)
		self.addAction(shPaInfoDialAction)
		
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
		#if icon is not None:
			#action.setIcon(QIcon(":/%s.png" % icon))
		if shortcut is not None:
			action.setShortcut(shortcut)
		if tip is not None:
			action.setToolTip(tip)
			action.setStatusTip(tip)
		if slot is not None:
			self.connect(action, QtCore.SIGNAL(signal), slot)
		if checkable:
			action.setCheckable(True)
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
		
	def reloadImageAfterCrop(self):
		'''After Crop,set the image to None'''
		del self.iamgePaths[self.curImgNo]	
		if not self.iamgePaths:
			if self.main.image: del self.main.image
			self.main.image = None
			return
		else:
			self.openFile(self.iamgePaths[0])#Show first image
			self.curImgNo = 0
		
	def load(self):
		'''Action 1'''
		'''Open image without given name'''
		self.iamgePaths = openFileDialog(self,QString("Open Image"),QString(),self.filters(),QString())#TEmp
		if not self.iamgePaths:return
		self.openFile(self.iamgePaths[0])#Show first image
		self.curImgNo = 0
		self.imgNamePrefix = "201309011030_001_"
		
	def lastImage(self):
		'''Show the last Image if there is'''
		if self.curImgNo == -1:return
		if self.curImgNo - 1 >= 0:
			self.openFile(self.iamgePaths[self.curImgNo-1])
			self.curImgNo += -1
		else:
			print('There is no more image, first one!')

	def nextImage(self):
		'''Show the next Image if there is'''
		if self.curImgNo == -1:return
		if self.curImgNo+1 <= len(self.iamgePaths) - 1:
			self.openFile(self.iamgePaths[self.curImgNo+1])
			self.curImgNo += 1
		else:
			print('There is no more image, last one!')
		
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
	
	#def getImageAndParams(self):#,param):
		#'''If all parameters are valid for given function, and image is loaded, return image.
		#Otherwise return NULL and print any error messages to console
		#param parameters to check'''
		##if not self.getParams(param): 
			##return None
		##Get image and return it
		#i=self.getImage()
		#return i		
	
	
	def save(self):
		'''Save image under given name
		Parameter specifies name of image.
		If name is given in parameter and not with dialog, no questions about overwriting will be asked.
		If no parameter is specified, dialog is invoked to ask for one'''
		i=self.getImage()
		if not i: return
		fileName="%s%s%03d.png" % (image_path,self.imgNamePrefix,self.imgNameSuffix)
		self.imgNameSuffix+=1
		
		self.main.saveImage(ps2qs(fileName))
		self.postOp(i,False)
		
		#Once saved, append the save img's path into the croppedImages list
		self.croppedImages.append(fileName)
		#self.curveletExtract(fileName)

	#def crop(self,param):
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
		
		self.save()#Save immediately after crop
		#Flip to next image, without this image,show the user cropped image.
		self.reloadImageAfterCrop()
		self.postOp(i)
		
		
		
	def cleanAfterPredict(self):
		'''To do:Clean the context'''
		#cropped Images
		#curImgNo
		#imgSavedNumber
		pass
	
	def curveletExtract(self):
		'''Extract the curvelet from given image name'''
		if not self.croppedImages:
			print("No images cropped(selected) yet")
			return
		
		vecList = []
		for name in self.croppedImages:
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
		print(self.svmModel .predict(vectorList))
	
	def showPatientInfoDialog(self):
		#http://stackoverflow.com/questions/5874025/pyqt4-how-to-show-a-modeless-dialog
		#If you don't pass the self argument,it will be recycled by garbage collector!
		form = PatientInfoDialog(parent=self)
		if form.exec_():
			self.diagonosis = form.getDiagnosisInfo()
			print(self.diagonosis)
			
		#form.exec_()#?
	
from AbsWindow import AbsWindow

class ImageWindow(AbsWindow):
	def __init__(self,parent = None,img_save_path= '../data/images/'):
		super(ImageWindow, self).__init__(parent,img_save_path)
		
if __name__ == '__main__':
	import sys
	#QSetting http://blog.sina.com.cn/s/blog_4b5039210100h3zb.html
	globalSettings = QtCore.QSettings("JiZhe","CTAnalysis")
	globalSettings.setValue("view/scale",QtCore.QVariant(True))
	globalSettings.setValue("view/center",QtCore.QVariant(True))
	app = QtGui.QApplication(sys.argv)
	#window = MainWindow()
	window = ImageWindow()
	window.show()
	#window.load()
	sys.exit(app.exec_())