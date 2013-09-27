from PyQt4 import QtGui, QtCore
from PyQt4.QtCore import Qt
from PyQt4.QtCore import QRect
from ImageView import ImageView
from append import *

class MainWindow(QtGui.QWidget):
	def __init__(self):
		QtGui.QWidget.__init__(self)
		self.splCmd=QtGui.QSplitter(Qt.Vertical,self)
		self.splTop=QtGui.QSplitter(Qt.Horizontal,self.splCmd)
		self.main=ImageView(self.splTop)
		
	def openFile(self,name):
		'''Open image with given name'''
		self.main.loadImage(name)
		#self.setTitle()
		self.postOp(self.getImage(),False)
		
	def postOp(self,i,doUpdate):
		'''Function to call after performing an operation.Redraw the image and handle any errors'''
		'''i Image that was processed'''
		'''doUpdate If true, update image on screen.
				 In some operations it may be unnecessary to update, like if the image was not modified,
				 or if the update is done in other way. Default is to update'''
		self.main.cancelRect()#Will ensure that updateMenus() will be called in the process
		if  doUpdatem:self.main.update()
		
	def load(self,param):
		'''Open image with given name Parameter specifies name of image 
		If no parameter is specified, dialog is invoked to ask for one'''
		if param.count() < 1:
			#No parameters
			fileName = openFileDialog(self,"Open Image","loadimage",filters(),"loadimagepath")
		else:
			fileName=param[0]
		if (fileName.isNull()):return
		openFile(fileName)
		
	
	def filters(self,useGeneric,useBareFormat):
		'''Return suggested filters to use in a save/load dialog'''
		out = QtCore.QStringList()
		out << "BMP (*.bmp)"
		out << "Dicom (*.dcm *.dicom)"
		out << "JPEG (*.jpg *.jpeg)"
		out << "PNG (*.png)"
		return out
	
if __name__ == '__main__':
    
	import sys
	#QSetting http://blog.sina.com.cn/s/blog_4b5039210100h3zb.html
	globalSettings = QtCore.QSettings("JiZhe","CTAnalysis")
	
	app = QtGui.QApplication(sys.argv)
	window = MainWindow()
	window.show()
	sys.exit(app.exec_())