# Functions More Practice 3
#
# @ author: Kat
# date: 11/11/2022

# Write a program that maps a list of words into a list of integers representing 
# the lengths of the corresponding words.

list_words = ["tiger", "leopard", "ocelot", "cheetah", "lion"]
list_lengths = []
def word_length(list_words):
    for count in range (0,len(list_words)):
        num = len(list_words[count])
        list_lengths.append(num)
word_length(list_words)
print(list_lengths)
'''
#assertions
list_words = ["tiger", "leopard", "ocelot", "cheetah", "lion"]
list_lengths = [5, 7, 6, 7, 4]
'''
