# -*- coding: utf-8 -*- 

import os
import ccf
import sys
sys.path.append("..")
from scipy import misc
import numpy as np

imageDir = u"C:\\Users\\Charles\\Desktop\\dcmProgram\\病例\\恶性"
save_path = u"C:\\Users\\Charles\\Desktop\\result\\恶性"

#os.chdir(imageDir)
info_dic = {}

patients_name_list = os.listdir(imageDir)
for patients_name in patients_name_list:
	patient_dir = os.path.join(imageDir, patients_name)
	if os.path.isdir(patient_dir):
		patient_dir = os.path.join(patient_dir,u"轴")
		os.chdir(patient_dir)#进入\轴路径
		
		image_names = os.listdir(patient_dir)#找到该路径下所有图像
		
		file_content = []
		for img_name in image_names:
			if img_name.startswith('result'):
				XX = misc.imread(img_name)
				#If it's a gray image, shape of XX would be 2d ,sth like (73,63)
				if not XX.shape:
					print "shape error img_name%s" % img_name
					break
				if len(XX.shape) == 2:
					pass
				else:
					XX= XX[:,:,0] if XX.shape[2] > 1 else XX#if RGB,only tackle R
					
				print "%s---------%s" % (patients_name,img_name)
				
				[MEAN,SD,CT,HG,MP,ENG,INE,IDM,ENT,COR,SM,DM,SE,DE,ANGLES] = ccf.ccf(XX)
				results = ccf.ccf(XX)
				vec = []
				for r in results[:-1]:#The last item has 3 cells
					vec+= r
					
				
				file_content.append(vec)
		
		if file_content:
			os.chdir(save_path)
			#os.mkdir(patients_name)
			#os.chdir(os.path.join(save_path,patients_name))
			file_name = patients_name+'.txt'
			np.savetxt(file_name, file_content,fmt="%f", delimiter=",")
			print(1)
			#the_file = open("i.txt",'w')
			#the_file.writelines(file_content)
			#the_file.close()
		
		
				

print(13)