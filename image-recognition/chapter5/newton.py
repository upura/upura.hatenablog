# -*- coding: utf-8 -*-
"""
Created on Wed Jul  5 15:10:36 2017

@author: ishihara
"""

import numpy as np

def objectiveFunction(x):
    return 3*x[0]**2 + 2*x[0]*x[1] + x[1]**2

def gradientHessian(x):
    g = [6*x[0] + 2*x[1], 2*x[0] + 2*x[1]]
    h = [[6, 2],
         [2, 2]]
    return g, h

def newtonLineSearch(function, ghFunction, x, tolerance):
    residual = 1e12
    fOld = 1e12
    alpha = 1
    while residual > tolerance:
        f = function(x)
        g, h = ghFunction(x)
        delta = -np.linalg.solve(h, g)
        x = x + alpha*delta
        residual = abs(f-fOld)
        fOld = f
    return x, f

x0 = [10.0, 10.0]
x, f = newtonLineSearch(objectiveFunction, gradientHessian, x0, 1e-12)
print(x, f)