# Serching Strings Practice 4
#
# @ author: Kat
# date: 15/11/2022

# Write a program that returns the index position of the first instance of the text 
# "fight"

fight_club = "The first rule of fight club is: do not talk about fight club."
fight_club_fight_index = fight_club.find("fight")
print("The index position of fight is {0}\n"
      .format(fight_club_fight_index))
'''
Input: fight_club = "The first rule of fight club is: do not talk about fight 
club."
Output:
The index position of fight is 18
'''
