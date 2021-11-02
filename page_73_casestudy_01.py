"""
Author: Phan Ngoc Linh
Date: 10/09/2021
Problem:
   Write a program that computes an investment report
Solution:
   The four principal parts of the program perform the following tasks:
       1. Receive the user’s inputs and initialize data.
       2. Display the table’s header.
       3. Compute the results for each year, and display them as a row in the table.
       4. Display the totals.
    ....
"""
startBalance = float(input("Enter the investment amount: "))
years = int(input("Enter the number of years: "))
rate = int(input("Enter the rate as a %: "))
rate = rate / 100
print("%4s%18s%10s%16s" % ("Year", "Starting balance",     "Interest", "Ending balance"))
for year in range(1, years + 1):
    interest = startBalance * rate
    endBalance = startBalance + interest
    print("%4d%18.2f%10.2f%16.2f" % (year, startBalance, interest, endBalance))
    startBalance = endBalance
    interest += interest
