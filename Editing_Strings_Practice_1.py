# Editing Strings Practice 1
# @ author: Kat
# date: 15/11/2022

# Write a program that accepts a user input sentence and then replaces all the 
# spaces with dashes before displaying the output to screen.

sentence = input("Please enter a sentence\n\n")
print("Replacing part of a string...\n{0}".format(sentence.replace(" ", "-")),"\n")
'''
#assertion
Input: I love tigers
Output:
Replacing part of a string...
I-love-tigers 
'''
