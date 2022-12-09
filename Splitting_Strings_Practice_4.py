# Splitting Strings Practice 4
#
# @ author: Kat
# date: 15/11/2022

# Write a program to get a string made of the first 2 and the last 2 words from a given a 
# sentence. If the sentence contains less than 2 words, return instead the empty string.

sentence = "This is a sentence from which to make another sentence."
def get_new_sentence(sentence):
    split_sentence = sentence.split()
    if len(split_sentence) < 2:
        return []
    else:
        list_2 = []
        list_2.append(split_sentence[0])
        list_2.append(split_sentence[1])
        list_2.append(split_sentence[-2])
        list_2.append(split_sentence[-1])
        return list_2
print(get_new_sentence(sentence))
'''
#assertion
Input: sentence = "This is a sentence from which to make another sentence."
Output: ['This', 'is', 'another', 'sentence.']
'''
