#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np

if __name__ == '__main__':
    # 矩阵创建
    A = np.array([[1, 2], [3, 4]])
    print(A)

    # 矩阵的属性
    print(A.shape)
    # 矩阵的转置
    print("A.T = \n", A.T)

    # 获取矩阵的元素
    print(A[1, 1])
    print(A[0])
    # 获取第0列的元素
    print(A[:, 0])
    # 获取第1行的元素 等价于 A[1]
    print(A[1, :])
    print(A[1])

    # 矩阵的基本运算
    B = np.array([[5, 6], [7, 8]])
    print("A + B =\n{}".format(A + B))
    print("A - B =\n{}".format(A - B))
    print("10 * A =\n{}".format(10 * A))
    print("A * 10 =\n{}".format(A * 10))
    print("A * B =\n{}".format(A * B))
    print("A.dot(B) =\n{}".format(A.dot(B)))

    p = np.array([10, 100])
    # 矩阵 的每行 与 向量p 相加
    print("A + p =\n{}".format(A + p))
    # 所有元素 +1
    print("A + 1 =\n{}".format(A + 1))
    print("A.dot(p) =\n{}".format(A.dot(p)))
