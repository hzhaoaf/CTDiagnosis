#http://stackoverflow.com/questions/13840289/how-to-use-qrubberband-with-qrect-class-in-pyqt
#http://srinikom.github.io/pyside-docs/PySide/QtGui/QRubberBand.html
#http://www.qtcentre.org/threads/28823-Crop-image

'''Use QLabel to show a image. Implement a QRubberBand over the label. 
Then get the rect of rubber band , translate to image cordinates and crop the image using QImage::scaled.
Then set the scaled image on the label.'''

import os
from PyQt4 import QtGui, QtCore

class Window(QtGui.QWidget):
    def __init__(self):
        QtGui.QWidget.__init__(self)
        self.bg = QtGui.QFrame(self)
        self.bg.setGeometry(10,10,800,600)
        self.pic = QtGui.QLabel(self.bg)
        #self.pic.setGeometry(10, 10,800,600)
        #use full ABSOLUTE path to the image, not relative
        self.image = QtGui.QImage()
        self.image.load(os.getcwd()+"/1.png")
        self.pic.setPixmap(QtGui.QPixmap.fromImage(self.image))

        #If you pass a parent to PySide.QtGui.QRubberBand ¡®s constructor, 
        #the rubber band will display only inside its parent, but stays on top of other child widgets. 
        #If no parent is passed, PySide.QtGui.QRubberBand will act as a top-level widget.  
        #self.rubberband = QtGui.QRubberBand(QtGui.QRubberBand.Rectangle,)
        self.rubberband = QtGui.QRubberBand(QtGui.QRubberBand.Rectangle, self.pic)
        self.setMouseTracking(True)

    def mousePressEvent(self, event):
        self.origin = event.pos()
        self.rubberband.setGeometry(QtCore.QRect(self.origin, QtCore.QSize()) )
        self.rubberband.show()
        #QtGui.QWidget.mousePressEvent(self, event)

    def mouseMoveEvent(self, event):
        if self.rubberband.isVisible():
            #Control the Rubber within the imageViewer!!!
            self.rubberband.setGeometry(QtCore.QRect(self.origin, event.pos()).normalized() & self.image.rect())
        #QtGui.QWidget.mouseMoveEvent(self, event)
    
    def cropImage(self,rect):
        self.image = self.image.copy(rect)
        self.pic.setPixmap(QtGui.QPixmap.fromImage(self.image))
        self.image.save(os.getcwd()+'/cropped.png')
        self.update()
        
    def mouseReleaseEvent(self, event):
        if self.rubberband.isVisible():
            self.rubberband.hide()
            selected = []
            rect = self.rubberband.geometry()
            print(rect)
            self.cropImage(rect)
            '''
            for child in self.findChildren(QtGui.QPushButton):
                if rect.intersects(child.geometry()):
                    selected.append(child)
            print 'Selection Contains:\n ',
            if selected:
                print '  '.join(
                    'Button: %s\n' % child.text() for child in selected)
            else:
                print ' Nothing\n'
            '''
        #QtGui.QWidget.mouseReleaseEvent(self, event)

if __name__ == '__main__':

    import sys
    app = QtGui.QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())