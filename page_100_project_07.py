"""
Author: Phan Ngoc Linh
Date: 25/08/2021
Problem:
   Teachers in most school districts are paid on a schedule that provides a salary based on their number of
   years of teaching experience. For example, a beginning teacher in the Lexington School District might be
   paid $30,000 the first year. For each year of experience after this first year, up to 10 years, the teacher
   receives a 2% increase over the preceding value. Write a program that displays a salary schedule, in tabular
   format, for teachers in a school district. The inputs are the starting salary, the percentage increase, and
   the number of years in the schedule. Each row in the schedule should contain the year number and the salary
   for that year.
Solution:
    ....
"""
luong = float(input("Nhập vào lương khơi điểm: "))
years = int(input("Nhập vào số năm làm việc: "))
rate = int(input("Nhập vào %: "))
rate = rate / 100
print("%4s%18s" % ("Year", "Wage"))
totalluong = 0
for year in range(1, years + 1):
    interest = luong * rate
    totalluong = luong + interest
    print("%4d%18.2f" % (year, luong))
    luong = totalluong
    interest += interest