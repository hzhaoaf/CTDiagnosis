# -*- coding: utf-8 -*-
from PyQt4 import QtGui, QtCore
from PyQt4.QtCore import Qt,QString,QRect
from ImageViewPrivate import ImageViewPrivate
from Image import Image
from math import floor

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
     
    def selectionFromImageCoords(self,selectionRect):
        '''Return selection rectangle converted from image coordinate system to window coordinate syste'''
        x= (selectionRect.left())*self.data_rect.width()/self.image.x()+self.data_rect.left()
        y= (selectionRect.top())*self.data_rect.height()/self.image.y()+self.data_rect.top()
        xr=(selectionRect.right()+1)*self.data_rect.width()/self.image.x()+self.data_rect.left()-1
        yr=(selectionRect.bottom()+1)*self.data_rect.height()/self.image.y()+self.data_rect.top()-1
        return QRect(x,y,xr,yr)
    
    def selectionToImageCoords(self,selectionRect):
        '''Return selection rectangle converted to image coordinate system@param selectionRect rectangle to convert'''
        dw=self.data_rect.width()
        dh=self.data_rect.height()
        x=int(floor((selectionRect.left()-self.data_rect.left())* self.image.x()/dw))
        y=int(floor((selectionRect.top()-self.data_rect.top())* self.image.y()/dh))
        xr=int(floor((selectionRect.right()-self.data_rect.left()) * self.image.x()/dw))
        yr=int(floor((selectionRect.bottom()-self.data_rect.top())*self.image.y()/dh))
        #print(QRect(x,y,xr,yr))
        return QRect(x,y,xr,yr)

    def setDataRect(self):
        '''Update data_rect'''
        #Get image dimensions
        dx=self.image.x()
        dy=self.image.y()        
        #Get image screen dimensions (may differ if zoom is set)
        screen_dx=dx*self.zoom/100.0
        screen_dy=dy*self.zoom/100.0
        x=self.d.width()
        y=self.d.height()
        wx=x
        wy=dy*wx/dx
        if wy > y:
            wy=y
            wx=dx*wy/dy
        if self.isSet("center"):#居中画图而不拉伸
            self.data_rect=QRect(max((x-screen_dx)/2,0),max((y-screen_dy)/2,0),screen_dx,screen_dy)
        else:
            self.data_rect=QRect(max((x-wx)/2,0),max((y-wy)/2,0),wx,wy)
            
    def getSelection(self):
        '''return the selection rectangle from (x0,y0,x1,y1) to (x,y,width,height)'''
        width = self.selection.width() - self.selection.left()
        height = self.selection.height() - self.selection.top()
        return QRect(self.selection.left(),self.selection.top(),width,height)
    
    def repaint(self,x,y,p,src):
        '''Repaint the image using given painter and size of output window
        @param x width of output window
        @param y height of output window
        @param p QPainter to use
        @param src Which part of image to repaint (when not in fullscreen)'''
        '''TypeError: QPainter.setRenderHint(QPainter.RenderHint, bool on=True): first argument of unbound method must have type 'QPainter'''
        #p.setRenderHint(QtGui.QPainter.SmoothPixmapTransform,True)
        p.setRenderHint(QtGui.QPainter.Antialiasing,True)
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
        self.setDataRect()
        #Repaint stripes around image if needed
        if self.data_rect.left() > src.left():
            #repaint stripe on left
            tmp = QRect(0,0,self.data_rect.left(),y)
            p.fillRect(tmp & src,black)
        if self.data_rect.right()<src.right():
            #repaint on right
            tmp = QRect(self.data_rect.right(),0,x-self.data_rect.right(),y)
            p.fillRect(tmp & src,black)
        if self.data_rect.top()>src.top():
            #repaint on top
            tmp = QRect(self.data_rect.left(),0,self.data_rect.width(),self.data_rect.top())
            p.fillRect(tmp & src,black)
        if self.data_rect.bottom()<src.bottom():
            #repaint on bottom
            tmp = QRect(self.data_rect.left(),self.data_rect.bottom(),self.data_rect.width(),y-self.data_rect.bottom())
            p.fillRect(tmp & src,black)
        #Show scaled to window
        #Set target to data rectangle
        target=self.data_rect
        #Draw entire image scaled
        source = QRect(0,0,self.image.x(),self.image.y())
        self.image.draw(p,source,target)#Stop Here
          
    def getImage(self):
        ''' Return image shown in the widget (or NULL if nothing is shown)
        If the image is modified, update() should be called to redraw the new image'''
        return self.image
    
    def moveRubberBand(self,newGeom):
        '''Move the rubberband after updating the zoom level'''
        if not rb: return
        self.rb.setGeometry(newGeom)  
        
    def rectCheck(self):
        ''' Called when selection is finished (on releasing the mouse button) and on start'''
        if self.selection.isValid():
             #"Snap rect to grid"
            self.setDataRect()
            self.d.moveRubberBand(self.selectionFromImageCoords(self.selection))
   

    def cancelRect(self):
        self.d.cancelRect()
        self.rectCheck()
    
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
        '''sizeHint() 方法给出一个推荐的大小。这里我们重写这个方法'''
        '''Return size hint for the widget'''
        if self.image:
            #Size of image
            return QtCore.QSize(self.image.x(),self.image.y())
        else:
            #Some default,very Important
            return QtCore.QSize(840,630)

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
    
    def selRect(self,r):
        '''Update selection rectangle position'''
        if r.width()<=0 or r.height()<=0:
            self.selection=QRect()
        else:
            self.selection = self.selectionToImageCoords(r)
            print(self.selection)
            x1=self.selection.left()
            x2=self.selection.right()
            y1=self.selection.top()
            y2=self.selection.bottom()
            w=self.selection.width()
            h=self.selection.height()
            #selText
            print(QString.number(x1)+","+QString.number(y1)+" - "+QString.number(x2)+","+QString.number(y2)
                     +" ("+QString.number(w)+"x"+QString.number(h)+") ")
    
    def rectCheck(self):
        pass

