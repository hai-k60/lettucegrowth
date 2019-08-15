from sklearn.linear_model import Ridge
import numpy as np
from matplotlib import pyplot as plt 
line= np.loadtxt("data30fix.txt", comments="#",dtype='float', delimiter=" ", unpack=False)

x=line[:,0]
X=np.array([x]).T
y=line[:,1]
y=np.array([y])[0]

# n_samples, n_features = 10, 5
# rng = np.random.RandomState(0)
# y = rng.randn(n_samples)
# X = rng.randn(n_samples, 1)
print(X)
print(y)
clf = Ridge(alpha=2.0)
clf.fit(X, y) 
#Ridge(alpha=1.0, copy_X=True, fit_intercept=True, max_iter=None,
#     normalize=False, random_state=None, solver='auto', tol=0.001)
print(clf.predict(X))
print(clf.coef_)
plt.plot(x,y,"ob") 
plt.show()