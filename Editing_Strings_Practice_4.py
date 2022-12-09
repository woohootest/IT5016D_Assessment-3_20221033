# Editing Strings Practice 4
# @ author: Kat
# date: 15/11/2022

# Write a program that executes the following test case assertion:
# "The only thing that scares me is Keyser Soze." becomes 
# => "The*oNly*tHing*That*ScareS*me*Is*keYser*Soze."
# Hint: Every fifth character is capitalised

sentence = "The only thing that scares me is Keyser Soze."
sentence = sentence.replace(" ","*")
sentence = sentence.lower()
new_sentence = ""
for char in range (0,len(sentence)):
    if char % 5 == 0:
        letter = sentence[char]
        letter = letter.upper()
        new_sentence += letter
    else:
        new_sentence += sentence[char]
print(new_sentence)
