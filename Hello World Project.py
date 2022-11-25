# Garrett Bolhuis
# August 24th 2022
# Intro. to Programming CSC 1019
# Hello World Project With While Loop

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> CODE BELOW <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<#
choice = ''

print ("Hello World!")

choice = input ("\n\nEnter end to exit the program, or rerun to rerun the program\n\n")

while choice != 'end':
    print ("Hello World!")
    choice = input ("\n\nEnter end to exit the program, or rerun to rerun the program\n\n")
while choice != 'rerun':
    print ("goodbye")
    break
    
