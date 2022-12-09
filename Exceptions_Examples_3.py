# Exceptions Examples 3
#
# @ author: Kat
# date: 15/11/2022

def divide_numbers(number_1, number_2):
    try:
        return number_1 / number_2
    except ZeroDivisionError:
        return "Error, cannot divide by zero."
    except TypeError as e:
        message = "Error, an operand is the wrong type...\n" \
               "Or as Python would say...\n{0}".format(e)
        return message
 
print(divide_numbers(3,"Four"))

'''
Process finished with exit code 0
'''
