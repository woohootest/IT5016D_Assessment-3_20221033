# Returning Data From Functions Practice 3
# author: Kat
# date: 11/11/2022

# Create a simple calculator that just sums 2 numbers entered by the user. Use 
# the function to return the calculated answer to the calling code.

score = 0
print('\nSumming Two Numbers')
def get_sum(num1, num2):
   sum = num1 + num2
   return sum    
num1 = int(input('\nEnter the first number: '))
num2 = int(input('\nEnter the second number: '))
print('\nThe sum of {0} and {1} is {2}'.format(num1, num2, get_sum(num1, 
num2)))    
'''
# assertion
input 4 and 3
output:
Summing Two Numbers
Enter the first number: 4
Enter the second number: 3
The sum of 4 and 3 is 7
'''
