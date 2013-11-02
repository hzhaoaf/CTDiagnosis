#coding=utf8
import sys, os
import sqlite3

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


