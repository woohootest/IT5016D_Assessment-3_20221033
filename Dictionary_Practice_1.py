# Dictionary Practice 1
#
# @ author: Kat
# date: 08/11/2022

# Write a program that removes entries from
# a stored dictionary where the length of the key is 2.

#initialise dictionary 1
city_dict1 = {'AKL':'Auckland', 'CC':'Christchurch', 'DUD':'Dunedin', 'WLG':'Wellington', 
'AUK':'Auckland'}
print('\nCity Dictionary 1:',city_dict1)
indexes_to_delete = []
print('\nDeleting entries from dictionary where key length is 2')
for val in city_dict1.keys():
    if len(val)==2:
        indexes_to_delete.append(val)
for items in indexes_to_delete:
    del(city_dict1[items])
print('\nCity Dictionary 1:', city_dict1)
'''
# assertion: output should be missing the Christchurch entry
'''
