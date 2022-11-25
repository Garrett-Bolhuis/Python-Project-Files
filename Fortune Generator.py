# Garrett Bolhuis
# September 19th 2022
# Intro. to Programming CSC 1019
# Fortune Generator with loop

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> CODE BELOW <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<#
#uses 5 basic random quotes, and a funny one i threw in in a list format and prints one at a time.
choice = ''

import random
quotes = [" Good things come to those who wait.",
          " Patience is a virtue.",
          " The early bird gets the worm.",
          " A wise man once said everything in its own time and place.",
          " Fortune cookies rarely share fortunes.",
          " Your parents didn't allow you to get a fortune cookie."]

print ("--------------------------------------------------------------------------------")
print (random.choice(quotes))
print ("--------------------------------------------------------------------------------")

input ("Please type RERUN to restart the progam, or EXIT to leave the program. ")

while choice != 'EXIT':
    print ("--------------------------------------------------------------------------------")
    print (random.choice(quotes))
    print ("--------------------------------------------------------------------------------")
    choice = input ("Please type RERUN to restart the progam, or EXIT to leave the program. ")

while choice != 'RERUN':
    print ("Goodbye.")
    break
    
