# While loop Challenge 4/ SECOND VARIANT

# Write a password program that prompts the user for a password
# and gives them just 3 attempts. If the user types exit when prompted
# for the password, then the program should terminate.

# author: Kat
# date: 03/11/2022

password = (input("Please enter your password\n\n"))
stored_password_variable = "Welcome1234"
counter = 0
correct_flag = False

while counter < 2 and correct_flag == False:
    if password == stored_password_variable:
        print("\nCorrect password\n\n")
        correct_flag = True
    elif password == "Exit":
        print("\nProgramme terminated\n\n")
        correct_flag = True
    else:
        print("\nIncorrect password\n\n")
        password = (input("Please enter a password\n\n"))
        counter += 1 
