"""
Author: Phan Ngoc Linh
Date: 10/09/2021
Problem:
   The German mathematician Gottfried Leibniz developed the following method to approximate the value of
   π: π/4 5 1 ] 1/3 1 1/5 ] 1/7 1 . . . Write a program that allows the user to specify the number of iterations
   used in this approximation and that displays the resulting value.
Solution:
    ....
"""
num = int(input("Nhập vào số lần = "))
pi_four = 0
counter = 1
for i in range(1, num + 1):
    if(i % 2 != 0):
        pi_four = pi_four + 1 / counter
    else:
        pi_four = pi_four - 1 / counter
    counter += 2
pi = pi_four * 4
print("pi =", pi)