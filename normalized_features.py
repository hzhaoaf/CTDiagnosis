#coding=utf8
'''
    这个脚本从外部的文件中导入需要从存入数据库的字段
    patient_features, image_features, label
'''
import os, json
#import pdb;pdb.set_trace()
well_dir = u'F:\良性'
ill_dir = u'F:\恶性'
files = os.listdir(ill_dir)
name_labels = {}
name_features = {}
name_images = {}

def convert_feature_list(converting_list):
    convert_indexs  = [14,12,19,0,1,18,17,10,3,4,8,13,11,2,5,7,6,9,15,16]
    feature =[ None for i in range(20)]

    for count, index in enumerate(convert_indexs):
        feature[index] = converting_list[count]
    return feature


for f in files:
    print f
    lines = open('%s/%s' % (ill_dir, f), 'r').readlines()
    if f == 'patient_features.txt':
        lines = lines[1:]
        lines = [l.strip().split('\t') for l in lines if l]
        name_labels = {l[0]: l[1] for l in lines}
        name_features = {l[0]: convert_feature_list(l[2:]) for l in lines}
    else:
        lines = [l.strip() for l in lines if l]
        for l in lines:
            features = l.split(',')
            image_name = f.split('.')[0]
            name_images.setdefault(image_name, []).append(features)
res = []
for name, images_features in name_images.items():
    for image_features in images_features:
        label = name_labels.get(name.encode('utf8'), '-1')
        patient_features = name_features.get(name.encode('utf8'), [])
        res.append([name.encode('utf8'), label, ','.join(patient_features), ','.join(image_features)])

f = open('normalized_ill_features.txt', 'w+')
for r in res:
    #print r
    line = '%s\n' % '----'.join(r)
    f.write(line)
f.close()
