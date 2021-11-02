"""
Author: Phan Ngoc Linh
Date: 02/09/2021
Problem:
   The kinetic energy of a moving object is given by the formula KE = 1/2*m*v**2
   where m is the object’s mass and v is its velocity.
   Modify the program you created in Project 5 so that it prints the object’s kinetic energy as well as its momentum.

Solution:
   Human beings, desktop computers, cellphones
    ....
"""
mass = float(input("Enter the mass = "))
velocity = float(input("Enter the velocity = "))
momentum = mass * velocity
kineticEnergy = 1/2 * mass * (velocity ** 2)
print("Momentum = ",momentum )
print("Kinetic Energy = ",kineticEnergy)