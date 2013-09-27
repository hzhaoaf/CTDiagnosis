from PyQt4 import QtGui, QtCore
from PyQt4.QtCore import Qt,QString,QRect
from ImageViewPrivate import ImageViewPrivate
from Image import Image


class ImageView(QtGui.QScrollArea):
    def __init__(self,parent):
        '''constructor of ImageView'''
        QtGui.QWidget.__init__(self)
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
     
    def repaint(self,x,y,p,src):
        '''Repaint the image using given painter and size of output window
        @param x width of output window
        @param y height of output window
        @param p QPainter to use
        @param src Which part of image to repaint (when not in fullscreen)'''
        p = QtGui.QPainter#temp
        print("repaint in ImageView")
        p.setRenderHint(QtGui.QPainter.SmoothPixmapTransform,True)
        p.setPen = Qt.blue
        black = QtGui.QColor(0,0,0)
        if not self.image:
            #No image is loaded
            p.drawRect(0,0,x-1,y-1)
            p.fillRect(1,1,x-2,y-2,black)
            p.drawText(0,0,x,y,Qt.AlignVCenter | Qt.AlignCenter,QString("No image loaded"))
            return

        if self.image.x<=0 and self.image.y()<=0:
            #Invalid image is loaded
            p.drawRect(0,0,x-1,y-1)
            p.fillRect(1,1,x-2,y-2,black)
            p.drawText(0,0,x,y,Qt.AlignVCenter | Qt.AlignCenter,QString("Invalid image"))
            return
        #Rectangle specifying entire window
        rect = QRect(0,0,x,y)
        #Determine target rectangle at screen
        #Update data rectangle for mouse navigation
        
    def getImage(self):
        ''' Return image shown in the widget (or NULL if nothing is shown)
        If the image is modified, update() should be called to redraw the new image'''
        return self.image
    
    def cancelRect(self):
        pass
    
    def flushImage(self):
        '''Use after new image is loaded to flush/redraw various data'''
        self.update()
        self.cancelRect()
        #emit zoomChanged(zoom);
        #emit info("");


    def loadImage(self,name):
        '''Open image with given name in viewer'''    
        if self.image: del self.image
        self.image = Image(name)
        self.flushImage()
        
    def sizeHint(self):
        '''Return size hint for the widget'''
        if self.image:
            #Size of image
            return QtCore.QSize(self.image.x(),self.image.y())
        else:
            #Some default
            return QtCore.QSize(600,400)

    #Load state of specified optional feature from settings (default value is false)
    def isSet(self,name):
        globalSettings = QtCore.QSettings("JiZhe","CTAnalysis")
        return globalSettings.value("view/"+name).toBool()
    
    #Return minimum size neede to display the widget
    def minSize(self):
        if self.image :
        #if self.image and self.isSet("scale"):
            #Size of image
            x = self.image.x()
            y = self.image.y()
            x = x * self.zoom / 100.0
            y = y * self.zoom / 100.0
            return QtCore.QSize(x,y)
        else:
            #No minimum
            return QtCore.QSize(0,0)
        

    #Change internal widget's minimum size.Schedule this and internal widget to repaint.
    def update(self):
        self.d.setMinimumSize(self.minSize())
        self.d.update()
        #QtGui.QScrollArea.update()?

    def mouseCoordEvent(self,e):
        pass
    
    #Update selection rectangle position
    def selRect(self,r):
        pass
    
    def rectCheck(self):
        pass

