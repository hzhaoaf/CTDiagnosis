#coding=utf8
import time, json
import numpy as np
from sklearn.svm import NuSVC
from sklearn.externals import joblib

from svm_dal import SVMDAL

train_data = '../data/trainData-36-9-19.txt'
svm_path = '../data/svm/test_model.joblib.pkl'

class SVM:

    def __init__(self):
       self.svm_path = svm_path
       self.load_svm()
       self.dal = SVMDAL()

    def load_svm(self):
        self.clf = joblib.load(self.svm_path)

    def get_trainning_data(self):
        '''
            从数据库中获取全部训练数据
        '''
        res = self.dal.select_trainning_data()
        features, labels = [], []
        for r in res:
            f = json.loads(r[0])
            features.append(f)
            labels.append(r[1])
        return features, labels

    def get_trainning_data_from_file(self, filename):
        '''
            重新读入训练集
        '''
        f = open(filename, 'r')
        line = f.readline()
        features = []
        labels = []
        names = []
        while line:
            if line.startswith("#"):
                line = f.readline()
                continue
            parts = line.strip().split('\t')
            labels.append(int(parts[1]))
            features.append([float(r) for r in parts[2:]])
            names.append(parts[0])
            line = f.readline()
        return features, labels, names

    def update_svm(self):
        '''
            增加训练集后，重新训练模型
        '''
        self.get_trainning_data()
        self.train_svm()
        self.load_svm()

    def train_svm(self):
        features, labels, names = self.get_trainning_data()
        X = np.array(features)
        y = np.array(labels)
        clf = NuSVC(kernel='linear')
        clf.fit(X, y)
        joblib.dump(clf, self.svm_path, compress=9)

    def predict(self, test_data):
        '''
            传入N组数据进行预测，返回患病概率（患病数/N）
        '''
        test_num = len(test_data)
        test_res = self.clf.predict(test_data)
        print test_res
        positive_num = len([r for r in test_res if r == 1])
        return positive_num / float(test_num)

if __name__ == '__main__':
    svm = SVM()
    features, labels, names = svm.get_trainning_data(train_data)
    test_features, test_labels, test_names = features[-5:], labels[-5:], names[-5:]
    print svm.predict(test_features)




