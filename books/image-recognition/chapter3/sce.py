# -*- coding: utf-8 -*-
"""
Created on Sat Jul 22 14:23:26 2017
"""
import matplotlib.pyplot as plt
from sklearn import datasets

iris = datasets.load_iris()

Y = iris.target
X = iris.data[:,2:]
length = X[:,0]
breadth = X[:,1]

plt.plot(length[0:50],breadth[0:50],'o',label='setosa')
plt.plot(length[50:100],breadth[50:100],'o',label='versicolor')
plt.plot(length[100:150],breadth[100:150],'o',label='virginica')
plt.xlim([0,8])
plt.ylim([-1,3])
plt.xlabel('length')
plt.ylabel('breadth')
plt.legend(loc='lower right')
plt.show()

# PCA
from sklearn.decomposition import PCA
pca = PCA(n_components = 2)
pca.fit(X)
X_pca = pca.transform(X)

plt.plot(X_pca[0:50,0],X_pca[0:50,1],'o',label='setosa')
plt.plot(X_pca[50:100,0],X_pca[50:100,1],'o',label='versicolor')
plt.plot(X_pca[100:150,0],X_pca[100:150,1],'o',label='virginica')
plt.xlim([-4,4])
plt.ylim([-2,2])
plt.xlabel('PC1')
plt.ylabel('PC2')
plt.title('PCA')
plt.legend(loc='lower right')
plt.show()

# whitening
import numpy as np

mean = np.mean(X,0)
cov = np.cov(X, rowvar=0)
v, S = np.linalg.eig(cov)
Lambda = np.dot(np.dot(np.linalg.inv(S), cov), S)
xmu =  X - mean
Lambda_invhalf = np.linalg.inv(np.sqrt( np.diag (Lambda) ) * np.identity(2))
X_whiten =xmu.dot(S).dot(Lambda_invhalf.transpose())

plt.plot(X_whiten[0:50,0],X_whiten[0:50,1],'o',label='setosa')
plt.plot(X_whiten[50:100,0],X_whiten[50:100,1],'o',label='versicolor')
plt.plot(X_whiten[100:150,0],X_whiten[100:150,1],'o',label='virginica')
plt.xlim([-3,3])
plt.ylim([-4,4])
plt.title('whiten')
plt.legend(loc='lower right')
plt.show()

# Fisher LDA
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
lda = LinearDiscriminantAnalysis(n_components=2)
lda.fit(X, Y)
X_lda = lda.transform(X)

plt.plot(X_lda[0:50,0],X_lda[0:50,1],'o',label='setosa')
plt.plot(X_lda[50:100,0],X_lda[50:100,1],'o',label='versicolor')
plt.plot(X_lda[100:150,0],X_lda[100:150,1],'o',label='virginica')
plt.title('Fisher LDA')
plt.legend(loc='lower right')
plt.show()

# Fisher LDA n=1
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
lda = LinearDiscriminantAnalysis(n_components=1)
lda.fit(X, Y)
X_lda = lda.transform(X)

plt.plot(X_lda[0:50,0],'o',label='setosa')
plt.plot(X_lda[50:100,0],'o',label='versicolor')
plt.plot(X_lda[100:150,0],'o',label='virginica')
plt.title('Fisher LDA (n=1)')
plt.legend(loc='lower right')
plt.show()

# CCA
from sklearn.cross_decomposition import CCA
cca = CCA(n_components=2)
cca.fit(X, Y)
X_cca = lda.transform(X)

plt.plot(X_cca[0:50,0],X_cca[0:50,1],'o',label='setosa')
plt.plot(X_cca[50:100,0],X_cca[50:100,1],'o',label='versicolor')
plt.plot(X_cca[100:150,0],X_cca[100:150,1],'o',label='virginica')
plt.xlim([-8,9])
plt.ylim([-4,4])
plt.title('CCA')
plt.legend(loc='lower right')
plt.show()

# PLS
from sklearn.cross_decomposition import PLSRegression
pls2 = PLSRegression(n_components=2)
pls2.fit(X, Y)
X_pls = pls2.transform(X)

plt.plot(X_pls[0:50,0],X_pls[0:50,1],'o',label='setosa')
plt.plot(X_pls[50:100,0],X_pls[50:100,1],'o',label='versicolor')
plt.plot(X_pls[100:150,0],X_pls[100:150,1],'o',label='virginica')
plt.xlim([-3,3])
plt.ylim([-1,1])
plt.title('PLS')
plt.legend(loc='lower right')
plt.show()