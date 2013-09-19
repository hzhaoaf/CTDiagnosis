import numpy as NP
from svm import *

#Data = NP.random.randint(-5, 5, 1000).reshape(500, 2)

#rx = [ (x**2 + y**2) < 9 and 1 or 0 for (x, y) in Data ]

#px = svm_problem(rx, Data)

#pm = svm_parameter(kernel_type=RBF)

#v = svm_model(px, pm)

#v.predict([3, 1])

from libsvm import *
prob = svm_problem([1,-1],[[1,0,1],[-1,0,-1]])
param = svm_parameter(kernel_type = LINEAR, C = 10)
  ## training  the model
m = svm_model(prob, param)
#testing the model
m.predict([1, 1, 1])
