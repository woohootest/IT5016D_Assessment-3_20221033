# Scrubbing a stuborn pan
# author: Kat
# date: 03/11/2022

import random

dirty = True #state of the pan
scrub_count = 0 # number of scrubs

while(dirty):
    scrub_count += 1
    print('Scrub the pan: {}'.format(scrub_count))

    print('Rinse & check if the pan is clean.')

    if not random.randint(0,9):
        print('All clean!')
        dirty = False
    else:
        print('Still dirty...')
