# Garrett Bolhuis
# November 7th 2022
# Intro. to Programming CSC 1019
# Powerball Project

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> CODE BELOW <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<#
#Powerball Lottery
import random
import sys

lg1=[]
lg2=[]
lg3=[]
pbg=[]

lotoreward1=["$1"]

lotoreward2=["$100"]

lotoreward3=["$1000"]

powerballreward=["$1000000"]

loto_list=[]
n=3
for i in range(n):
    loto_list.append(random.randint(1,9))

pwbllt=[]
n=1
for i in range(n):
    pwbll.append(random.randint(1,3))

choice = ''

choice = input("would you like to play a lottery game? y/n: ")
while choice == 'y':
    lg1=input("please guess your first lottery number: ")
    if 0 > int(lg1) > 9:
        print("your number must be between 1 and 9.")
    else:
        lg2=input("please guess your second lottery number: ")
    if 0 > int(lg2) > 9:
        print("your number must be between 1 and 9.")
    else:
        lg3=input("please guess your last lottery number: ")
    if 0 > int(lg3) > 9:
        print("your number must be between 1 and 9.")
    else:
        pbg=input("now you may guess your powerball number: ")
    if 0 > int(pbg) > 3:
        print("your number must be between 1 and 3.")
    else:
        print("lottery guesses: "lg1+" "+lg2+" "+lg3+"powerball guess: "+pbg)
        print(loto_list)
        print(pwbll)

