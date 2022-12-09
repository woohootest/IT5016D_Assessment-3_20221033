# Lists Practice 1
#
# @ author: Kat
# date: 08/11/2022

# Create a stored list with an even number of elements. The list must have
# no fewer than 6 elements. Write a program that returns the first
# half of all the elements  of any list containing an even number of elements.list_1 = [ 34, 123, 5, 77, 59, 2, 4, 42]

list_1 = [ 34, 123, 5, 77, 59, 2, 4, 42]
length = len(list_1)
half = (int(length/2))
print(list_1[0:half])
'''
# assertion 
output = [34, 123, 5, 77]
'''
