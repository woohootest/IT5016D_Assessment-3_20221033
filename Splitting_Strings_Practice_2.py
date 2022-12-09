# Splitting Strings Practice 2
#
# @ author: Kat
# date: 15/11/2022

# Write a program that takes a single user input of any number of integers separated by 
# commas and then outputs the sum of the numbers.

user_numbers = input("Please enter any number of integers separated by commas.\n\n")
split_input = user_numbers.split(",")

#turn the list of strings into a list of int
int_list = [int(i) for i in split_input]

#calculate sum of items in a list
calc_sum = sum(int_list)
print(calc_sum)
'''
#assertions
Input: 4,6,7,8,2,3,1
Output: 31
'''
