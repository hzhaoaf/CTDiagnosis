# -*- coding: utf-8 -*-
#!/usr/bin/env python

from __future__ import division
from PyQt4.QtCore import *
from PyQt4.QtGui import *

try:
    _fromUtf8 = QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s
    
try:
    _encoding = QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QApplication.translate(context, text, disambig)

class ImageControlWidget(QWidget):

    def __init__(self, leftFlow=0, rightFlow=0, maxFlow=100,
                 parent=None):
        super(ImageControlWidget, self).__init__(parent)
        self._parent = parent
        self.setObjectName(_fromUtf8("ImageControlWidget"))        
        self.prev_button = QPushButton(self)
        self.prev_button.setText(_translate("ImageControlWidget", "上一张", None))
        self.prev_button.setMinimumHeight(80)
        self.prev_button.clicked.connect(parent.previousImage)
         
        self.next_button = QPushButton(self)
        self.next_button.setText(_translate("ImageControlWidget", "下一张", None))
        self.next_button.setMinimumHeight(80)
        self.next_button.clicked.connect(parent.nextImage)
        
        self.is_in_use_checkbox = QCheckBox(self)
        self.is_in_use_checkbox.setText(_translate("ImageControlWidget", "计算该图像", None))
        self.is_in_use_checkbox.stateChanged.connect(self._check_box_state_changed)
        
        self.crop_button = QPushButton(self)
        self.crop_button.setText(_translate("ImageControlWidget", "裁剪", None))
        self.crop_button.setMinimumHeight(60)
        self.crop_button.clicked.connect(parent.crop)
        
        self.vlayout = QVBoxLayout()
        self.vlayout.addWidget(self.crop_button)
        self.vlayout.addWidget(self.is_in_use_checkbox)
        
        self.hlayout = QHBoxLayout(self)
        self.hlayout.addWidget(self.prev_button)
        self.hlayout.addLayout(self.vlayout)
        self.hlayout.addWidget(self.next_button)
        #self.label = QLabel(self)
        #self.label.setFrameStyle(QFrame.StyledPanel|QFrame.Sunken)
        #self.label.setAlignment(Qt.AlignCenter)
        #fm = QFontMetricsF(self.font())
        #self.label.setMinimumWidth(fm.width(" 999 l/s "))

        #self.setSizePolicy(QSizePolicy(QSizePolicy.Expanding,
                                       #QSizePolicy.Expanding))
        #self.setMinimumSize(self.minimumSizeHint())
        #self.valueChanged()
        
    def _check_box_state_changed(self):
        able = self.is_in_use_checkbox.isChecked()
        self._parent.change_image_in_use_state(able)

    def set_in_use_checked(self,able):
        self.is_in_use_checkbox.setChecked(able)
        
    def valueChanged(self):
        a = self.leftSpinBox.value()
        b = self.rightSpinBox.value()
        self.label.setText("%d l/s" % (a + b))
        self.emit(SIGNAL("valueChanged"), a, b)
        self.update()


    def values(self):
        return self.leftSpinBox.value(), self.rightSpinBox.value()


    #def minimumSizeHint(self):
        #return QSize(self.leftSpinBox.width() * 3,self.leftSpinBox.height() * 5)

    #def resizeEvent(self, event=None):
        #fm = QFontMetricsF(self.font())
        #x = (self.width() - self.label.width()) / 2
        #y = self.height() - (fm.height() * 1.5)
        #self.label.move(x, y)
        #y = self.height() / 60.0
        #x = (self.width() / 4.0) - self.leftSpinBox.width()
        #self.leftSpinBox.move(x, y)
        #x = self.width() - (self.width() / 4.0)
        #self.rightSpinBox.move(x, y)
