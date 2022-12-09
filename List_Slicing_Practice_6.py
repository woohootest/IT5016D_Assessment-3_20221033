# List slicing Practice 6
#
# @ author: Kat
# date: 08/11/2022

# result = False
# for x in list1:
# for y in list@:
# if x ==y:
# result = True
# return result

# The code shown is part of the program
# that takes 2 lists and returns True if they have at least one
# common member. Use the code to write the complete program. Use 2 stored liststo test your work.

list_1 = [1,56,123,87]
list_2 = [34, 84, 76, 93]
result = False
for x in list_1:
    for y in list_2:
        if x == y:
            result = True       
print(result)
'''
# assertion
list_1 = [1,56,123,87], list_2 = [34, 84, 76, 93], output = False
list_1 = [1,56,123,87], list_2 = [34, 84, 56, 93], output = True
'''
