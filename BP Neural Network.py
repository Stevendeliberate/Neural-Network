import numpy as np 
import matplotlib.pyplot as plt 
from sigmoid import sigmoid

#输入数据
X = np.array([[1,0,0]
             ,[1,0,1]
             ,[1,1,0]
             ,[1,1,1]])

#标签
Y = np.array([[0,1,1,0]])

#隐层偏置值 隐层神经元设为5个
w = np.random.random((3,5))
#输出层偏置值，输出层只有一个神经元
v = np.random.random((5,1))
hidden_layer = np.dot(X,w)
output_layer = np.dot(hidden_layer,v)
t = sigmoid(output_layer)
print(t)
'''
for i in range(50000):
    hidden_layer = np.dot(X,w)
    output_layer = np.dot(hidden_layer,v)

    print(output_layer)
'''
