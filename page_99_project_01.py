"""
Author: Phan Ngoc Linh
Date: 10/09/2021
Problem:
   Write a program that accepts the lengths of three sides of a triangle as inputs.
   The program output should indicate whether or not the triangle is an equilateral triangle.
Solution:
    ....
"""
x = float(input("Canh x ="))
y = float(input("Canh y ="))
z = float(input("Canh z ="))
if x == y and y == z:
    print("xyz la tam giac deu")
else:
    print("xyz khong phai la tam giac deu")