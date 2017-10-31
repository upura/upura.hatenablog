#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt

beta = [0.1, 1.0, 10]

def sigmoid(x):
    return 1.0 / (1.0 + np.exp(-x))

def swish(beta, x):
    return x * sigmoid(beta * x)

n = 1000
x = np.linspace(-5, 3, n)
y = [[] for i in range(len(beta))]

plt.title("Swish")

for i in range(len(beta)):
    y[i] = swish(beta[i], x)
    plt.plot(x, y[i], label = "β=" + str(beta[i]))

plt.legend(loc="upper left")
plt.show()