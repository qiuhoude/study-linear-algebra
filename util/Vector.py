#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class Vector(object):
    """向量"""

    def __init__(self, lst):
        self._values = lst

    def __getitem__(self, index):
        """向量的第index个元素"""
        return self._values[index]

    def __len__(self):
        """获取向量的长度,有多少个元素"""
        return len(self._values)

    def __repr__(self):
        return "Vector({})".format(self._values)

    def __str__(self):
        return "({})".format(self._values)
