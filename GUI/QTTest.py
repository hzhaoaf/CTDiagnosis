import sys
from PyQt4 import QtGui,QtCore
from ui_testQt import Ui_MainWindow
#app = QtGui.QApplication(sys.argv)
#label = QtGui.QLabel("Hello QT!")
#quitButton = QtGui.QPushButton("Quit")
#QtCore.QObject.connect(quitButton,QtCore.SIGNAL("clicked()"),app,QtCore.SIGNAL("quit()"))
#quitButton.show()
#sys.exit(app.exec_())
import sys
from PyQt4 import QtGui,QtCore,QtWebKit
from PyQt4.QtWebKit import QWebPage
class Browser(QtGui.QMainWindow):
    def __init__(self,parent=None):
        QtGui.QWidget.__init__(self,parent)
        self.ui=Ui_MainWindow()
        self.ui.setupUi(self)

        
app=QtGui.QApplication(sys.argv)
myapp=Browser()
myapp.show()
sys.exit(app.exec_())