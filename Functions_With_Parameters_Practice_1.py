# Functions with parameters practice 1
#
# @ author: Kat
# date: 11/11/2022

# Write a function that calculates and displays the number of upper and lowercase letters in a 
# stored string.

print('\nCounting Characters')
word = input("Please enter a string: ")
def count_characters(word):
  upper_case, lower_case, other_characters = 0, 0, 0
  for key, value in enumerate(word):
    if value.isupper(): 
      upper_case += 1
    elif value.islower():
      lower_case += 1
    else:
      other_characters += 1    
  print('\nCharacter Counts:'
        '\nUpper case letters: {0}'
        '\nLower case letters: {1}'
        '\nOther characters: {2}'
        .format(upper_case, lower_case, other_characters))
count_characters(word)
#'''
# test case assertion 1
print("\n\nTest case assertion 1 - output shown below.\n\n")
print("Counting Characters:\n",
      "Please enter a string: Jeff Williams\n\n",
      "Character Counts:\n\n",
      "Upper case letters: 2\n",
      "Lower case letters: 10\n",
      "Other characters: 1")
#'''
