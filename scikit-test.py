import numpy as np
import matplotlib.pyplot as plt

content = np.loadtxt("german.data-numeric")
newX = content[1]
#b=np.vstack((content[:,1],content[:,2]))
#print b

X = np.array([[-1, -1], [-2, -1], [-3, -2], [1, 1], [2, 1], [3, 2]])
Y = np.array([1, 1, 1, 2, 2, 2])
from sklearn.naive_bayes import GaussianNB
clf = GaussianNB()
clf.fit(X, Y)
GaussianNB()
#print(clf.predict([[-0.8, 1]]))