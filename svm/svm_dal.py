#coding=utf8
import sys, os
import sqlite3
import json

sys.path.append('../')

import config
from config import database_path
#这里需要根据config所在路径计算database_path的最终路径
database_path = '%s/%s' % (os.path.dirname(config.__file__), database_path)

class SVMDAL:

    def __init__(self):
        self.conn = sqlite3.connect(database_path)
        self.cursor = self.conn.cursor()

    def select_trainning_data(self):
        '''
            从training_data表中选出type为0的记录，读入其features和label
        '''
        sql = 'select patient_features, image_features, label from training_data'
        self.cursor.execute(sql)
        return self.cursor.fetchall()

    def save_training_data(self, filenames, images_features, labels):
        sql = "insert into training_data(image_name, image_features, label) values (?, ?, ?)"
        rows = []
        for i in range(0, len(filenames)):
            name = filenames[i]
            image_feautures = json.dumps(images_features[i])
            label = labels[i]
            rows.append((name, image_feautures, label))
        self.cursor.executemany(sql, rows)
        self.conn.commit()

    def save_withP_training_data(self, rows):
        sql = "insert into training_data(patient_features, image_features, label) values (?, ?, ?)"
        self.cursor.executemany(sql, rows)
        self.conn.commit()




