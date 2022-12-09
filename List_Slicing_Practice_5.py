# List slicing Practice 5
#
# @ author: Kat
# date: 08/11/2022

# Write a Python program that uses the following code:
# <span class="codeline">1</span> list_1.append(list_2)</code>
# <code><span class="codeline">2</span> print(list_1)</code>
# <code><span class="codeline">3</span> list_1.extend(list_2)</code>
# <code><span class="codeline">4</span> print(list_1)

import random
list_1 = [1, 56, 123, 87]
list_2 = [34, 75, 13, 89]
list_1.append(list_2)
print(list_1)
list_1.extend(list_2)
print(list_1)
'''
# test case assertion 1
[1, 56, 123, 87, [34, 75, 13, 89]]
# test case assertion 2
[1, 56, 123, 87, [34, 75, 13, 89], 34, 75, 13, 89]
'''
