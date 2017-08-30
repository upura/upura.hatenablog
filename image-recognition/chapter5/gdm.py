# -*- coding: utf-8 -*-
"""
Created on Wed Jul  5 09:59:38 2017
"""

import numpy as np
import matplotlib.pyplot as plt

def J(x):
    return x*(x-4)+5

def diffJ(x):
    h = 1e-4
    return (J(x+h) - J(x)) / h

n = 100
x = np.linspace(0, 5, n)
np.random.seed(seed = 32)
stack = [] # プロット用のリスト

'''
# Graph
plt.xlim(-1, 6)
plt.ylim(-1, 8)
plt.xlabel(r"$\omega$")
plt.ylabel(r"$J(\omega)$")
plt.plot(x, J(x), "b")
plt.show()
'''

# 初期値
omega = np.random.rand()*5
# ステップ幅
eta = 0.01

for i in range(100000):
    # プロット用のリスト
    stack.append(omega)
    # パラメータ更新
    omega = omega-eta*diffJ(omega)
        # 収束判定
    if eta*diffJ(omega)<=0.0001:
        break

# 結果表示
plt.xlabel(r"number of steps")
plt.ylabel(r"$\omega$")
plt.plot(stack, "r")
plt.show()