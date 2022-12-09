# List slicing Practice 4
#
# @ author: Kat
# date: 08/11/2022

# A lottery number generator stores 49 balls numbered 1 to 49. 6 Balls are picked one
# at a time from the machine (The balls are not returned) Write a python program that simulates this.

from random import randint
lotto_balls = list(range(1, 50))
print(lotto_balls)
selected_balls = []
counter = 0
balls_left = 49
while counter <= 6:
    ball_index = randint(1, balls_left) - 1
    ball = lotto_balls[ball_index]
    if (ball) not in selected_balls:
        selected_balls.append(ball)
        lotto_balls.pop(ball_index)
    balls_left -= 1
    counter += 1
print("selected_balls are...\n")
print(selected_balls,"\n")
print("Remaining balls are...\n")
print(lotto_balls)
'''
# test case assertion:
since the outputs are randomised, I assert that they show:
A list of balls from 1 to 49 is created
6 balls are selected
The ball numbers are not repeated
The the balls are removed from the initial list
'''
