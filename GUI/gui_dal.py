#coding=utf8
import sys, os
import json
import sqlite3

from datetime import datetime
import time

sys.path.append('../')

import config
from config import database_path
#这里需要根据config所在路径计算database_path的最终路径
database_path = '%s/%s' % (os.path.dirname(config.__file__), database_path)

table_sqls = ['''create table if not exists diagnosis_record (
                id integer primary key autoincrement,
                patient_name text, -- 患者姓名
                probabilities text, -- 患病概率, json存储的tuple, (p1, p2)，分布表示是否使用用户信息进行预测
                patient_info text default "", --患者其他信息，以json存储的dict
                diagnose_time datetime,
                create_time datetime default (datetime('now', 'localtime'))
                )
              ''',
              '''create table if not exists training_data (
                id integer primary key autoincrement,
                diagnosis_id int default 0, --对应到诊断记录中的id，默认为0, 表示没有诊断记录
                patient_features text, -- 根据患者信息提取出来的特征，以json存储的list
                image_name text, --图片名
                image_features text, --图片的全部特征
                label int, --图片的label 0：不患病 1: 患病
                create_time datetime default (datetime('now', 'localtime'))
                )
              '''
            ]



class GUIDAL:

    def __init__(self):
        self.conn = sqlite3.connect(database_path)
        self.cursor = self.conn.cursor()

    #def check_database():
    #    '''
    #        检查database_path下的是否存在，不存在的话需要创建该文件
    #    '''

    def save_traning_data(self, training_data):
        '''
            保存GUI中需要进行训练的记录，支持批量处理
        '''
        records = []
        for d in training_data:
            row = (d['diagnosis_id'], d['patient_features'], d['image_name'], d['image_features'], img['label'])
            records.append(row)
        sql = "insert into training_data(diagnosis_id, patient_features, image_name, image_features, label) values (?, ?, ?, ?, ?)"
        self.cursor.executemany(sql, records)
        self.conn.commit()

    def save_diagnosis_record(self, patient_info={}, patient_info_features=[], images_features={},
                              probabilities=(0.0, 0.0), label=0, add_to_training=False):
        '''
            记录每次诊断的记录
            patient_info: 用户的相关信息, 包括diagnose_time, patient_name
            patient_info_features: 根据用户信息提取出来进行训练预测的特征
            images_features: 该次诊断涉及到的图片的特征信息, filename: [140]这样的形式
            probabilities: 两个概率值, 分别表示使用和不使用用户信息特征进行训练和预测的结果
            label: 是否患病，经过人确定之后的结果，用来作为训练数据
            add_to_training: 表示本次训练的图片是否要加到训练集

        '''

        patient_name = patient_info.get('xingming', '')
        #diagnose_time = patient_info['jianchariqi'] if patient_info.get("jianchariqi") else datetime.now()

        diagnose_time = datetime.now()
        patient_info = json.dumps(patient_info)
        probabilities = json.dumps(probabilities)

        sql = "insert into diagnosis_record (patient_name, probabilities, patient_info, diagnose_time) values (?, ?, ?, ?)"
        self.cursor.execute(sql, (patient_name, probabilities, patient_info, diagnose_time))
        self.conn.commit()

        if add_to_training:
            diagnose_id = self.cursor.lastrowid
            training_data = []
            for filename, features in images_features.items():
                d = {}
                d['diagnose_id'] = diagnose_id
                d['image_name'] = filename
                d['patient_features'] = json.dumps(patient_features)
                d['image_features'] = json.dumps(features)
                d['label'] = label
                training_data.append(d)
            self.save_traning_data(training_data)

    def get_all_diagnosis_info(self):
        sql = 'select id, patient_name, diagnose_time, probabilities from diagnosis_record'
        self.cursor.execute(sql)
        records = []
        for r in self.cursor.fetchall():
            probabilities = json.loads(r[3])
            records.append([r[0], r[1], r[2], probabilities[0], probabilities[1]])
        return records

    def get_one_diagosis_info(self, patient_id):
        '''
            根据患者id，查找已有诊断记录
            将患者姓名一起放到返回的dict中
        '''
        sql = 'select patient_info from diagnosis_record where id = %d' %patient_id
       # self.cursor.execute(sql, patient_id)
        self.cursor.execute(sql)
        res = self.cursor.fetchone()
        patient_info = json.loads(res[0])
        return patient_info

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
    gui_dal.create_tables()
    #gui_dal.show_tables()
    #images = [{'name': 'file2', 'features': '{}', 'type': 1, 'label': 2},
    #          {'name': 'file3', 'features': '{}', 'type': 1, 'label': 2},
    #          {'name': 'file4', 'features': '{}', 'type': 1, 'label': 2},
    #          {'name': 'file5', 'features': '{}', 'type': 1, 'label': 2},]
    #images = {'name': 'file1', 'features': '{}', 'type': 1, 'label': 2}
    #gui_dal.save_images(images)
    #from datetime import datetime
    #records = [{'patient_name': u'张三', 'probabilities': 0.5, 'image_ids': '[4, 5, 6]', 'patient_info': '{"age": 45}', 'patient_info_features': '[]', 'diagnose_time': datetime.now()},
    #           {'patient_name': u'李四', 'probabilities': 0.6, 'image_ids': '[4, 5, 6]', 'patient_info': '{"age": 46}', 'patient_info_features': '[]', 'diagnose_time': datetime.now()},
    #           {'patient_name': u'王二', 'probabilities': 0.7, 'image_ids': '[4, 5, 6]', 'patient_info': '{"age": 47}', 'patient_info_features': '[]', 'diagnose_time': datetime.now()},
    #           {'patient_name': u'赵六', 'probabilities': 0.8, 'image_ids': '[4, 5, 6]', 'patient_info': '{"age": 48}', 'patient_info_features': '[]', 'diagnose_time': datetime.now()}]
    ##records = [{'patient_name': '张三', 'probability': 0.5, 'image_ids': '[4, 5, 6]', 'patient_info': '{'age: 45}', 'diagnose_time': datetime.now()}]
    #gui_dal.save_diagnosis_records(records)
    #print gui_dal.get_diag_records_by_patient_name(u'张三')
    #gui_dal.save_diagnosis_record()


