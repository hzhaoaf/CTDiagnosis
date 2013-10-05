# -*- coding: utf-8 -*-

from PyQt4 import QtGui, QtCore
from PyQt4.QtCore import Qt
from PyQt4.QtCore import QRect
from ImagePrivate import ImagePrivate
import math

def frac(x):
	''' Return fractional part of number'''
	return x - math.floor(x)

class Image:
	def __init__(self,data):
		'''constructor of Image'''
		if isinstance(data,QtCore.QString):#Init by name
			self.d = ImagePrivate()
			self.loadImage(data)
			
	def crop(self,x1,y1,width,height):
		'''
		 Crop image, replace image by its sub-region
		 @param x1 X-coordinate of the upper-left crop rectangle corner.
		 @param y1 Y-coordinate of the upper-left crop rectangle corner.
		 @param x2 X-coordinate of the lower-right crop rectangle corner.
		 @param y2 Y-coordinate of the lower-right crop rectangle corner.
		 #@param border_condition type of border condition if some of the desired region is outside the image.
		'''
		self.d.i = self.d.i.copy(x1,y1,width,height)#QImage.copy (self, int x, int y, int w, int h)
		self.d.imageChanged()
	
	#def beforeOp():
		#if (useUndo()):
		        #d->iUndo=d->i
		        #d->undoValid=True

	def loadImage(self,name):
		'''Replace image contents with new one'''
		#self.d.i.loadFromData(name.toLocal8Bit().data())
		self.d.i.load(name)
		self.d.setName(name)
		#self.clearUndo()
	def x(self):
		''' Return width of the image'''
		return self.d.i.size().width()
	def y(self):
		''' Return height of the image'''
		return self.d.i.size().height()	
	
	
	def draw(self,p,source,target,subsource = None):
		#这里很难写，回头还要看看写的对不对
		'''Draw image using QPainter
		@param p painter used to draw image
		@param source source rectangle - which part of image to draw
		@param target destination rectangle - which area to draw to
		@param subsource subpixel-accurate subset of source'''	
		wx=source.width()
		wy=source.height()
		x0=source.left()
		y0=source.top()
		source0 = QRect(0,0,wx,wy)
		theBytes=wx*wy*4 #RGBA
		if  self.d.pix_w !=wx or self.d.pix_h !=wy:
			#Size was changed since last time
			del self.d.pixdata
			self.d.pixdata=None
		if not self.d.pixdata:
		        #self.d.pixdata=(int *)malloc(theBytes)
		        self.d.pix_x=x0
		        self.d.pix_y=y0
		        self.d.pix_w=wx
		        self.d.pix_h=wy

		if subsource == None:
			p.drawImage(target,self.d.i,source0)
		else:
			subsource0 = QtCore.QRectF(frac(subsource.left()),frac(subsource.top()),subsource.width(),subsource.height())
			p.drawImage(target,self.d.i,subsource0)