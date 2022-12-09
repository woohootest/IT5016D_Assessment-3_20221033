# Splitting Strings Practice 1
#
# @ author: Kat
# date: 15/11/2022

# Write a program that takes a single user input of 3 integers separated by commas and 
# then outputs the average of the numbers.user_numbers = input("Please enter 3 integers separated by commas.\n\n")

user_numbers = input("Please enter 3 integers separated by commas.\n\n")
split_input = user_numbers.split(",")
#turn the list of strings into a list of int
int_list = [int(i) for i in split_input]
#calculate average of items in a list
calc_average = sum(int_list)/len(int_list)
print(calc_average)
'''
#asertions
Input: 3,4,5
Output: 4.0
'''
