# Functions with parameters practice 2
#
# @ author: Kat
# date: 11/11/2022

# Write a function that sums all the numbers in a stored list.

print('\nSumming list values')
#initialise list
list = [5, 7, 21, 32, 10]
print('\nList Entries:', list)
#sum values in the list
def sum_items(list):
  sum = 0
  for value in list:
      sum += value
  return sum    
print('\nSum of values in the list: {0}'
      .format(sum_items(list)))
#'''
# test case assertion 1
print("\n\nTest case assertion 1 - output shown below.\n\n")
print("Summing list values\n\n",
      "List Entries: [5, 7, 21, 32, 10]\n\n",
      "Sum of values in the list: 75\n")
#'''
