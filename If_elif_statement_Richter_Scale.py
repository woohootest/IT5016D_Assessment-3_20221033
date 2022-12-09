# If_elif_statement_Richter_Scale.py
# author: Kat
# date: 03/1/2022

print("Welcome to Richter Scale")
magnitude_scale = float(input("Please enter a magnitude scale between 2.0 and 10.0\n"))
print("Thank you for the magnitude scale entered is ",magnitude_scale,"\n")
print("The Richter Scale for this magnitude is...", end="")

if magnitude_scale > 10.0:
   print("The Richter Scale for magnitudude entered is Meteoric")
elif magnitude_scale > 8.0:
    print("Great")
elif magnitude_scale > 7.0:
    print("Major")
elif magnitude_scale > 6.0:
    print("Strong")
elif magnitude_scale > 5.0:
    print("Moderate")
elif magnitude_scale > 4.0:
    print("Light")
elif magnitude_scale > 3.0:
    print("Minor")
elif magnitude_scale > 2.0:
    print("Very minor")
elif magnitude_scale < 2.0:
    print("Micro")
else:
    print("Meteroic")
    
