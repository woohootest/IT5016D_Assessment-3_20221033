# Dictionary Practice 2
#
# @ author: Kat
# date: 08/11/2022

# Write a program that sums all the values of a stored dictionary.
# Assume that all the values are integers.

print('\nSumming dictionary values')
#initialise dictionary 1 
city_dict1 = {'AKL':1495, 'CHC':389.7, 'DUD':118.5, 'WLG':405}
print('\nCity Dictionary 1:',city_dict1)
#sum values in the dictionary
sum = 0
for popn in city_dict1.values():
    sum += popn
print('\nTotal population in the major cities (in thousands):')
print(sum)
'''
# assertion output should be:
Total population in the major cities (in thousands):
2408.2
'''
