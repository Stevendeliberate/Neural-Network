import numpy as np 
import matplotlib.pyplot as plt 
from mpl_toolkits.mplot3d.axes3d import Axes3D

def sgn(data):
    x = data.copy()
    temp = x>0
    x[temp] = 1
    temp = x<=0
    x[temp] = 0
    return x

def update(x,y,w,lr=0.03,epoches=50000):
    for i in range(epoches):
        t = sgn(np.dot(w , x))
        w_gard = y - t
        w += lr * np.dot(w_gard,x.T)
    return w

#数据产生
x_data = np.random.normal(-10,10,(2,10))
x_data = np.sort(x_data)
y_data = np.random.randint(0,2,(1,10))
y_data = np.sort(y_data)

#数据预处理
x_data = np.r_[x_data,np.ones(x_data.shape[1]).reshape((1,10))]
w = np.ones(x_data.shape[0])
w = w[np.newaxis,:]

print("x_data:",x_data)
print("y_data:",y_data)
print("w:",w)

w = update(x_data,y_data,w)
print(w)



#2dim绘图
#计算分解线的斜率和截距
k = -w[0,0]/w[0,1]
b = -w[0,2]/w[0,1]

#随机样本
x_test = np.random.normal(-10,10,(2,10))
x_test = np.sort(x_test)
y_test = x_test[0,:]*k + b
print(x_test)
print(y_test)
plt.scatter(x_data[0,:],x_data[1,:],c = y_data[0,:])
plt.plot(x_test[0,:],y_test,'r')
plt.show()

'''
#3dim绘图
fig = plt.figure()
ax = Axes3D(fig)
k1 = -w[0,0]/w[0,2]
k2 = -w[0,1]/w[0,2]
b = -w[0,3]/w[0,2]
#随机样本
x_test = np.random.normal(-10,10,(3,10))
x_test = np.sort(x_test)
print(x_test)
ax.scatter3D(x_data[0,:],x_data[1,:],x_data[2,:] , c = y_data[0,:])
X,Y = np.meshgrid(x_test[0,:],x_test[1,:])
Z = X*k1 + Y * k2 + b
ax.plot_surface(X,Y,Z,color = 'blue')
plt.show()
'''