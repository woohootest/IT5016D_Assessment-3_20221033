# Simple timer in Python
#
# @ author: Kat
# date: 08/11/2022

from datetime import datetime, timedelta
 
duration = 5
 
run = input("enter s to begin...")
 
period = timedelta(seconds=1)
 
next_time = datetime.now() + period
 
counter = 0
while run == 's' and counter < duration:
    if next_time <= datetime.now():
        print("..", counter)
        counter += 1
        # reevaluate the next_time variable
        next_time += period
