import numpy as np 
from matplotlib import pyplot as plt 
from sklearn import datasets, linear_model
line= np.loadtxt("data30fix.txt", comments="#",dtype='float', delimiter=" ", unpack=False)

x=line[:,0]
x=np.array([x]).T
y=line[:,1]
y=np.array([y]).T

one = np.ones((x.shape[0],1))
xbar = np.concatenate((one, x),axis=1)
print(xbar)
print(x)
print(y)
reg=linear_model.LinearRegression()
reg.fit(xbar,y)
print(reg.coef_)

w0=reg.coef_[0][0]
w1=reg.coef_[0][1]

print(w0)
print(w1)

x0=np.linspace(0,810,2)
y0=w0+w1*x0

#plt.title("") 
plt.xlabel("x S (cm2)") 
plt.ylabel("y Fresh weight (g)")
plt.plot(x0,y0,"r") 
plt.plot(x,y,"ob") 
plt.show()