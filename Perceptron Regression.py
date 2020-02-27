import numpy as np 
import matplotlib.pyplot as plt 

def purelin(x):
    return x

def update(x,y,w,lr,epochs):
    for i in range(epochs):
       t = purelin(np.dot(x,w))
       y_gard = y - t
       w = w + lr * np.dot(x.T,y_gard)/x.shape[0]
    return w

#训练数据
x_data = np.linspace(-10,10,20).reshape(20,1)
nosie = np.random.normal(-0.1,0.1,20).reshape(20,1)
y_data = x_data * 0.2 + 2 + nosie

#绘制训练数据的散点图
plt.scatter(x_data,y_data,c = 'r')


#数据准备
x_data = np.c_[x_data,np.ones(x_data.shape)]
w = np.ones((1,x_data.shape[1])).reshape(2,1)

w = update(x_data , y_data , w , 0.01 , 500000)
print(w)

x_test = np.linspace(-10,10,10).reshape(10,1)
x_test = np.c_[x_test,np.ones(x_test.shape)]
y_test = np.dot(x_test , w)
plt.plot(x_test[:,0],y_test,'b')
plt.show()

