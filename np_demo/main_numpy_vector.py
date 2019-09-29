#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np

if __name__ == "__main__":
    print(np.__version__)

    # np.array 创建向量
    vec = np.array([1, 2, 3])
    print(vec)
    # np中不只能存数字 不能添加其他类型的元素
    # vec[0] = "abc"

    # 零向量
    print(np.zeros(5))
    # 5 个 1
    print(np.ones(5))
    # 5 个 666
    print(np.full(5, 666))

    print("size : ", vec.size)
    print("len  : ", len(vec))
    print("vec[0] : ", vec[0])
    print("vec[-1] : ", vec[-1])
    print("vec[0: 2] : ", vec[0: 2])
    print("type(vec[0: 2]) : ", type(vec[0: 2]))

    # np.array的基本运算
    vec2 = np.array([4, 5, 6])
    print("{} + {} = {}".format(vec, vec2, vec + vec2))
    print("{} - {} = {}".format(vec, vec2, vec - vec2))
    print("{} * {} = {}".format(2, vec, 2 * vec))
    print("{} * {} = {}".format(vec, vec2, vec * vec2))
    print("{}.dot({}) = {}".format(vec, vec2, vec.dot(vec2)))

    print("{} norm {}".format(vec, np.linalg.norm(vec)))
    # normalize 求单位向量
    normalize = vec / np.linalg.norm(vec)
    print("{} normalize {}".format(vec, normalize))
    print("norma(normalize) = {}".format(np.linalg.norm(normalize)))
