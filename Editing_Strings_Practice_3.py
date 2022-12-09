# Editing Strings Practice 3
# @ author: Kat
# date: 15/11/2022

# Write a program that randomly picks a character from a stored string and 
# then places that character between every character in the string

from random import randint
sentence = "I love tigers"
index = randint(0, len(sentence))
letter_at_index = sentence[index]
print("Inserting a random character into a string...\n{0}".format(letter_at_index.join(sentence)),"\n")
'''
#assertions
Input: sentence = "I love tigers"
Output:
Inserting a random character into a string...
Ie eleoeveee eteiegeeeres
'''
