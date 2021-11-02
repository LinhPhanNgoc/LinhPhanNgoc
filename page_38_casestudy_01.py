"""
Author: Phan Ngọc Linh
Date: 02/09/2021
Problem:
    The customer requests a program that computes a person’s income tax.
Solution:
    Compute a person’s income tax.
    1. Significant constants
            tax rate
            standard deduction
            deduction per dependent
    2. The inputs are
            gross income
            number of dependents
    3. Computations:
            taxable income = gross income - the standard
            deduction - a  deduction for each dependent
            income tax = is a fixed percentage of the taxable income
    4. The outputs are
            the income tax

    ....
"""
grossincome = float(input("Enter the gross income :"))
numberofdependents = int(input("Enter the number of dependents :"))
taxableincome = grossincome - 10000 - numberofdependents * 3000
incometax = taxableincome * 0.2
print("The in come tax is $" + str(incometax))