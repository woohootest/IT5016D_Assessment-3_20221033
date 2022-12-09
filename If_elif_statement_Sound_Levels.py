# If_elif_statement_Sound_Levels.py
# author: Kat
# date: 03/1/2022

print("Welcome to Sound Level Identifier")
sound_level = int(input("Please enter sound level using numbers between 40dB and 130dB\n"))
print("Thank you for the sound level entered is...",sound_level,"\n")
print("The sound level is...", end="")


if sound_level > 130:
    print("Sound is not defined")
elif sound_level == 130:
    print("Jackhammer")
elif sound_level > 106 < 130:
    print("Between petrol lawnmover and jackhammer")
elif sound_level == 106:
    print("Petrol lawnmover")
elif sound_level > 70 < 106:
    print("Between alarm clock and petrol lawnmower")
elif sound_level == 70:
    print("Alarm clock")
elif sound_level > 40 < 70:
    print("Between quite room and alarm clock")
elif sound_level == 40:
   print("Quiet room")
elif sound_level < 40:
   print("Sound is not defined")
else:
    print("Sound is not defined")
