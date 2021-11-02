"""
Author: Phan Ngoc Linh
Date: 10/09/2021
Problem:
   Write a format operation that builds a string for the float variable amount that has exactly two digits of
   precision and a field width of zero.
Solution:
    ....
"""
num = float(input())
print("%0s" % "%0.2f" % num)