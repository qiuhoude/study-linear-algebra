#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
from .Matrix import Matrix
from .Vector import Vector


class MatrixTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.matrix1 = Matrix([[1, 2], [3, 4]])
        self.matrix2 = Matrix([[5, 6], [7, 8]])

    def test_MatrixPrint(self):
        matrix = Matrix([[1, 2], [3, 4]])

        print(matrix)
        print("matrix.shape = {}".format(matrix.shape()))
        print("matrix.size = {}".format(matrix.size()))
        print("len(matrix) = {}".format(len(matrix)))
        print("matrix[0][0] = {}".format(matrix[0, 0]))

    def test_MatrixOperation(self):
        print("add: {}".format(self.matrix1 + self.matrix2))
        print("subtract: {}".format(self.matrix1 - self.matrix2))
        print("{} * scalar-mul: {}".format(2, 2 * self.matrix1))
        print("scalar-mul * {}: {}".format(2, self.matrix1 * 2))
        print("zero_2_3: {}".format(Matrix.zero(2, 3)))

    def test_MatrixDot(self):
        #  矩阵与向量 相乘
        T = Matrix([[1.5, 0], [0, 2]])
        p = Vector([5, 3])
        print("T.dot(p) = {}".format(T.dot(p)))

        # 矩阵 与 矩阵相乘
        P = Matrix([[0, 4, 5], [0, 0, 3]])
        print("T.dot(P) = {}".format(T.dot(P)))

        print("A.dot(B) = {}".format(self.matrix1.dot(self.matrix2)))
        print("B.dot(A) = {}".format(self.matrix2.dot(self.matrix1)))


if __name__ == '__main__':
    unittest.main()
