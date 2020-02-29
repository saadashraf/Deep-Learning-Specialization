import numpy
from dnn_app_utils_v3 import *

A = numpy.array([[1, 2, 3],
                [3 , 4 , 5]])

ans, cache = sigmoid(A)

print(ans)