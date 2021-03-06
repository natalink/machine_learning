#!/usr/bin/env python
import numpy as np
import matplotlib.pyplot as plt
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier, AdaBoostClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.lda import LDA
from sklearn.qda import QDA

train = np.loadtxt("german.data-numeric")
new = np.array(train)
train_x = new[0:(len(new)-100),0:24]
train_y = new[0:(len(new)-100),24]
test_x = new[(len(new)-100):,0:24]
test_y = new[(len(new)-100):,24]

classifiers = [
    GaussianNB(),
    KNeighborsClassifier(3),
#    SVC(kernel="linear", C=0.025),
#    SVC(gamma=2, C=1),
    DecisionTreeClassifier(max_depth=5),
#    RandomForestClassifier(max_depth=5, n_estimators=10, max_features=1),
    AdaBoostClassifier(),
    LDA(),
    QDA()]

for classifier in classifiers:
    print "============================================="
    print "Training classifier", classifier
    clf = classifier
    clf.fit(train_x, train_y)

#neigh = KNeighborsClassifier(n_neighbors=6)
#neigh.fit(train_x, train_y)
    print(clf.score(test_x, test_y))
    #print "=============================================="
#print(neigh.score(test_x, test_y))
