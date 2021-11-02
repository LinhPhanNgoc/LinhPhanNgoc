"""
Author: Phan Ngoc Linh
Date: 02/09/2021
Problem:
   An employee’s total weekly pay equals the hourly wage multiplied by the total number of regular hours plus any
   overtime pay. Overtime pay equals the total overtime hours multiplied by 1.5 times the hourly wage.
   Write a program that takes as inputs the hourly wage, total regular hours, and total overtime hours and
   displays an employee’s total weekly pay.
Solution:
    ....
"""
wage = float(input("Enter the wage : $"))
h = float(input("Enter the hours :"))
ot = float(input("Enter the overtime hours :"))
total =wage * h + wage * ot * 1.5
print("The  total weekly pay is", total, "$")