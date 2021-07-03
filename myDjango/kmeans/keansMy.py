import joblib
from sklearn.cluster import MiniBatchKMeans
import sklearn.svm as svm
import os
from sklearn.cluster import KMeans
import numpy as np
import traceback

#设置递归深度
import sys
sys.setrecursionlimit(1000000)


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

#模型储存路径
dir_str = os.path.join(BASE_DIR,"module_static","module.txt")

def train(data):
    X_train,Y_train = divide(np.array(data))
    _train(X_train,Y_train,dir_str)
    return True


def dev(data):
    X_test, Y_true = divide(np.array(data))
    Y_pre =_test(dir_str,X_test)
    Y_pre = array2list(Y_pre)
    Y_true = array2list(Y_true)
    return {'y_true':Y_true,'y_pre':Y_pre}

def run(data):
    data = np.array(data)
    #划分
    datax = data[:, 1:data.shape[1]]
    #预测
    Y_pre = _test(dir_str,datax)
    array2list(Y_pre)
    return Y_pre


#划分，去除第一列序号，最后两列是标签
def divide(train):
    X_train = train[:, 2:train.shape[1] - 2]
    y_train = train[:, [-2, -1]]
    return X_train, y_train


def _train(X_train, y_train, path):
    try:
        y_copy = []
        for item in y_train:
            y_copy.append(item[0] * 2 + item[1])
        model = svm.SVC(kernel='linear',C=0.4)
        model.fit(X_train, np.array(y_copy))
        joblib.dump(filename=path, value=model)
    except Exception:
        traceback.print_exc()



def _test(path, X_test):
    model = joblib.load(path)
    y_copy = model.predict(X_test)
    y_pre = []
    for item in y_copy:
        if item == 3:
            y_pre.append([1, 1])
        elif item == 2:
            y_pre.append([1, 0])
        elif item == 1:
            y_pre.append([0, 1])
        elif item == 0:
            y_pre.append([0, 0])
    return y_pre


def array2list(data):
    data = list(data)
    for i in range(len(data)):
        data[i] = list(data[i])
    return data