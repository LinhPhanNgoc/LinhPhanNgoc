"""
Author: Phan Ngoc Linh
Date: 10/09/2021
Problem:
   Write a program that computes square roots.
Solution:
   1. The input is a number.
   2. The outputs are the program's estimate of the square root using Newton's method of successive approximations, and Python's own estimate using math.sqrt.
    ....
"""
import math
x = float(input("Enter a positive number: "))
tolerance = 0.000001
estimate = 1.0
while True:
    estimate = (estimate + x / estimate) / 2
    difference = abs(x - estimate ** 2)
    if difference <= tolerance:
        break
print("The program's estimate:", estimate)
print("Python's estimate:     ", math.sqrt(x))

