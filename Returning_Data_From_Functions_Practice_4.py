# Returning Data From Functions Practice 4
# author: Kat
# date: 11/11/2022

# ist_a = ["brown", "grey", "amber"]
# list_b = ["red", "green"]
# list_c = ["purple"]
# Create a program that has a stored list list_d which contains the 3 lists shown 
# above. The program must check lists a to c. For any list that contains less than 3 
# elements, the program must prompt for user input and use the data entered to 
# fill the list.

print('\nColour Lists\n')
list_a = ["brown", "grey", "amber"]
list_b = ["red", "green"]
list_c = ["purple"]
col_list = [list_a, list_b, list_c]
def get_colour(colour_list):
   ctr = len(colour_list)
   while ctr < 3:
      colour = input('Please enter another colour to complete the list {0}:'.format(colour_list))
      ctr += 1
      colour_list.append(colour)
   return colour_list
for clist in col_list:    
  get_colour(clist)
print('\nThe 3-colour lists are:')
for clist in col_list:    
  print(clist)  
'''
# assertion
input: yellow
input: green, blue
output:
Colour Lists
Please enter another colour to complete the list ['red', 'green']: yellow
Please enter another colour to complete the list ['purple']: green
Please enter another colour to complete the list ['purple', 'green']: blue
The 3-colour lists are:
['brown', 'grey', 'amber']
['red', 'green', 'yellow']
['purple', 'green', 'blue']
'''
