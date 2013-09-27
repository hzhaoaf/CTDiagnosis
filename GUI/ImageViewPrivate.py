from PyQt4 import QtGui, QtCore
from PyQt4.QtCore import Qt

from ImageViewPrivate import ImageViewPrivate

class ImageViewPrivate(QtGui.QWidget):
	def __init__(self,_p):
		self.setPalette(QtGui.QPalette(QtGui.QColor(128,128,128)))
		self.setAttribute(Qt.WA_NoSystemBackground)
		self.setAttribute(Qt.WA_OpaquePaintEvent)
		self.p = _p
		self.rb = None
		self.moveRb = False
		self.setMouseTracking(True)