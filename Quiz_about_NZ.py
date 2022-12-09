# True/False quiz: Boolean values True/Fales
# Author: Kat
# Date 03/11/2022



from datetime import datetime

print("Kia Ora! Welcome to the quiz! Answer True or False to the following questions\n")
score = 0
start_time = datetime.today()

str_one = input("30%of the country is a national reserve.\n")
answer_one = "True"
answer_two = "False"

if  answer_one == 'True':
   score = score + 1
   print("\nThat is correst.Your score is ", score ,"\n\n")
else:
   print("\nThat is incorrest. Your score is ", score ,"\n\n")
