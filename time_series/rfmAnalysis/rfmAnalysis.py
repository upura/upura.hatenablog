#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pandas as pd
df = pd.read_csv('df.csv')

import numpy as np
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D

df.iloc[:,2] = np.log10(df.iloc[:,2]+1)
df.iloc[:,3] = np.log10(df.iloc[:,3]+1)

CLUSTERS_NUM = 5
pred = KMeans(n_clusters=CLUSTERS_NUM).fit_predict(df.iloc[:,1:4])
df = pd.concat([df, pd.DataFrame(pred)], axis=1)
fig = plt.figure()
ax = Axes3D(fig)
ax.set_xlabel("Recency")
ax.set_ylabel("Log10(Frequency)")
ax.set_zlabel("Log10(Monetary)")
d = []
for cluster_i in range(CLUSTERS_NUM):
    d.append(df[df.iloc[:,4]==cluster_i])
    c = cm.hot(float(cluster_i) / CLUSTERS_NUM)
    ax.plot(d[cluster_i].iloc[:,1], d[cluster_i].iloc[:,2], d[cluster_i].iloc[:,3], "o", color=ｃ, ms=2, mew=0.5)
plt.show()
