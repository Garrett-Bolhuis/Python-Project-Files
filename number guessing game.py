# Garrett Bolhuis
# August 24th 2022
# Intro. to Programming CSC 1019
# Envelope Project with Simple while loop

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> CODE BELOW <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<#
choice = ''
import random

the_number = random.randint(1,100)
guess = int

while guess != the_number:
    guess = int(input("Guess a number between 1-100: "))
    if guess > the_number:
        print ("Guess lower. . . \n")
    elif guess < the_number:
        print ("Guess higher. . . \n")
    CPUnum = random.randint (1,100)
    print("Computer guesses: " + str(CPUnum))
    if CPUnum > the_number:
            print("Guess lower. . . \n")
    elif CPUnum < the_number:
        print("Guess higher. . . \n")

                
    if CPUnum == the_number:
        print("The Computer Won! The number was: " + str(the_number) + ".")
    elif guess == the_number:
        print("You Win! The number was: " + str(the_number) + ".")


choice = input("Enter end to exit the game, or rerun to rerun it. ")
while choice == "rerun":
        import random

        the_number = random.randint(1,100)
        guess = int

        while guess != the_number:
            guess = int(input("Guess a number between 1-100: "))
        if guess > the_number:
            print ("Guess lower. . . \n")
        elif guess < the_number:
            print ("Guess higher. . . \n")
        CPUnum = random.randint (1,100)
        print("Computer guesses: " + str(CPUnum))
        if CPUnum > the_number:
                print("Guess lower. . . \n")
        elif CPUnum < the_number:
            print("Guess higher. . . \n")

                
        if CPUnum == the_number:
            print("The Computer Won! The number was: " + str(the_number) + ".")
        elif guess == the_number:
            print("You Win! The number was: " + str(the_number) + ".")
        choice = input("Enter end to exit the game, or rerun to rerun it.")


while choice == 'end':
    print ("goodbye!")
    break
