from PyQt4 import QtGui, QtCore
from PyQt4.QtCore import Qt
from PyQt4.QtCore import QRect,QSize

class ImagePrivate:
	def __init__(self):
		'''constructor'''
		self.undoValid = False
		self.pixdata = None
		self.pix_x,self.pix_y,self.pix_w,self.pix_h = 0,0,0,0
		self.i = QtGui.QImage()
		
	def imageChanged(self):
		'''function to call when image is changed - flush some internal variables'''
		if self.pixdata:
			del self.pixdata
			self.pixdata = None
			
	def setName(self,name):
		'''Set name of image'''
		self.imgName = name
		if name.isNull():
			self.imgFullName = QtCore.QString.None
		else:
			self.imgFullName = QtCore.QFileInfo(name).absoluteFilePath()
			

		