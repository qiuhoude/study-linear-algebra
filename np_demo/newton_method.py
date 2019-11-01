#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 牛顿法
# 原来函数
def h(x):
    return x * x - 8 * x + 16


# 1次导
def h1(x):
    return 2 * x - 4


# 2次导
def h2(x):
    return 2


def main():
    xk = 0
    k = 1
    y = 0
    e = 0.0001
    times = 10000

    while k < times:
        y = h(xk)
        a = h1(xk)
        if abs(a) <= e:
            break
        b = h2(xk)
        xk -= a / b
        k += 1
    print("k = ", k)
    print("x = ", xk)
    print("y = ", y)


if __name__ == '__main__':
    main()
