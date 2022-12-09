# Returning Data From Functions Practice 1
# author: Kat
# date: 11/11/2022

# Write a function that takes a stored list of integers and returns the values that 
# are less than or equal to the list average.

print('\nDisplaying values less than the average in a list\n')
numlist = [23, 45, 62, 33, 76, 13, 24, 66]
def get_average(numlist):
  summation = 0
  for num in numlist:
    summation += num
  return summation / len(numlist)
def get_lower_nums(average, numlist):
  lower_nums = []
  for num in numlist:
    if num < average:
       lower_nums.append(num)
  return lower_nums
average = get_average(numlist)
lower_nums = get_lower_nums(average, numlist)
print('Average: {0}\nValues less than the average: {1} '.format(average, 
lower_nums))
'''
#assertions
Displaying values less than the average in a list
Average: 42.75
Values less than the average: [23, 33, 13, 24]
'''
