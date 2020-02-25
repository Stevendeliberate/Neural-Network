import numpy as np 
import matplotlib.pyplot as plt

def sgn(data):                  #定义sgn函数，大于0的数输出1，小于等于0的数输出-1
    x = data.copy()
    temp = x>0
    x[temp] = 1
    x[~temp] = -1
    return x

x = np.random.normal(-10,10,100)    #按照正态分布随机100个数
x = np.sort(x)                      #将随机的数排序
y = sgn(x)                          #进行sgn计算

plt.plot(x , y , "r",linewidth = 5) #绘图

#修改坐标轴位置，将原点放在零点处。
ax = plt.gca()                      #gca：get current axis
ax.xaxis.set_ticks_position("bottom")
ax.yaxis.set_ticks_position("left")
ax.spines['bottom'].set_position(('data',0))
ax.spines['left'].set_position(('data',0))

plt.show()

