"""
Author: Phan Ngoc Linh
Date: 10/09/2021
Problem:
   Write a code segment that displays the values of the integers x, y, and z on a single line, such that each value is right-justified with a field width of 6.
Solution:
    ....
"""
x = int(input())
y = int(input())
z = int(input())
print("%6s" % x, "%6s" % y, "%6s" % z)