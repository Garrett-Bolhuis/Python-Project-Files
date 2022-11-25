# Garrett Bolhuis
# eventually 2022
# Intro. to Programming CSC 1019
# Guess the Word PT. 2

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> CODE BELOW <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
import random

wordstuple = ("meeting", "commitment", "guard", "tablet", "tribe", "writer", "fence", "devote", "government", "random", "python")
word = random.choice(wordstuple)
response = " "
loop = "t"
letter = ""

txt = 'Word Guessing game'
print(txt.center(80," "))
obscured = "*"*len(word) 
print (obscured.center(80," "))
while loop == "t":
        response = input ("Would you like to guess the word? y or n: ")
        if response == "n":
                letter = input ("guess a letter in the word: ")
                if letter.lower() in word.lower():
                    print ("That letter is in the word")
                    new_word = ""
                    for i in range(len(word)):
                        if word[i].lower()==letter.lower():
                            new_word += word[i]
                        else:
                            new_word += obscured[i]
                    obscured = new_word
                    print(obscured.center(80," "))
                    if obscured == word:
                        print("Congraqtulations! You revealed the word!")
                        quit()
                else:
                    print("sorry, but that letter is not in the word.")
                    print(obscured.center(80," "))
        else:
            guess = input("Guess the word: ")
            if guess == word:
                print("you guessed the word correctly")
                input("press any key and enter to exit: ")
                quit()
            else:
                print(" you did not guess correctly")



