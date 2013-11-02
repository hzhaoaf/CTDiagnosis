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
                image_ids text, --用于该次诊断的全部图片id
                patient_info text default "", --患者其他信息，以json存储的dict
                patient_info_features text default "", --根据患者信息提取出来的特征，以json存储的list
                diagnose_time datetime,
                create_time datetime default (datetime('now', 'localtime'))
                )
              ''',
              '''create table if not exists image (
                id integer primary key autoincrement,
                name text, -- 图片名
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

    #def check_database():
    #    '''
    #        检查database_path下的是否存在，不存在的话需要创建该文件
    #    '''

    def save_images(self, images):
        '''
            保存GUI中需要记录的图像，支持批量处理
            传入参数可以为字典或者字典list
            需要返回存储图片的id
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
        sql = "select id from image where name in ({0})".format(','.join(['?' for _ in images]))
        image_names = [img['name'] for img in images]
        self.cursor.execute(sql, image_names)
        res = self.cursor.fetchall()
        return [r['id'] for r in res]

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
        images = []
        for filename, features in images_features.items():
            image = {}
            image['name'] = filename
            image['features'] = json.dumps(features)
            image['type'] = 0 if add_to_training else 1 # 0表示训练，1表示不用作训练集
            image['label'] = label
            images.append(image)

        image_ids = self.save_images(images)
        image_ids = json.dumps(image_ids)
        patient_name = patient_info.get('patient_name', '')
        #diagnose_time = patient_info['jianchariqi'] if patient_info.get("jianchariqi") else datetime.now()
        diagnose_time = datetime.now()
        patient_info = json.dumps(patient_info)
        patient_info_features = json.dumps(patient_info_features)
        probabilities = json.dumps(probabilities)

        sql = "insert into diagnosis_record (patient_name, probabilities, image_ids, patient_info, patient_info_features, diagnose_time) values (?, ?, ?, ?, ?, ?)"
        self.cursor.execute(sql, (patient_name, probabilities, image_ids, patient_info, patient_info_features, diagnose_time))
        self.conn.commit()

    def get_all_diagnosis_info():
        sql = 'select id, patient_name, diagnose_time, probabilities from diagnosis_record'
        self.cursor.execute(sql)
        records = []
        for r in self.cursor.fetchall():
            probabilities = json.loads(r['probabilities'])
            records.append([r['id'], r['patient_name'], r['diagnose_time'], probabilities[0], probabilities[1]])
        return records

    def get_one_diagosis_info(self, patient_id):
        '''
            根据患者id，查找已有诊断记录
            将患者姓名一起放到返回的dict中
        '''
        sql = 'select patient_info from diagnosis_record where id = ?';
        self.cursor.execute(sql, patient_id)
        res = self.cursor.fetchone()
        patient_info = json.loads(res['patient_info'])
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
    #gui_dal.create_tables()
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
    gui_dal.save_diagnosis_record()


