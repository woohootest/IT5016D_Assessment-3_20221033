# Lists Practice 1
#
# @ author: Kat
# date: 08/11/2022

# Write a program that returns the last quarter of all the elements
# of any list whose total number of elements is a multiple of four.

list_1 = [ 34, 123, 5, 77, 59, 2, 4, 42, 1, 2, 19, 108]
length = len(list_1)
if length % 4 == 0:
    quarter = (int(length/4))
    three_quarters = quarter * 3
    print(list_1[three_quarters: length])
'''
# assertion 
output = [2, 19, 108]
'''
