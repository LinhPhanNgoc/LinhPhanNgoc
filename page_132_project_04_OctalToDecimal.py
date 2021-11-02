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
o_t_n=int(input('Enter a string of octal digits: '))
i = 1
dc = 0
while (o_t_n != 0):
    rmd = o_t_n % 10
    o_t_n //= 10
    dc += rmd * i
    i *= 8
print('The integer value is ',dc)