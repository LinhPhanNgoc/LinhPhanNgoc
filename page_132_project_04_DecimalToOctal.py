"""
Author: Phan Ngoc Linh
Date: 25/09/2021
Problem:
   Octal numbers have a base of eight and the digits 0–7. Write the scripts octalToDecimal.py and decimalToOctal.py,
   which convert numbers between the octal and decimal representations of integers. These scripts use algorithms that
   are similar to those of the binaryToDecimal and decimalToBinary scripts developed in Section 4-3.
Solution:
    ....
"""
d_c_n=int(input('Enter a decimal integer: '))
i = 1
o_c_n = 0
num=""
while (d_c_n != 0):
    rm = d_c_n % 8
    d_c_n //= 8
    o_c_n = o_c_n + rm * i
    i *= 10
    num = str(rm)+num
print('The octal representation is ',o_c_n)