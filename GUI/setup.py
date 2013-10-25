from distutils.core import setup
import py2exe

import sys
sys.path.append('../')
dcm = 'dcm.testDCM'
svm_path = 'svm.svm'

setup(windows=[{"script":"MainWindow.py"}],
      options={"py2exe":{
                    "includes" : ["sip", dcm, svm_path,
                                  'sklearn',
                                  'scipy.sparse.csgraph._validation',
                                  'sklearn.linear_model.sgd_fast.weight_vector']}})

