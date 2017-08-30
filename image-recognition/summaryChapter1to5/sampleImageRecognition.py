# -*- coding: utf-8 -*-
"""
Created on Fri Aug 11 13:40:00 2017

@author: ishihara
"""

from chainer import datasets
import cv2
import numpy as np
from tqdm import tqdm
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans
from sklearn.svm import LinearSVC

# データの読み込み
train, test = datasets.get_cifar10()
# image = train[i][0]    # trainのi番目の画像
# label = train[i][1]    # trainのi番目のラベル

# サンプリングと記述
## SIFT特徴
def sampling_descriptor(data):
    images_des = [] # 特徴量のリスト
    images_labels = [] # 特徴量を得られた画像のラベル郡
    for i in tqdm(range(len(data))):
        image = data[i][0]
        # 画素が0～1に正規化されているので255倍
        image_rollaxis = np.uint8(np.rollaxis(image, 0, 3) * 255)
        image_rollaxis_gray = cv2.cvtColor(image_rollaxis, cv2.COLOR_BGR2GRAY)
        sift = cv2.xfeatures2d.SIFT_create()
        kp, des = sift.detectAndCompute(image_rollaxis_gray, None)
        if isinstance(des, type(None)):
            continue
        elif len(des)==1:
            continue
        else:
            images_labels.append(data[i][1])
            images_des.append(des)
    return images_des, images_labels

# 線画
'''
from skimage import io
# 元画像
io.imshow(np.uint8(np.rollaxis(train[0][0], 0, 3) * 255))
# 検出点の線画
i=0
kp = sift.detect(image_rollaxis_gray)
out = cv2.drawKeypoints(image_rollaxis_gray, kp, None)
io.imshow(out)
'''

# 統計的特徴抽出
## PCA
def statistical_feature_extract(X):
    images_des_all = [] # 統計的特徴抽出済の特徴量
    for i in range(len(X)):
        pca = PCA(n_components = 2)
        pca.fit(X[i])
        for de in pca.transform(X[i]):
            images_des_all.append(de)
    return images_des_all

# コーディング
## KMeansによるBoVW
def coding(X_ap):
    bovw = np.zeros((len(X_ap), NUM_K))
    for i in tqdm(range(len(X_ap))):
        cluster = kmeans_model.predict(X_ap[i].reshape(1, -1))
        bovw[i, cluster] += 1
    return bovw

# プーリング
## 最大値プーリング
def pooling(C, X):
    V = []
    for i in tqdm(range(len(X))):
        tmp = np.zeros(NUM_K)
        if isinstance(X[i], type(None)):
            V.append(X[i])
        else:
            for j in range(len(X[i])):
                tmp += C[i+j]
            for k in range(len(tmp)):
                if tmp[k] != 0:
                    tmp[k] = 1
            V.append(tmp)
    return V

# サンプリングと記述
X, images_labels = sampling_descriptor(train)

# 統計的特徴抽出
X_ap = statistical_feature_extract(X)

# KMeansモデルの学習
NUM_K = 200 # クラスタ数
kmeans_model = KMeans(n_clusters=NUM_K, max_iter=100).fit(X_ap)

# コーディング
C = coding(X_ap)

# プーリング
V = pooling(C, X)

# 検証データからのVの作成
X_test, images_labels_test = sampling_descriptor(test)
X_ap_test = statistical_feature_extract(X_test)
C_test = coding(X_ap_test)
V_test = pooling(C_test, X_test)

# 分類
## 線形SVM
clf = LinearSVC()
clf.fit(V, images_labels)

# 検証データの分類
label_predict = clf.predict(V_test)

# 精度評価
from sklearn.metrics import confusion_matrix
print(confusion_matrix(images_labels_test, label_predict))
from sklearn.metrics import classification_report
target_names = ['airplane','automobile',
                'bird','cat',
                'deer','dog',
                'frog','horse',
                'ship','truck']
print(classification_report(images_labels_test, label_predict,
                            target_names=target_names))