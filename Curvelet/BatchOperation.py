# -*- coding: utf-8 -*- 

import os

imageDir = u"C:\\Users\\Charles\\Desktop\\dcmProgram\\病例\\良性"
#os.chdir(imageDir)
info_dic = {}

patients_name_list = os.listdir(imageDir)
for patients_name in patients_name_list:
	patient_dir = os.path.join(imageDir, patients_name)
	if os.path.isdir(patient_dir):
		patient_dir = os.path.join(patient_dir,u"轴")
		info_dic[patients_name] = []
		image_names = os.listdir(patient_dir)
		for img_name in image_names:
			if img_name.startswith('result'):
				image_path = os.path.join(patient_dir,img_name)
				info_dic[patients_name].append(image_path)
				
print(13)