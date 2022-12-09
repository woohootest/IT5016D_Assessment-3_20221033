# Exceptions Examples 2
#
# @ author: Kat
# date: 15/11/2022

def divide_numbers(number_1, number_2):
    try:
        return number_1 / number_2
    except ZeroDivisionError:
        return "Error, cannot divide by zero."
 
print(divide_numbers(3,"asdf"))

'''
Process finished with exit code 1
'''
