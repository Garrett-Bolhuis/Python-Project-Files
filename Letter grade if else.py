# Garrett Bolhuis
# August 24th 2022
# Intro. to Programming CSC 1019
# Envelope Project with Simple while loop

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> CODE BELOW <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<#
choice = ''
score = int(input("Please enter a score 1-30: "))

if  score>=27 and score<=30:
    print ("Your grade is an: A")
elif score>=24 and score<27:
    print ("Your grade is a: B")
elif score>=21 and score<24:
    print ("Your gradse is a: C")
elif score>=18 and score<21:
    print ("Your grade is a: D")
elif score>=0 and score<18:
    print ("Your grade is a: F")
else:
    print ("Invalid Score")
choice = input ("enter end to exit or return to restart the program: ")
while choice !='end':
    score = int(input("Please enter a score 1-30: "))

    if  score>=27 and score<=30:
        print ("Your grade is an: A")
    elif score>=24 and score<27:
        print ("Your grade is a: B")
    elif score>=21 and score<24:
        print ("Your gradse is a: C")
    elif score>=18 and score<21:
        print ("Your grade is a: D")
    elif score>=0 and score<18:
        print ("Your grade is a: F")
    else:
        print ("Invalid Score")
    choice = input ("enter end to exit or return to restart the program: ")
while choice != 'return':
    print ("Goodbye")
    break
