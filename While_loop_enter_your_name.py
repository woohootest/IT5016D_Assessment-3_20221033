# While loop "Enter your name" - a statement that will execute 
#      it's block of code as long as it's condition remains true
# author: Kat
# date: 03/11/2022

name = ""

while len(name) == 0:
    name = input("Enter your name: ")

print("Hello "+name)








# Other variant of the same program

name = None

while not name:
    name = input("Enter your name: ")

print("Hello "+name)
