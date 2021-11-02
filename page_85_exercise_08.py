"""
Author: Phan Ngoc Linh
Date: 10/09/2021
Problem:
   The variables x and y refer to numbers. Write a code segment that prompts the user for an arithmetic operator
   and prints the value obtained by applying that operator to x and y.
Solution:
    ....
"""
x=float(input("Enter x value: "))
y=float(input("Enter y value: "))
operator = input("Enter operator: ")
if operator == '+' :
    print("x + y =", x + y )
elif operator == '-' :
    print("x - y =", x - y )
elif operator == '*' :
    print("x * y =", x * y)
elif operator == '/' :
    print("x / y =", x / y)
else:
    print("Error")



