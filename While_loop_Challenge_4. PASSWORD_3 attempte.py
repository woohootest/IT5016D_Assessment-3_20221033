# While loop Challenge 4

# Write a password program that prompts the user for a password
# and gives them just 3 attempts. If the user types exit when prompted
# for the password, then the program should terminate.

# author: Kat
# date: 03/11/2022

#correst password: iamtree

number_of_tries = 3

while True:
    answer = input("Enter your password... ")
    if answer == "iamatree":
        print("Welcome!")
# correct answer, so exit loop using break
        break
    else:
        print("Sorry, password is incorrect. Try again!")
        number_of_tries -= 1

#check number of tries and break if none left
    if number_of_tries == 0:
        print("You have run out of goes. Try again later.")
        break

x = input("Please press any key to exit.")
