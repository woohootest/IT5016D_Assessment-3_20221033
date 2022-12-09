# Count Up Timer
#
# @ author: Kat
# date: 08/11/2022


import time

running = True
seconds = 0
end = 10

while(running):
    print(seconds)
    time.sleep(1)
    seconds += 1
    if(seconds >=end):
        running = False
        print(seconds)
print("Done!")
