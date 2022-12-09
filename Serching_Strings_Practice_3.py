# Serching Strings Practice 3
#
# @ author: Kat
# date: 15/11/2022

# Write a program that gets user input and determines whether the text 
# matches the start of the string.

fight_club = "The first rule of fight club is: do not talk about fight club."
user_text = input("Please enter some case sensitive text.\n\n")
print("Does this string start with the given text?....{0}\n"
      .format(fight_club.startswith(user_text)))
'''
#Assertions
Input: the
Output: Does this string start with the given text?....False
#assertion 2
Input: The
Output: Does this string start with the given text?....True
'''
