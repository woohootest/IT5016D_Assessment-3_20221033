# Returning Data From Functions Practice 5
# author: Kat
# date: 11/11/2022

# Write a Python function to find the Max of 3 stored numbers.

print('\nFinding max of three numbers\n')
numlist = []
def get_number_list(numlist):
   ctr = len(numlist)
   while ctr < 3:
      num = float(input('Please enter a number: '))
      if num.is_integer():
          num = int(num)
      numlist.append(num)
      ctr += 1
   return numlist
def get_max(numlist):
   max = numlist[0]
   ctr = 1
   while ctr < len(numlist):
      if numlist[ctr] > max:
         max = numlist[ctr]
      ctr += 1   
   return max
numlist = get_number_list([])
print('\n{0} is the largest of the three numbers: {1}'.format(get_max(numlist), numlist))
'''
#assumptions
Input, 56, 34, 78
Output:
Finding max of three numbers
Please enter a number:  56
Please enter a number: 34
Please enter a number: 78
78 is the largest of the three numbers: [56, 34, 78]
'''
