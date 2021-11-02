"""
Author: Phan Ngoc Linh
Date: 25/08/2021
Problem:
   Construct truth tables for the following Boolean expressions:
   a. not (A or B)
   b. not A and not B
Solution:
a.
    A    B    A or B    not (A or B)
    T    T      T           F
    T    F      T           F
    F    T      T           F
    F    F      F           T
b.
    A    B    not A    not B    not A and not B
    T    T      F        F            F
    T    F      F        T            F
    F    T      T        F            F
    F    F      T        T            T
    ....
"""