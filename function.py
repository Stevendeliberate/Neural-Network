import numpy as np 
import matplotlib.pyplot as plt 

class function():
    def __init__(self):
        pass
    
    def sgn(self,x_data):
        x = x_data.copy()
        temp = x>0
        x[temp] = 1
        x[~temp] = -1
        return x
    
    def purline(self,x_data):
        x = x_data.copy()
        return x
    
    def sigmoid(self,x_data):
        x = x_data.copy()
        y = 1 / (1 + np.exp(-x))
        return y

'''
x_data = np.linspace(-5,5,50)

a = function()
y_data = a.sgn(x_data)

plt.plot(x_data , y_data , 'r')
ax = plt.gca()                      #gca：get current axis
ax.xaxis.set_ticks_position("bottom")
ax.yaxis.set_ticks_position("left")
ax.spines['bottom'].set_position(('data',0))
ax.spines['left'].set_position(('data',0))
plt.show()
'''