"""
Author: Phan Ngoc Linh
Date: 02/09/2021
Problem:
   Five Star Retro Video rents VHS tapes and DVDs to the same connoisseurs who like to buy LP record albums.
   The store rents new videos for $3.00 a night, and oldies for $2.00 a night.
   Write a program that the clerks at Five Star Retro Video can use to calculate the total charge for a customer’s video rentals.
   The program should prompt the user for the number of each type of video and output the total cost.
Solution:
    ....
"""
count_new_video = int(input("Nhập số lượng video mới: "))
count_old_video = int(input("Nhập số lượng video cũ: "))
days = int(input("Nhập số đêm thuê: "))
newvideo = 3
oldvideo = 2
total = days * ((count_old_video * oldvideo) + (count_new_video * newvideo))
print("Number of new video = ", count_new_video)
print("Number of old video = ", count_old_video)
print("Total = ", total , "$")

