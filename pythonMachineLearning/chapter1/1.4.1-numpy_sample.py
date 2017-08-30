# -*- coding: utf-8 -*-
import numpy as np

# (3,)の配列
x = np.array([1,2,3])
print(x)

# (2,3)の配列
A = np.array([[1,2,3],[4,5,6]])
print(A)

# 配列の形
print(A.shape)
# データ型
print(A.dtype)

# 1行2列の要素にアクセス
print(A[1,2])
# 0行目の要素にアクセス
print(A[0])

# スライシング
print(A[:,0:1])
print(A[:,0])

# 転置
print(A.T)
print(A.T.shape)

# 3次元配列の場合
B = np.array([[[1,2],[3,4],[5,6]]])
print(B)
print(B.T)
print(B.shape)
print(B.T.shape)

# (2,3)->(1,6)に変形
print(A.reshape(1,6))
A.reshape(1,7) # 要素数不一致でエラー

# 配列の連結
B = np.ones((2,3))
print(np.r_[A,B]) # 行
print(np.c_[A,B]) # 列

#四則演算
print(A + B)
print(A - B)
print(A * B)
print(B / A)

C = np.array([[1,2,3]])
print(C)
print(A + C) # Cの次元が拡張される

c = np.array([1,2,3])
print(c) # (3,)->(1,3)->(2,3)と拡張される
print(A + c)