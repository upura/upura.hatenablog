#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt

def sigmoid(x):
    return 1.0 / (1.0 + np.exp(-x))

def swish(x):
    return x * sigmoid(x)

n = 1000
x = np.linspace(-5, 3, n)
y = swish(x)

plt.title("Swish")
plt.plot(x, y, "r")
plt.show()
