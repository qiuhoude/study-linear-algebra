#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
from .Vector import Vector


class VectorTest(unittest.TestCase):

    def setUp(self) -> None:
        self.vec1 = Vector([5, 2])
        self.vec2 = Vector([3, 1])
        self.k = 3

    def test_VectorPrint(self):
        print(self.vec1)
        print("len(vec) = {}".format(len(self.vec1)))
        print("vec[0] = {}".format(self.vec1[0]))

    def test_VectorOperation(self):
        print("{} + {} = {}".format(self.vec1, self.vec2, self.vec1 + self.vec2))
        print("{} - {} = {}".format(self.vec1, self.vec2, self.vec1 - self.vec2))
        print("{} * {} = {}".format(self.vec1, self.k, self.vec1 * self.k))
        print("{} * {} = {}".format(self.k, self.vec1, self.k * self.vec1))
        print("+{} = {}".format(self.vec1, +self.vec1))
        print("-{} = {}".format(self.vec1, -self.vec1))

        vec0 = Vector.zero(2)
        print(vec0)
        print("{} + {} = {}".format(self.vec1, vec0, self.vec1 + vec0))

        print("norm({}) = {}".format(self.vec1, self.vec1.norm()))
        print("norm({}) = {}".format(self.vec2, self.vec2.norm()))
        print("norm({}) = {}".format(vec0, vec0.norm()))

        print("normalize({}) is {}".format(self.vec1, self.vec1.normalize()))
        print("normalize({}) is {}".format(self.vec2, self.vec2.normalize()))

        try:
            vec0.normalize()
        except ZeroDivisionError as e:
            print("零向量没有单位向量")

        print("{}.dot{} = {}".format(self.vec1, self.vec2, self.vec1.dot(self.vec2)))
        print("{}.dot{} = {}".format(self.vec1, vec0, self.vec1.dot(vec0)))
        print("{}.dot{} = {}".format(vec0, self.vec1, vec0.dot(self.vec1)))


if __name__ == '__main__':
    unittest.main()
