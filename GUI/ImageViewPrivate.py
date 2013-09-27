from PyQt4 import QtGui, QtCore
from PyQt4.QtCore import Qt
from PyQt4.QtCore import QRect


class ImageViewPrivate(QtGui.QWidget):
	def __init__(self,_p):
		QtGui.QWidget.__init__(self)
		self.setPalette(QtGui.QPalette(QtGui.QColor(128,128,128)))
		#self.setAttribute(Qt.WA_NoSystemBackground)
		#self.setAttribute(Qt.WA_OpaquePaintEvent)#Some weired effect?
		self.p = _p
		self.rb = None
		self.moveRb = False
		self.setMouseTracking(True)
	
	def sizeHint(self):
		'''Return size hint from parent item'''
		return self.p.sizeHint()
	
	def mouseMoveEvent(self,e):
		print(e.pos())
		if self.rb and (e.buttons() & Qt.LeftButton):
			r = QRect(self.origin,e.pos()).normalized()
			self.rb.setGeometry(r )#& self.p.data_rect)#use & to control the rb within the window
			self.p.selRect(self.rb.geometry())
		self.p.mouseCoordEvent(e)
		e.ignore()
	
	def mousePressEvent(self,e):
		if e.button() == Qt.LeftButton:
			self.moveRb = True
			self.origin = e.pos()
			if not self.rb: 
				self.rb = QtGui.QRubberBand(QtGui.QRubberBand.Rectangle, self)
			self.rb.setGeometry(QtCore.QRect(self.origin, QtCore.QSize()))
			self.rb.show()
			e.accept()
		else:
			e.ignore()
			
	def mouseReleaseEvent(self,e):
		if e.buttons() & Qt.LeftButton:#Left button is still pressed
			e.ignore() 
			return
		if self.moveRb:
			self.moveRb = False
			self.p.selRect(self.rb.geometry())
			self.p.rectCheck()
		else:
			e.ignore()