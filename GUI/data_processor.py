#coding=utf8
import sqlite3

database_path = '../data/database/ctdiagnosis.db'
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

class DataProcessor:

    def __init__(self):
        self.init_database()

    def init_database(self):
        try:
            self.conn = sqlite3.connect(database_path)
            self.cursor = self.conn.cursor()
            for sql in table_sqls:
                print sql
                self.cursor.execute(sql)
                self.conn.commit()
        except Exception as e:
            print e

    def show_tables(self):
        sql = "select * from diagnosis_record"
        self.cursor.execute(sql)
        print 'all tables', self.cursor.fetchall()

if __name__ == '__main__':
    data_processor = DataProcessor()
    data_processor.show_tables()

