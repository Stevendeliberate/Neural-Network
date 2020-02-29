import numpy as np 
import matplotlib.pyplot as plt 

def sigmoid(x):
    y = 1 / (1 + np.exp(-x))
    return y

def Dsigmoid(x):
    return x * (1 - x)

'''
x_data = np.linspace(-5,5,50)
y_data = sigmoid(x_data)

plt.plot(x_data , y_data , 'r')
ax = plt.gca()                      #gca：get current axis
ax.xaxis.set_ticks_position("bottom")
ax.yaxis.set_ticks_position("left")
ax.spines['bottom'].set_position(('data',0))
ax.spines['left'].set_position(('data',0))
plt.show()
'''