# Functions with parameters practice 3
#
# @ author: Kat
# date: 11/11/2022

# Write a program that prompts the user for a number and then
# outputs the first 4 multiples of that number. You must use a loop in
# your method. Assume that the user enters a valid positive integer

base = int(input("\nPlease enter a number: "))
def display_multiples(base):
  ctr = 1
  num = base
  while ctr <= 4:
    num += base
    ctr += 1
    print(num)
    
display_multiples(base)
#'''
# test case assertion 1
print("\n\nTest case assertion 1 - input and output shown below.\n\n")
print("Please enter a number: 3\n",
      "6\n",
      "9\n",
      "12\n",
      "15")
#'''
