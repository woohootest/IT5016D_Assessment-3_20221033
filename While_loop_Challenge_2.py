# While loop "Challenge 2"
# author: Kat
# date: 03/11/2022


number = int(input("Please enter a number\n\n"))
counter = 0
total = 0

while counter <= number:
    total = total + counter
    counter += 1

print("\nn = ", number, " sum = ",total,"\n\n")
