# Garrett Bolhuis
# October 17th 2022
# Intro. to Programming CSC 1019
# Guess the Word PT. 1

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> CODE BELOW <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
import random

wordstuple = ("meeting", "commitment", "guard", "tablet", "tribe", "writer", "fence", "devote", "government", "random", "python")
word = random.choice(wordstuple)

def restart():
    return rerun_options()

choice =''
guess = ''
def rerun_options():
    txt = 'Word Guessing game'
    new_str = txt.center(80)
    print(new_str)
    ast = '*' * len(word)
    new_ast = ast.center(80)
    print (new_ast)
    choice = input ("Would you like to guess the word? y or n: ")
    if choice == 'n':
            letter = input ("guess a letter in the word: ")
            if letter.lower() in word:
                print ("That letter is in the word")
            else:
                print("that letter is not in the word")
            if choice == 'y':
                guess = input("Guess the word: ")
            if guess == word:
                print("you guessed the word correctly")
            input("press any key and enter to exit: ")
            quit()
    else:
            print(" you did not guess correctly")
            input("press any key and enter to exit: ")
            quit()
while True:
    again=input("Would you like to guess again? y or n: ")
    if again not in {"y","n"}:
        print("please emter a valid input: ")
    elif again == "n":
        print("Goodbye")
        exit()
    elif again == "y":
    return restart()
restart()


