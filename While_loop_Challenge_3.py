# While loop challenge 3
# Write a program that prints multiples of p from 10 until the value
# of q (inclusive) Examples: the user enters: p = 4 and Q = 29 Answer: 12, 16, 20, 24, 28,

# author: Kat
# date: 03/11/2022

is_running = True

p = int(input("Please enter an increment\n\n"))
q = int(input("Please enter an ending number\n\n"))

counter = 10
number = 10

starting_number = (10 % p) + 10

while counter < q:
    print(starting_number ,end=", ")
    starting_number = starting_number + p
    counter += p
             
