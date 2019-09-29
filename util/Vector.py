#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math
from ._globals import EPSILON


class Vector(object):
    """向量"""

    def __init__(self, lst):
        assert isinstance(lst, list), \
            "lst type must be list"
        self._values = lst
        self._name = "vec"

    def __getitem__(self, index):
        """向量的第index个元素"""
        return self._values[index]

    def __iter__(self):
        """迭代器"""
        return self._values.__iter__()

    def __len__(self):
        """获取向量的长度,有多少个元素"""
        return len(self._values)

    def __repr__(self):
        return "Vector({})".format(self._values)

    def __str__(self):
        return "({})".format(", ".join(str(e) for e in self))

    def __add__(self, other):
        """向量的加法, 并返回结果"""
        assert isinstance(other, Vector) and len(self) == len(other), \
            "Error Length of vectors must be same."
        return Vector([a + b for a, b in zip(self, other)])

    def __sub__(self, other):
        """向量的减法, 并返回结果"""
        assert isinstance(other, Vector) and len(self) == len(other), \
            "Error Length of vectors must be same."
        return Vector([a - b for a, b in zip(self, other._values)])

    def __mul__(self, k):
        """ 向量乘以标量 k 返回结果: self * k向量"""
        return Vector([k * a for a in self])

    def __rmul__(self, k):
        """ 向量乘以标量 k 返回结果: k * self 向量"""
        return self * k

    def __pos__(self):
        """ 返回向量取正结果 """
        return 1 * self

    def __neg__(self):
        """ 返回向量取负的结果 """
        return -1 * self

    @classmethod
    def zero(cls, dim):
        assert isinstance(dim, int), \
            "dim type must be int "
        """ 返回一个 dim 纬度的零向量"""
        return cls([0] * dim)

    def norm(self):
        """返回向量的模"""
        return math.sqrt(sum(a * a for a in self))

    def normalize(self):
        """ 返回单位向量 unit vector"""
        norm = self.norm()
        if norm < EPSILON:
            raise ZeroDivisionError("Normalize error! norm is zero.")
        # 有了除法之后可以 向量直接除于标量
        return Vector([e for e in self / norm])
        # return Vector([e / norm for e in self])

    def __truediv__(self, k):
        """ 返回除法结果 向量除标量,self / k """
        return self * (1 / k)

    def dot(self, other):
        """向量的点乘, 返回点乘后的标量"""
        assert isinstance(other, Vector) and len(self) == len(other), \
            "Error in subtracting. Length of vectors must be same."
        return sum(a * b for a, b in zip(self, other))
