import time

word = 'bottles'
# This uses a for loop to iterate over several print lines
for num_beer in range(99, 0,-1):
    print(num_beer, word, "of beer on the wall!")
    time.sleep(2.5)
    print(num_beer, word, " of beer!")
    time.sleep(2)
    print("take one down!")
    time.sleep(1)
    print("pass it around!")
    time.sleep(1)
    # The loop reaches a condition where depending on the iteration
    #It'll switch to either the if or else.
    if(num_beer == 1):
        print("No more bottles of beer on the wall...")
        time.sleep(2)
    else:
        new_beer = num_beer - 1
        if new_beer == 1:
            word = "bottle"
            print(new_beer, word, "of beer on the wall..")
            time.sleep(2)
    print()
