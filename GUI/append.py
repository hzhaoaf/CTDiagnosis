# -*- coding: utf-8 -*-

from PyQt4 import QtGui, QtCore
from PyQt4.QtCore import Qt
from PyQt4.QtCore import QRect

def ps2qs(zhongwen):
	return QtCore.QString(unicode(zhongwen, 'gb2312', 'ignore'))

def qs2ps(zhongwen):
	'''PyQt的QString和python的string的区别
	http://www.cnblogs.com/babykick/archive/2011/05/16/2048155.html'''
	return unicode(zhongwen,'gbk','ignore').encode('gb2312')

def dcm2Png(filePath):
	'''Input:  .dcm file path
	Output: .png file path'''
	import sys,os
	sys.path.append("..")
	from dcm.testDCM import *
	#os.path.splitext():分离文件名与扩展名,os.path.basename(path):返回文件名 
	#picName = os.path.splitext(os.path.basename(filePath))[0]
	filePath = qs2ps(filePath)
	plan=dicom.read_file(filePath)
	im = dcm2pil(plan)
	savedFilePath = os.path.splitext(filePath)[0] + ".png"
	im.save(savedFilePath)
	return ps2qs(savedFilePath)

def getDir(fd):
	'''Get current directory from File Dialog'''
	d=fd.directory();
	return d.absolutePath()

def openFileDialog(parent,caption,settingName,filters,savePath):
	global globalSettings
	fd = QtGui.QFileDialog(parent)
	#if filters.size():#AttributeError: 'QStringList' object has no attribute 'size'
	if filters.count():
		#Set filters if filters specified
		fd.setFilters(filters)
	if  not caption.isNull():
		fd.setWindowTitle(caption)
	if savePath.isNull():
	        #No save path specified -> start in current directory
		fd.setDirectory(".")
        else:
		#Try to set last used saved path, if it exists
		globalSettings = QtCore.QSettings("JiZhe","CTAnalysis")
		fd.setDirectory(globalSettings.value("history/path/"+savePath,"."))
	fd.setFileMode(QtGui.QFileDialog.ExistingFile)
	while True:
		if  not settingName.isNull():
			#// Restore window position from settings if applicable
			globalSettings = QtCore.QSettings("JiZhe","CTAnalysis")
			globalSettings.restoreWindow(fd,settingName)
		if fd.exec_()==QtGui.QDialog.Accepted:
			if  not settingName.isNull():
				#Save window position to settings if applicable
				globalSettings.saveWindow(fd,settingName)
			if not savePath.isNull():
				#Save the path if desired
				if globalSettings.read("history/save_filePath"):
					#//Note that there is only one central setting "save paths in dialog" for all dialog types
					globalSettings.write("history/path/"+savePath,getDir(fd));
			files = fd.selectedFiles()
			if  not files.isEmpty(): 
				name = files[0]
				if name.endsWith("DCM"):
					name = dcm2Png(name)
					
			if  QtCore.QFileInfo(name).isDir():#directory was selected
				#** \todo  test this ! */ 
				fd.setDirectory(name)
				continue#restart dialog
			return name
		return QtCore.QString()