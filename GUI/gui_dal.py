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
                create_time datetime default current_timestamp
                )
              ''',
              '''create table if not exists image (
                id integer primary key autoincrement,
                name text, -- u'图片名'
                directory text, -- 图片存放目录
                features text, --图片的全部特征
                type int, --图片类型，0:训练数据 1: 预测数据
                label int, --图片的label(type为0时才有值)，0：不患病 1: 患病
                create_time datetime default current_timestamp
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

    def show_tables(self):
        sql = "select * from diagnosis_record"
        self.cursor.execute(sql)
        print 'all tables', self.cursor.fetchall()

if __name__ == '__main__':
    gui_dal = GUIDAL()
    gui_dal.show_tables()
    images = [{'name': 'file2', 'features': '{}', 'type': 1, 'label': 2},
              {'name': 'file3', 'features': '{}', 'type': 1, 'label': 2},
              {'name': 'file4', 'features': '{}', 'type': 1, 'label': 2},
              {'name': 'file5', 'features': '{}', 'type': 1, 'label': 2},]
    images = {'name': 'file1', 'features': '{}', 'type': 1, 'label': 2}
    gui_dal.save_images(images)


