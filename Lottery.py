# Garrett Bolhuis
# November 7th 2022
# Intro. to Programming CSC 1019
# Powerball Project

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> CODE BELOW <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<#
#Powerball Lottery
import random

import sys

ltgss_list=[]

pbgss_list=[]

loto_list=[]
n=3
for i in range(n):
    loto_list.append(random.randint(1,9))
pwbll_list=[]
n=1
for i in range(n):
    pwbll_list.append(random.randint(1,3))

print(" ")
txt = 'Welcome to the lottery! Try and guess the right numbers to win BIG!'
print(txt.center(80," "))
titleunderline = "*"*len(txt)
print(titleunderline.center(80," "))

lotonum=0

choice = ''
choice = input("\nwould you like to play a lottery game? y/n: ")
if choice == 'y':
    while lotonum<3:
        lotoguess=int(input("please guess your lottery numbers(one at a time): "))
        if 1<=int(lotoguess)<=9:
            for i in range(n):
                ltgss_list.append(lotoguess)
                lotonum +=1
        else:
            print("your number must between 1 and 9")
    pbguess=int(input("now you can guess your powerball number: "))
    pwbllnum=0
    if pwbllnum<1:
        if 1<=int(pbguess)<=3:
            for i in range(n):
                pbgss_list.append(pbguess)
                pwbllnum +=1
        else:
            print("your powerball number must be between 1 and 3")

    print("your chosen numbers are: ")
    print(ltgss_list)
    print("the winninbg numbers are: ")
    print(loto_list)
    print("your powerball number was: ")
    print(pbgss_list)
    print("the winning powerball number was: ")
    print(pwbll_list)

count = 0
for g in ltgss_list:
    for l in loto_list:
        if g == l:
            count += 1
pbcount = 0
for s in pbgss_list:
    for w in pwbll_list:
        if s == w:
            count += 1
    else:
        print("you did not match the powerball number.")

print("you matched: ",count, "lottery numbers.")
if count == 0:
    print("unfortunately you did not win anything")
if count == 1:
    print("congratulations, you matched 1 number. you won $10")
if count == 2:
    print("congratulations, you matched 2 numbers. you won $100")
if count == 3:
    print("WOW! you matched all 3 numbers! you won $1000!")
if pbcount != 0:
    print("Congratulations, you matched the powerball number! you won $10000 for the powerball!")

