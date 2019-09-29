#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from .Vector import Vector


class Matrix(object):
    """ 矩阵 """

    def __init__(self, lst2d):
        """ lst2d 是个二维数组"""
        self._value = [row[:] for row in lst2d]

    def __str__(self):
        return "Matrix({})".format(self._value)

    __repr__ = __str__

    @classmethod
    def zero(cls, r, c):
        """返回一个r行c列的零矩阵"""
        # return cls([[0 for col in range(c)] for row in range(r)])
        return cls([[0] * c for _ in range(r)])

    def row_vector(self, index):
        """返回矩阵的第index个行向量"""
        return Vector(self._value[index])

    def col_vector(self, index):
        """返回矩阵的第index个列向量"""
        return Vector([row[index] for row in self._value])

    def __getitem__(self, pos):
        """返回矩阵pos位置的元素"""
        r, c = pos
        return self._value[r][c]

    def shape(self):
        """返回矩阵的形状: (行数， 列数)"""
        return len(self._value), len(self._value[0])

    def row_num(self):
        """返回矩阵的行数"""
        return self.shape()[0]

    def col_num(self):
        """返回矩阵的列数"""
        return self.shape()[1]

    def size(self):
        """返回矩阵的元素个数"""
        r, c = self.shape()
        return r * c

    __len__ = row_num

    def __add__(self, other):
        """矩阵相加 返回结果"""
        assert isinstance(other, Matrix) and self.shape() == other.shape(), \
            "Error in adding. Shape of matrix must be same"

        return Matrix([[a + b for a, b in zip(self.row_vector(i), other.row_vector(i))]
                       for i in range(self.row_num())])

    def __sub__(self, other):
        """返回两个矩阵的减法结果"""
        assert isinstance(other, Matrix) and self.shape() == other.shape(), \
            "Error in subtracting. Shape of matrix must be same"

        return Matrix([[a - b for a, b in zip(self.row_vector(i), other.row_vector(i))]
                       for i in range(self.row_num())])

    def __mul__(self, k):
        """返回矩阵的数量乘结果: self * k"""
        return Matrix([e * k for e in row] for row in self._value)

    def __rmul__(self, k):
        """返回矩阵的数量乘结果: k * self"""
        return self * k

    def __truediv__(self, k):
        """返回数量除法的结果矩阵：self / k"""
        return self * (1 / k)

    def __pos__(self):
        """返回矩阵取正的结果"""
        return 1 * self

    def __neg__(self):
        """返回矩阵取负的结果"""
        return -1 * self

    def dot(self, other):
        """ 矩阵的乘法, 与向量城 与矩阵乘"""
        if isinstance(other, Vector):
            # 矩阵和向量向乘
            # 矩阵列 与 向量长度 数相等
            assert self.col_num() == len(other), \
                "Error in Matrix-Vector Multiplication."
            return Vector([other.dot(self.row_vector(i)) for i in range(self.row_num())])

        if isinstance(other, Matrix):
            # 矩阵和矩阵相乘 self * other; (m*k) * (k*n) = (m*n)
            assert self.col_num() == other.row_num(), \
                "Error in Matrix-Vector Multiplication."
            return Matrix([self.row_vector(i).dot(other.col_vector(j)) for j in range(other.col_num())]
                          for i in range(self.row_num()))
