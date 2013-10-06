#coding=utf8
import sys, os
import sqlite3

sys.path.append('../')

import config
from config import database_path
#这里需要根据config所在路径计算database_path的最终路径
database_path = '%s/%s' % (os.path.dirname(config.__file__), database_path)

table_sqls = ['''create table if not exists diagnosis_record (
                id integer primary key autoincrement,
                patient_name text, -- 患者姓名
                probability real, -- 患病概率
                image_ids text, --用于该次诊断的全部图片id
                patient_info text default "", --患者其他信息，以json存储
                diagnose_time datetime,
                create_time datetime default (datetime('now', 'localtime'))
                )
              ''',
              '''create table if not exists image (
                id integer primary key autoincrement,
                name text, -- 图片名
                directory text, -- 图片存放目录
                features text, --图片的全部特征
                type int, --图片类型，0:训练数据 1: 预测数据
                label int, --图片的label(type为0时才有值)，0：不患病 1: 患病
                create_time datetime default (datetime('now', 'localtime'))
                )
              '''
            ]

class GUIDAL:

    def __init__(self):
        self.conn = sqlite3.connect(database_path)
        self.cursor = self.conn.cursor()

    def save_images(self, images):
        '''
            保存GUI中需要记录的图像，支持批量处理
            传入参数可以为字典或者字典list
        '''
        if not isinstance(images, list):
            images = [images]
        records = []
        for img in images:
            row = (img['name'], img['features'], img['type'], img['label'])
            records.append(row)
        sql = "insert into image (name, features, type, label) values (?, ?, ?, ?)"
        self.cursor.executemany(sql, records)
        self.conn.commit()

    def save_diagnosis_records(self, diag_records):
        '''
            记录每次诊断的记录
        '''
        if not isinstance(diag_records, list):
            diag_records= [diag_records]
        db_records = []
        for r in diag_records:
            row = (r['patient_name'], r['probability'], r['image_ids'], r['patient_info'], r['diagnose_time'])
            db_records.append(row)
        sql = "insert into diagnosis_record (patient_name, probability, image_ids, patient_info, diagnose_time) values (?, ?, ?, ?, ?)"
        self.cursor.executemany(sql, db_records)
        self.conn.commit()

    def get_diag_records_by_patient_name(self, patient_name):
        '''
            根据患者姓名，查找已有诊断记录，返回一个list
        '''
        sql = 'select * from diagnosis_record where patient_name = ?';
        self.cursor.execute(sql, (patient_name, ))
        return self.cursor.fetchall()

    def create_tables(self):
        '''
            debug method
        '''
        for sql in table_sqls:
            self.cursor.execute(sql)
            self.conn.commit()

    def show_tables(self):
        '''
           debug method
        '''
        sql = "select * from diagnosis_record"
        self.cursor.execute(sql)
        print 'all tables', self.cursor.fetchall()

if __name__ == '__main__':
    gui_dal = GUIDAL()
    #gui_dal.create_tables()
    #gui_dal.show_tables()
    #images = [{'name': 'file2', 'features': '{}', 'type': 1, 'label': 2},
    #          {'name': 'file3', 'features': '{}', 'type': 1, 'label': 2},
    #          {'name': 'file4', 'features': '{}', 'type': 1, 'label': 2},
    #          {'name': 'file5', 'features': '{}', 'type': 1, 'label': 2},]
    #images = {'name': 'file1', 'features': '{}', 'type': 1, 'label': 2}
    #gui_dal.save_images(images)
    #from datetime import datetime
    #records = [{'patient_name': u'张三', 'probability': 0.5, 'image_ids': '[4, 5, 6]', 'patient_info': '{"age": 45}', 'diagnose_time': datetime.now()},
    #           {'patient_name': u'李四', 'probability': 0.6, 'image_ids': '[4, 5, 6]', 'patient_info': '{"age": 46}', 'diagnose_time': datetime.now()},
    #           {'patient_name': u'王二', 'probability': 0.7, 'image_ids': '[4, 5, 6]', 'patient_info': '{"age": 47}', 'diagnose_time': datetime.now()},
    #           {'patient_name': u'赵六', 'probability': 0.8, 'image_ids': '[4, 5, 6]', 'patient_info': '{"age": 48}', 'diagnose_time': datetime.now()}]
    #records = [{'patient_name': '张三', 'probability': 0.5, 'image_ids': '[4, 5, 6]', 'patient_info': '{'age: 45}', 'diagnose_time': datetime.now()}]
    #gui_dal.save_diagnosis_records(records)
    gui_dal.get_diag_records_by_patient_name(u'张三')


