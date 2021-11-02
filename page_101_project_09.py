"""
Author: Phan Ngoc Linh
Date: 10/09/2021
Problem:
   Write a program that receives a series of numbers from the user and allows the user to press the enter
   key to indicate that he or she is finished providing inputs. After the user presses the enter key,
   the program should print the sum of the numbers and their average.
Solution:
    ....
"""
n = int(input("Nhap so phan tu cua list = "))
lst = []
tong = 0
for i in range(1, n + 1):
    lst.append(int(input()))
for v in lst:
    tong += v
print("Tong =", tong)
print("Trung binh=", tong / n)
