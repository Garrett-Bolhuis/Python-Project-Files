# Garrett Bolhuis
# August 24th 2022
# Intro. to Programming CSC 1019
# Envelope Project with Simple while loop

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> CODE BELOW <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<#
print ("random coin toss of 100 coins:")
import random
coin_heads, coin_tails, timesflipped = 0, 0, 0
timesflipped = 0
while timesflipped < 100:
    coin_flips = random.randrange(2)
    if coin_flips == 0:
        coin_heads = coin_heads+1
    else:
        coin_tails = coin_tails+1
    timesflipped+= 1
print ("out of 100 flips: " + str(coin_heads) + " were heads " + str(coin_tails) + " were tails ")
input ("press enter to exit: ")
