#!/usr/bin/python

#Ask the user for a number. Depending on whether the number is even or odd, print out an appropriate message to the user.
#
#Hint: how does an even / odd number react differently when divided by 2?
#
#Extras:
#
#If the number is a multiple of 4, print out a different message.
#Ask the user for two numbers: one number to check (call it num) and one number to divide by (check). If check divides evenly into num, tell that to the user. If not, print a different appropriate message.
#================================================================================================
print("Please enter a number to get us started with checking if it's equal or unequal")
number = int(raw_input())

mod = number % 2
if mod > 0:
	print("You've chosen an unequal number")
else:
	print("you've chosen a equal number")