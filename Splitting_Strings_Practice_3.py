# Splitting Strings Practice 3
#
# @ author: Kat
# date: 15/11/2022

# Write a program that randomly jumbles the words in a stored sentence then displays the 
# output. Research and use the Python shuffle function.

from random import shuffle
sentence = "this is a sentence that needs to be shuffled."
#split and shuffle sentence
split_sentence = sentence.split()
shuffle(split_sentence)
#print sentence
print(split_sentence)
'''
#assertions
Input: sentence = "this is a sentence that needs to be shuffled."
Output: ['a', 'shuffled.', 'sentence', 'to', 'this', 'is', 'be', 'needs', 'that']
'''
