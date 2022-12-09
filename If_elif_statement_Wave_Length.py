# If_elif_statement_Wave_Length.py
# author: Kat
# Date: 03/11/2022

print("Welcome to wavelength colour convertre\n")
wave_length = int(input("Please enter an integer wavelength between 380 and 750\n"))
print("Thank you, the wavelength that you entered in nanometers is ",wave_length,"\n")
print("The colour for this wavelength is...", end="")

if wave_length > 750:
    print("The wavelength entered is higher than the visible spectrum! This is infrared.")
elif wave_length >= 620:
    print("Red")
elif wave_length >= 590:
    print("Orange")
elif wave_length >= 570:
    print("Yellow")
elif wave_length >= 495:
    print("Green")
elif wave_length >= 450:
    print("Blue")
elif wave_length >= 380:
    print("Violet")
else:
    print("Infoterminate, :-(, the number entered is outside the visible spectrum!")
