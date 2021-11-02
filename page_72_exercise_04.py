"""
Author: Phan Ngoc Linh
Date: 10/09/2021
Problem:
   Write a loop that outputs the numbers in a list named salaries. The outputs should be formatted in a column
   that is right-justified, with a field width of 12 and a precision of 2.
Solution:
    ....
"""
n = int(input("Số phần tử của list: "))
salaries = []
for i in range(n):
    salaries.append(float(input()))
for i in salaries:
    print("%12s" % "%0.2f" % i)