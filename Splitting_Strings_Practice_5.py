# Splitting Strings Practice 5
#
# @ author: Kat
# date: 15/11/2022

# Write a program that takes a list of words and returns the length of the longest one.

sentence = "This is a sentence containing words of various length."
sentence_split = sentence.split()
def get_longest_word(sentence_split):
    longest_word = ""
    for count in range (0, len(sentence_split)):
        if len(sentence_split[count]) > len(longest_word):
            longest_word = sentence_split[count]
    return longest_word
print(get_longest_word(sentence_split))
'''
#assertion
Input: sentence = "This is a sentence containing words of various length."
Output: containing
'''
