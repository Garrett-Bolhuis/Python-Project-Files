# Garrett Bolhuis
# August 24th 2022
# Intro. to Programming CSC 1019
# Envelope Project with Simple while loop

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> CODE BELOW <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<#   
email_list = ['yeet@gmail.com', 'imtired@emai.com', 'email@email.com'] 

email = ""
choice = ""

def restart():
    return rerun_options()

def rerun_options():
    print (" Options: \n 1 -Show Email Adresses\n 2 -Add An Email Address\n 3 -Remove An Email Address\n 4 -Exit")
    choice = input(" Please enter the number corresponding to the opperation you wish to complete: ")
# choice 1 lists the emails.
    if choice == "1":
            print ("The emails are: ")
            for i in range(len(email_list)):
                print(str(i+1) + ")",email_list[i])
#choice 2 allows you to add an email to the list and shows the revised list.
    if choice == "2":
                dot = True
                at_sign = True
                extension = True
                not_full = True      
                email = input("Enter an email address: ")
                index = email.find(".")
                if "." not in email:
                    print("There is no dot in the email")
                    dot = False       
                if "@" not in email:
                    print("There is no @ in the email")
                    at_sign = False       
                if index != len(email) - 4:
                    print("There is not a .xxx at the end of the email")
                    extension = False   
                if len(email_list) >10:
                    print("The list is full")
                    not_full = False      
                if dot == True and at_sign == True and extension == True and not_full == True:    
                    email_list.append(email)
                    print(email + " Was added to the list. \nThe new email list is: ")
                    for i in range(len(email_list)):
                        print(str(i+1) + ")", email_list[i])
#choice 3 allows trhe user to remove an email from the list and shows the revised list.
    if choice == "3":
                for i in range(len(email_list)):
                    print(str(i+1) + ")", email_list[i])
                num = int(input("Enter a number to remove the associated email: "))
                while num <= 0 and num > len(email_list):
                    print("Invalid Opperation")
                email_list.remove(email_list[num-1])
                print("Email number " + str(num) + " has been removed.\nThe new email list is: ")
                for i in range(len(email_list)):
                    print(str(i+1) + ")", email_list[i])
#choice 4 will print goodbye and prompt the user to close the program.
    if choice == "4":
                print("Goodbye.")
                exit()
#This will appear when one of the above choice functions is complete and recalls the program back to the top to rerun the program.         
    while True:
        again=input("Would you like to use one of the functions again? y or n: ")
        if again not in {"y","n"}:
            print("Please enter a correct response: ")
        elif again == "n":
            print("Goodbye")
            exit()
        elif again == "y":
            return restart()
restart()

