import matplotlib.pyplot as plt 
import numpy as np 

def purelin(x):
    return x

x_data = np.random.normal(-10,10,20)
x_data = np.sort(x_data)

y_data = purelin(x_data)

plt.plot(x_data,y_data,'r')
plt.show()