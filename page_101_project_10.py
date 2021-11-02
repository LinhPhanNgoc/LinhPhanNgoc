"""
Author: Phan Ngoc Linh
Date: 25/08/2021
Problem:
   The credit plan at TidBit Computer Store specifies a 10% down payment and an annual interest rate of 12%.
   Monthly payments are 5% of the listed purchase price, minus the down payment. Write a program that takes
   the purchase price as input. The program should display a table, with appropriate headers, of a payment
   schedule for the lifetime of the loan. Each row of the table should contain the following items:
   • the month number (beginning with 1)
   • the current total balance owed
   • the interest owed for that month
   • the amount of principal owed for that month
   • the payment for that month
   • the balance remaining after payment
   The amount of interest for a month is equal to balance * rate / 12.
   The amount of principal for a month is equal to the monthly payment minus the interest owed.
Solution:
    ....
"""
price = float(input('Enter the purchase price: '))
month_number = 1
int_rate = 0.12
down_payment = price * 0.1
monthly_payment = (price-down_payment) * 0.05
current_balance = price - down_payment
print('{:<15s} {:<20s} {:<20s} {:<20s} {:<20s} {:<20s}'.format('Month','Starting Balance','Interest to Pay', 'Principal to Pay','Payment','Ending Balance'))
while current_balance > 0:
    if current_balance < monthly_payment:
        int_amt = 0
        principal = current_balance
        payment = current_balance
        ending_balance = 0
    else:
        int_amt = current_balance * (int_rate/12)
        principal = monthly_payment-int_amt
        payment = int_amt + principal
        ending_balance = current_balance - principal
    print('{:<15d} {:<20.2f} {:<20.2f} {:<20.2f} {:<20.2f} {:<20.2f}'.format(month_number, current_balance, int_amt,principal, payment, ending_balance))
    current_balance = ending_balance
    month_number += 1