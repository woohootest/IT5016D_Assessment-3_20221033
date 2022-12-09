# Lists Practice 1
#
# @ author: Kat
# date: 08/11/2022

import random
list_2 = [1, 19, 4, 8 ]
item_1 = (random.choice(list_2))
item_2 = (random.choice(list_2))
while item_1 == item_2:
    item_2 = (random.choice(list_2))
print(item_1, " ", item_2)
'''
# assertion 
output = any two items from list_2
'''
