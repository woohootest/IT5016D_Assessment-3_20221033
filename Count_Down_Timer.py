# Count Down Timer
#
# @ author: Kat
# date: 08/11/2022


import time

running = True
seconds = 10
end = 0

while(running):
    print(seconds)
    time.sleep(1)
    seconds -= 1
    if(seconds <=end):
        running = False
        print(seconds)
print("Happy New Year!")
