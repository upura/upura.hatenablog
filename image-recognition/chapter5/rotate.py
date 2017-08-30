# -*- coding: utf-8 -*-
"""
Created on Wed Jul  5 16:49:47 2017

@author: ishihara
"""

import numpy as np
import matplotlib.pyplot as plt

def J(x):
    return x*(x-4)+5

n = 100
x = np.linspace(0, 5, n)
np.random.seed(seed = 32)
stack = [] # プロット用のリスト

# Graph
plt.xlim(-1, 6)
plt.ylim(-1, 8)
plt.xlabel(r"$\omega$")
plt.ylabel(r"$J(\omega)$", rotation=0)
plt.plot(x, J(x), "b")
plt.show()
