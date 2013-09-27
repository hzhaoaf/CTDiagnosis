from PyQt4 import QtGui, QtCore
from ImageViewPrivate import ImageViewPrivate

class ImageView(QtGui.QScrollArea):
    #constructor of ImageView
    def __init__(self):
        self.image = None
        self.zoom = 100
        #if (!ic) ic=new IconCache();
        self.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.setSizePolicy(QtGui.QSizePolicy.Expanding,QtGui.QSizePolicy.Expanding)
        self.d =ImageViewPrivate(self)
        self.setWidget(self.d)
        self.setWidgetResizable(True)
        self.setBackgroundRole(QtGui.QPalette.Dark)
        self.setMouseTracking(True)
        self.mouse_x = -1
        self.mouse_y = -1
        self.mouse_ex = 0
        self.mouse_ey = 0
        self.data_rect = QtCore.QRect(0,0,1,1)
        #self.setMode(view)