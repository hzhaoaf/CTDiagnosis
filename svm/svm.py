#coding=utf8
import time, json, doctest
import numpy as np
from sklearn.svm import NuSVC
from sklearn.externals import joblib

from svm_dal import SVMDAL

train_data = '../data/trainData-36-9-19.txt'
withP_svm_path = '../data/svm/with_patients_model.joblib.pkl'
withoutP_svm_path = '../data/svm/without_patients_model.joblib.pkl'

def merge_arrays(array1, array2):
    '''
    将两个矩阵的每一行合并起来
    >>> merge_arrays([[1, 2], [3, 4]], [[5, 6], [7, 8]])
    [[1, 2, 5, 6], [3, 4, 7, 8]]
    '''

    merged_list = []
    for i in range(0, len(array1)):
        merged_list.append(array1[i] + array2[i])
    return merged_list


class SVM:

    def __init__(self):
        self.withP_svm_path = withP_svm_path
        self.withoutP_svm_path = withoutP_svm_path
        self.load_svm()
        self.dal = SVMDAL()

    def load_svm(self):
        self.withP_clf = joblib.load(self.withP_svm_path)
        self.withoutP_clf = joblib.load(self.withoutP_svm_path)

    def get_trainning_data(self):
        '''
            从数据库中获取全部训练数据
            返回两套训练数据，一个有用户信息，一个没有用户信息
        '''
        res = self.dal.select_trainning_data()
        patients_features = []
        images_features = []
        withoutP_features = []
        labels = []
        for r in res:
            if r[0]:
                patients_features.append(json.loads(r[0]))
                images_features.append(json.loads(r[1]))

            #当patient_features没有值的时候，表示这个数据只用来训练无用户信息的svm
            withoutP_features.append(json.loads(r[1]))
            labels.append(r[2])
        withP_features = merged_list(patient_features, images_features)
        return withP_features, withoutP_features, labels

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

    def train_svm(self):
        '''
            从数据库中取出训练数据，然后训练生成两个svm，一个使用用户特征，一个不使用用户特征
        '''
        #features, labels, names = self.get_trainning_data_from_file(train_data)
        withP_features, withoutP_features, labels = self.get_trainning_data()
        X = np.array(withoutP_features)
        y = np.array(labels)
        clf = NuSVC(kernel='rbf')
        clf.fit(X, y)
        joblib.dump(clf, self.withoutP_svm_path, compress=9)

        X = np.array(withP_features)
        clf = NuSVC(kernel='rbf')
        clf.fit(X, y)
        joblib.dump(clf, self.withP_svm_path, compress=9)

    def predict(patient_info_feature=[], images_features={}):
        '''
            传入N组数据进行预测，分布使用含用户信息的svm和不含用户信息的svm进行预测患病概率（患病数/N）
            返回一个tuple(p1, p2)
            p1-使用用户信息的svm
            p2-不使用用户信息的svm
        '''
        pred_num = len(images_features.keys())
        withP_pred_data = []
        withoutP_pred_data = []
        for filename, image_features in images_features.items():
            withP_pred_data.append(image_features)
            withoutP_pred_data.append(patient_info_feature + image_features)
        withP_res = self.withP_clf.predict(withP_pred_data)
        print withP_res
        positive_num = len([r for r in withP_res if r == 1])
        withP_probability = positive_num / float(pred_num)

        withoutP_res = self.withoutP_clf.predict(withoutP_pred_data)
        print withoutP_res
        positive_num = len([r for r in withoutP_res if r == 1])
        withoutP_probability = positive_num / float(pred_num)
        return (withP_probability, withoutP_probability)

if __name__ == '__main__':
    #svm = SVM()
    a = [[1, 2], [3, 4], [5, 6]]
    b = [[4, 5], [8, 9], [10, 11]]
    print merge_arrays(a, b)
    #features, labels, names = svm.get_trainning_data(train_data)
    #test_features, test_labels, test_names = features[-5:], labels[-5:], names[-5:]
    #print svm.predict(test_features)
    doctest.testmod()


