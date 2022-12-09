# If_elif_statement_Letter_of_Alphabet.py
# author: Kat
# date: 03/1/2022

letter = input("Please enter a letter\n")
print("Thank you for entering letter ",letter,"\n")
print("The type of the letter you entered is...",end="")

if letter == ("a" or "e" or "i" or "o" or "u"):
   print("It is a vowel")
elif letter == "y":
    print("Sometimes y is a vowel, and sometimes y is a consonant")
 
else:
    print("It is a consonant")
    
