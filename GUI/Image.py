from PyQt4 import QtGui, QtCore
from PyQt4.QtCore import Qt
from PyQt4.QtCore import QRect
from ImagePrivate import ImagePrivate
class Image:
	def __init__(self,data):
		'''constructor of Image'''
		if isinstance(data,QtCore.QString):#Init by name
			self.d = ImagePrivate()
			self.loadImage(data)
	def loadImage(self,name):
		'''Replace image contents with new one'''
		self.d.i.loadFromData(name.toLocal8Bit().data())
		self.d.setName(name)
		#self.clearUndo()
				