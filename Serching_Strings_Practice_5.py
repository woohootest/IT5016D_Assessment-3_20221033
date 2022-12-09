# Serching Strings Practice 4
#
# @ author: Kat
# date: 15/11/2022

# Write a program that contains a stored pin as a string. The program must 
# evaluate the string and say whether it contains numbers only

pin = "2580"
if pin.isdigit() == True:
    print("This pin is made up only of digits\n\n")
else:
    print("This pin contains characters other than digits\n\n")
'''
#assertions
Input: pin = "25.0"
Output: This pin contains characters other than digits
Input: pin = "25r0"
Output: This pin contains characters other than digits
Input: pin = "2580"
Output: This pin is made up only of digits
'''
