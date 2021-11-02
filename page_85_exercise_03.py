"""
Author: Phan Ngoc Linh
Date: 10/09/2021
Problem:
   Write a loop that counts the number of space characters in a string. Recall that the space character is represented as ' '.
Solution:
    ....
"""
x = input()
total = 0
for i in x:
    if i == ' ':
        total += 1
print("Number of space characters in a string =", total)