# -*- coding: utf-8 -*-
#!/usr/bin/env python

import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from gui_dal import GUIDAL
from PatientInfoDialog import PatientInfoReadOnlyDialog
from gui_model_diagnosis import UI_Diagnosis

MAC = "qt_mac_set_native_menubar" in dir()

class DiagnosisListDlg(QDialog):
    
    def show_patientinfo_readonly_dialog(self,diagnosis_to_show):
	    '''Create and show readonly diagnosis info Dialog window'''
	    form = PatientInfoReadOnlyDialog(diagnosis_to_show)
	    if form.exec_():
		    print("finish showing the read only diagnosis")    

    def parse_diagnosis_list(self,all_diagnosis):
	res = []
	for one_dia in all_diagnosis:
		whole_string = ''
		for item in one_dia:
			if isinstance(item,unicode):
				whole_string+=item + '\t' 
			else:
				whole_string+=str(item)+'\t'
		res.append(whole_string)
	
	return res 

    def __init__(self, name, diagnosis_list=None, parent=None):
        super(DiagnosisListDlg, self).__init__(parent)
        self.gui_dal = GUIDAL()
        self.name = name
	self._diagnosis_list = diagnosis_list
	stringlist = self.parse_diagnosis_list(diagnosis_list)
        self.listWidget = QListWidget()
        if diagnosis_list:
            self.listWidget.addItems(stringlist)
            self.listWidget.setCurrentRow(0)

        buttonLayout = QVBoxLayout()
        for text, slot in ((u"查看", self.show_dignosis_info_dialog),
                           (u"关闭", self.accept)):
            button = QPushButton(text)
            if not MAC:
                button.setFocusPolicy(Qt.NoFocus)
            if text == u"关闭":
                buttonLayout.addStretch()#button与其他button分离开
            buttonLayout.addWidget(button)
            self.connect(button, SIGNAL("clicked()"), slot)
        layout = QHBoxLayout()
        layout.addWidget(self.listWidget)
        layout.addLayout(buttonLayout)
        self.setLayout(layout)
        self.setWindowTitle( u"查看 %s 列表" % self.name)

    def show_dignosis_info_dialog(self):
        row = self.listWidget.currentRow()
        item = self.listWidget.item(row)
        if item:
            one_diagnosis_info = self.gui_dal.get_one_diagosis_info(self._diagnosis_list[row][0])
	    self.show_patientinfo_readonly_dialog(UI_Diagnosis(one_diagnosis_info))
	    

    def remove(self):
        '''
        Remove an item from listwidget
        '''
        row = self.listWidget.currentRow()
        item = self.listWidget.item(row)
        if item is None:
            return
        
        reply = QMessageBox.question(self, u"删除 %s" % self.name,
                        "删除 %s `%s'?" % (self.name, unicode(item.text())),QMessageBox.Yes|QMessageBox.No)
        
        if reply == QMessageBox.Yes:
            #takeItem() method Removes and returns the item from the given row in the list widget; otherwise returns 0.
            #Items removed from a list widget will not be managed by Qt, and will need to be deleted manually            
            item = self.listWidget.takeItem(row)
            del item
            #To Do : Remove this item from the database.

    def reject(self):
        self.accept()

    def accept(self):
        self.stringlist = QStringList()
        for row in range(self.listWidget.count()):
            self.stringlist.append(self.listWidget.item(row).text())
        self.emit(SIGNAL("acceptedList(QStringList)"), self.stringlist)
        QDialog.accept(self)

if __name__ == "__main__":
    fruit = [u"香蕉\t你个扒拉", "Apple", "Elderberry", "Clementine", "Fig",
             "Guava", "Mango", "Honeydew Melon", "Date", "Watermelon",
             "Tangerine", "Ugli Fruit", "Juniperberry", "Kiwi",
             "Lemon", "Nectarine", "Plum", "Raspberry", "Strawberry",
             "Orange"]
    app = QApplication(sys.argv)
    form = DiagnosisListDlg("Fruit", fruit)
    form.exec_()
    print "\n".join([unicode(x) for x in form.stringlist])