# -*- coding: utf-8 -*-
"""
Created on Sun Jan 21 21:33:34 2018

"""

import numpy as np
from sklearn import svm, datasets
import matplotlib.pyplot as plt
from itertools import product

if __name__ == '__main__':
    iris = datasets.load_iris()
    #特徴量は最初の2つ, クラスラベルも最初の2つを使う
    X = iris.data[:100, :2]
    #特徴量にノイズを加える
    E = np.random.uniform(0, 1.0, size=np.shape(X))
    X += E
    y = iris.target[:100]
    #meshのステップサイズ
    h = 0.02
    #コストパラメータ
    Cs = [2 ** -5, 2 ** 5]
    #RBFカーネルのパラメータ
    gammas = [2 ** -15, 2 ** -2, 2** -1, 
              2 ** 1, 2 ** 2, 2 ** 3]

    svms = [svm.SVC(C=C, gamma=gamma).fit(X, y) for C, gamma in product(Cs, gammas)]
    titles = ["C: small, gamma: 2**-15", "C: small, gamma: 2**-2",
              "C: small, gamma: 2**-1", "C: small, gamma: 2**1",
              "C: small, gamma: 2**2", "C: small, gamma: 2**3",
              "C: large, gamma: 2**-15", "C: large, gamma: 2**-2",
              "C: large, gamma: 2**-1", "C: large, gamma: 2**1",
              "C: large, gamma: 2**2", "C: large, gamma: 2**3"]
    x_min, x_max = X[:, 0].min() - 1, X[:, 0].max() + 1
    y_min, y_max = X[:, 1].min() - 1, X[:, 1].max() + 1
    xx, yy = np.meshgrid(np.arange(x_min, x_max, h), np.arange(y_min, y_max, h))

    for i, clf in enumerate(svms):
        plt.subplot(4, 3, i + 1)
        plt.subplots_adjust(wspace=0.4, hspace=1)
        Z = clf.predict(np.c_[xx.ravel(), yy.ravel()])
        Z = Z.reshape(xx.shape)
        plt.contourf(xx, yy, Z, cmap=plt.cm.Paired, alpha=0.8)
        plt.scatter(X[:, 0], X[:, 1], c=y, cmap=plt.cm.Paired)
        plt.xlabel("Sepal length", fontsize=8)
        plt.ylabel("Sepal width", fontsize=8)
        plt.xlim(xx.min(), xx.max())
        plt.ylim(yy.min(), yy.max())
        plt.xticks(())
        plt.yticks(())
        plt.title(titles[i], fontsize=8)
    plt.show()