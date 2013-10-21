#!/usr/bin/env python
# Copyright (c) 2007-8 Qtrac Ltd. All rights reserved.
# This program or module is free software: you can redistribute it and/or
# modify it under the terms of the GNU General Public License as published
# by the Free Software Foundation, either version 2 of the License, or
# version 3 of the License, or (at your option) any later version. It is
# provided for educational purposes and is distributed in the hope that
# it will be useful, but WITHOUT ANY WARRANTY; without even the implied
# warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See
# the GNU General Public License for more details.

from __future__ import division
from PyQt4.QtCore import *
from PyQt4.QtGui import *


class ImageControlWidget(QWidget):

    def __init__(self, leftFlow=0, rightFlow=0, maxFlow=100,
                 parent=None):
        super(ImageControlWidget, self).__init__(parent)
        self.pushButton = QPushButton(self)
        self.pushButton.setGeometry(QRect(110, 40, 75, 23))
        self.pushButton_2 = QPushButton(self)
        self.pushButton_2.setGeometry(QRect(550, 40, 75, 23))
        
        #self.label = QLabel(self)
        #self.label.setFrameStyle(QFrame.StyledPanel|QFrame.Sunken)
        #self.label.setAlignment(Qt.AlignCenter)
        #fm = QFontMetricsF(self.font())
        #self.label.setMinimumWidth(fm.width(" 999 l/s "))

        #self.setSizePolicy(QSizePolicy(QSizePolicy.Expanding,
                                       #QSizePolicy.Expanding))
        #self.setMinimumSize(self.minimumSizeHint())
        #self.valueChanged()


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




if __name__ == "__main__":
    import sys

    def valueChanged(a, b):
        print a, b

    app = QApplication(sys.argv)
    form = ImageControlWidget()
    form.connect(form, SIGNAL("valueChanged"), valueChanged)
    form.setWindowTitle("YPipe")
    form.move(0, 0)
    form.show()
    form.resize(400, 400)
    app.exec_()

