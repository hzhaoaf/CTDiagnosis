import numpy as np
from sklearn.svm import NuSVC
from sklearn.externals import joblib
import time

train_data = '../data/trainData-36-9-19.txt'
#path = os.path.normcase("c:/mydir/mysubdir/")


def parse_data(filename):
    '''
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
    
    
def svm():
    print "enter svm"
    features, labels, names = parse_data(train_data)
    train_features, train_labels, train_names = features[:-5], labels[:-5], names[:-5]
    test_features, test_labels, test_names = features[-5:], labels[-5:], names[-5:]
    print "get train data", len(train_features), len(train_features)
    X = np.array(train_features)
    y = np.array(train_labels)
    print "start create model"
    start = time.time()
    #clf = NuSVC(kernel='linear')
    #clf.fit(X, y)
    clf = load_model()
    save_model(clf)
    print "fit model cost %.2fs" % (time.time() - start)
    for index, f in enumerate(test_features):
        print "file %s predict %s labeled answer %s" % (test_names[index], clf.predict(test_features[index]), test_labels[index])

def save_model(clf):
    filename = 'test_model.joblib.pkl'
    joblib.dump(clf, filename, compress=9)

def load_model():
    filename = 'test_model.joblib.pkl'
    clf = joblib.load(filename)
    return clf

if __name__ == "__main__":
    svm()


    
    

