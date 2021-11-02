"""
Author: Phan Ngoc Linh
Date: 10/09/2021
Problem:
   Write a program that accepts the lengths of three sides of a triangle as inputs.
   The program output should indicate whether or not the triangle is a right triangle.
   Recall from the Pythagorean theorem that in a right triangle, the square of one side equals the sum of the squares of the other two sides.
Solution:
    ....
"""
x = float(input("Canh x ="))
y = float(input("Canh y ="))
z = float(input("Canh z ="))
if x * x == y * y + z * z or y * y == x * x + z * z or z * z == x * x + y * y:
    print("xyz la tam giac vuong")
else:
    print("xyz khong phai la tam giac vuong")