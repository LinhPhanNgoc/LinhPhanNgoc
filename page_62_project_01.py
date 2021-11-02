"""
Author: Phan Ngoc Linh
Date: 02/09/2021
Problem:
   The tax calculator program of the case study outputs a floating-point number that might show more than two
   digits of precision. Use the round function to modify the program to display at most two digits of precision
   in the output number.
Solution:
   Human beings, desktop computers, cellphones
    ....
"""
grossincome = float(input("Enter the gross income :"))
numberofdependents = int(input("Enter the number of dependents :"))
taxableincome = grossincome - 10000 - numberofdependents * 3000
incometax = taxableincome * 0.2
print("The in come tax is $" + str(round(incometax, 2)))
