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

    def __init__(self, leftFlow=0, rightFlow=0, maxFlow=100,parent=None):
        super(ImageControlWidget, self).__init__(parent)
        self._parent = parent
        self.setObjectName(_fromUtf8("ImageControlWidget"))        
        self.prev_button = QPushButton(self)
        self.prev_button.setText(_translate("ImageControlWidget", "上一张", None))
        self.prev_button.setMinimumHeight(60)
        self.prev_button.clicked.connect(parent.previousImage)
         
        self.next_button = QPushButton(self)
        self.next_button.setText(_translate("ImageControlWidget", "下一张", None))
        self.next_button.setMinimumHeight(60)
        self.next_button.clicked.connect(parent.nextImage)
        
        self.is_in_use_checkbox = QCheckBox(self)
        self.is_in_use_checkbox.setText(_translate("ImageControlWidget", "预测该图像", None))
        self.is_in_use_checkbox.stateChanged.connect(self._check_box_state_changed)
        
        # 创建QSlider，我们要的是横向的，  
        # 使用QtCore.Qt.Horizontal来定义          
        # 创建spinBox  
        _label = QLabel(u"设置区域生长算法阈值:")
        self.threshold_slider = QSlider(Qt.Horizontal,self)
        self.threshold_slider.setMaximumWidth(100)
        self.threshold_spinBox = QSpinBox(self)  
        self.threshold_slider.setRange( 0, 100 )  # 设置数值范围  
        self.threshold_slider.setRange( 0, 100 )   # 设置数值范围
        # 创建连接  
        self.threshold_spinBox.valueChanged.connect( self.threshold_slider.setValue )  
        self.threshold_slider.valueChanged.connect(  self.threshold_spinBox.setValue )  
          
        # 设置一个数值  
        self.threshold_spinBox.setValue(60)         
        
        self.crop_button = QPushButton(self)
        self.crop_button.setText(_translate("ImageControlWidget", "裁剪", None))
        self.crop_button.setMinimumHeight(60)
        self.crop_button.clicked.connect(parent.crop)
        
        #第一行，三个组件
        self.hlayout_up = QHBoxLayout()
        self.hlayout_up.addWidget(self.prev_button)
        self.hlayout_up.addWidget(self.crop_button)
        self.hlayout_up.addWidget(self.next_button)
        
        #第二行，四个组件
        self.hlayout_down = QHBoxLayout()
        #self.hlayout_down.addStretch()
        self.hlayout_down.addWidget(_label)
        self.hlayout_down.addWidget(self.threshold_slider)
        self.hlayout_down.addWidget(self.threshold_spinBox)
        self.hlayout_down.addStretch()
        self.hlayout_down.addWidget(self.is_in_use_checkbox)
        ayout = QVBoxLayout()
        
        #上下两个组件合并成一个数列组件
        self.vlayout = QVBoxLayout(self)
        self.vlayout.addLayout(self.hlayout_down)
        self.vlayout.addLayout(self.hlayout_up)
        

        
        #self.label = QLabel(self)
        #self.label.setFrameStyle(QFrame.StyledPanel|QFrame.Sunken)
        #self.label.setAlignment(Qt.AlignCenter)
        #fm = QFontMetricsF(self.font())
        #self.label.setMinimumWidth(fm.width(" 999 l/s "))

        #self.setSizePolicy(QSizePolicy(QSizePolicy.Expanding,
                                       #QSizePolicy.Expanding))
        #self.setMinimumSize(self.minimumSizeHint())
        #self.valueChanged()
        
    def get_threshold_value(self):
        return self.threshold_slider.value()
    
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
