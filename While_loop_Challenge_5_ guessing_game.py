# Guessing game

# Write a guessing game where the user has to guess a stored secret number.
#     After every guess, the program tells the user whether their
#     number was too large or too small. At the end, the number of tries needed should
#     be printed. It counts only as one try if they input the same number multiple times consecutively.

# author: Kat
# date: 03/11/2022

import random

print("\tWelcome to Guessing Game!")
print("\nI'm thinking of a number between 1 and 100")
print("Try to guess it as few attampts as possible.\n")

#set the initial value

the_number = random.randint(1, 100)
guess = int(input("Take a guess: "))
tries = 1

# guessing loop
while guess != the_number:
    if guess > the_number:
        print("Lower...")
    else:
        print("Higher...")
            
    guess = int(input("Take a guess: "))
    tries += 1

print("You guessed it!  The number was", the_number)
print("And it only took you", tries, "tries!\n")
  
input("\n\nPress the enter key to exit.")

