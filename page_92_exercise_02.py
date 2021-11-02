"""
Author: Phan Ngoc Linh
Date: 25/08/2021
Problem:
    The factorial of an integer N is the product of the integers between 1 and N, inclusive.
    Write a while loop that computes the factorial of a given integer N.
Solution:
    ....
"""
n = int(input("n = "))
count = 1
lt = 1
while count <= n:
    lt *= count
    count += 1
print("Luy thua =", lt)