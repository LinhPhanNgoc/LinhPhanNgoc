"""
Author: Phan Ngoc Linh
Date: 10/09/2021
Problem:
   Explain how to check for an invalid input number and prevent it being used in a program.
   You may assume that the user enters a number.
Solution:
   Ex: Kiểm tra số đầu vào x có lớn hơn số cần so sánh y không ?
    ....
"""
x = float(input("x = "))
y = float(input("y = "))
if x > y:
    print("x la so hop le")
else:
    print("x la so khong hop le")