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

image_path = '../data/images/'

#class MainWindow(QtGui.QWidget):
class MainWindow(QtGui.QMainWindow):
	def __init__(self,parent = None):
		#QtGui.QWidget.__init__(self)
		super(MainWindow, self).__init__(parent)
		self.setGeometry(40,40,880,660)
		
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
	
	def createMenus(self):
		fileOpenAction = self.createAction(ps2qs("&打开..."), self.load,
				QtGui.QKeySequence.Open, "fileopen",
				ps2qs("打开新的图像文件"))
		cropImageAction = self.createAction(ps2qs("&裁剪..."), self.crop,tip = ps2qs("裁剪图像"))
		svmGuessAction = self.createAction(ps2qs("&Magic..."), self.save,tip = ps2qs("分析图像患病概率"))	
		
		self.fileMenu = self.menuBar().addMenu(ps2qs("文件"))
		self.imgMenu = self.menuBar().addMenu(ps2qs("图像"))
		self.funcMenu = self.menuBar().addMenu(ps2qs("功能"))
		
		self.fileMenuActions = [fileOpenAction]
		self.imgMenuActions = [cropImageAction]
		self.funcMenuActions = [svmGuessAction]
		
		self.addAction(fileOpenAction)
		self.addAction(cropImageAction)
		self.addAction(svmGuessAction)
		
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
		
	def load(self):
		'''Action 1'''
		'''Open image without given name'''
		fileName = openFileDialog(self,QString("Open Image"),QString(),self.filters(),QString())#TEmp
		if fileName.isNull():return
		self.openFile(fileName)	
		
	
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
	def getImageAndParams(self):#,param):
		'''If all parameters are valid for given function, and image is loaded, return image.
		Otherwise return NULL and print any error messages to console
		param parameters to check'''
		#if not self.getParams(param): 
			#return None
		#Get image and return it
		i=self.getImage()
		return i		
	
	
	def save(self):
		'''Save image under given name
		Parameter specifies name of image.
		If name is given in parameter and not with dialog, no questions about overwriting will be asked.
		If no parameter is specified, dialog is invoked to ask for one'''
		i=self.getImage()
		if not i: return
		fileName=image_path+"123.png"
		self.main.saveImage(ps2qs(fileName))
		self.postOp(i,False)
		self.curveletExtract(fileName)

	#def crop(self,param):
	def crop(self):
		#A rectangle is normally expressed as an upper-left corner and a size
		'''Action 2'''
		'''Crop image _QStringList param  Command parameters'''
		i=self.getImageAndParams()#param)
		if not i: return
		rectan = self.main.getSelection()
		if not rectan:
			return
		
		#print(QRect(rectan.left(), rectan.top(), rectan.width(), rectan.height()))
		i.crop(rectan.left(), rectan.top(), rectan.width(), rectan.height())
		self.postOp(i)
		
	def curveletExtract(self,name):
		'''Extract the curvelet from given image name'''
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
		print(vec)
		self.svmPredict(vec)
		#print(len(vec))
		
		
	def svmPredict(self,vector):
		'''Predict the probability of a feature'''
		svmModel = SVM()
		print(svmModel.predict([vector]))
	

if __name__ == '__main__':
	import sys
	#QSetting http://blog.sina.com.cn/s/blog_4b5039210100h3zb.html
	globalSettings = QtCore.QSettings("JiZhe","CTAnalysis")
	globalSettings.setValue("view/scale",QtCore.QVariant(True))
	globalSettings.setValue("view/center",QtCore.QVariant(True))
	app = QtGui.QApplication(sys.argv)
	window = MainWindow()
	window.show()
	window.load()
	sys.exit(app.exec_())