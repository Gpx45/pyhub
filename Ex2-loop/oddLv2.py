from datetime import datetime
from time import sleep
from random import randint

odds = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29,
        31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55, 57, 59]

for i in range(5):
    right_this_minute = datetime.today().minute
    if right_this_minute in odds:
        print('This minute seems a little odd.')
    else:
        print('Not an odd minute.')
    sleep(randint(0,60)) # -> This is a Function
    #That is set to pause(sleep) for random amounts of time.
 # Function from time module to pause the screen for x amount
# Or it can also be done this way.
    # wait_timer = random.randint(0, 5)
    # time.sleep(wait_timer)

    # There are oher ways to make it but it depends on what you want
    # to do.
