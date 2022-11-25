# Garrett Bolhuis
# September 9th 2022
# Intro. to Programming CSC 1019
# Tip Calculator

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> CODE BELOW <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<#
print ("___________._____________    ___________________ _______  _____________________    ________________________ __________   ")
print ("\__    ___/|   \______   \  /  _____/\_   _____/ \      \ \_   _____/\______   \  /  _  \__    ___/\_____  \\______   \  ")
print ("  |    |   |   ||     ___/ /   \  ___ |    __)_  /   |   \ |    __)_  |       _/ /  /_\  \|    |    /   |   \|       _/  ")
print ("  |    |   |   ||    |     \    \_\  \|        \/    |    \|        \ |    |   \/    |    \    |   /    |    \    |   \  ")
print ("  |____|   |___||____|      \______  /_______  /\____|__  /_______  / |____|_  /\____|__  /____|   \_______  /____|_  /  ")
print ("                                   \/        \/         \/        \/         \/         \/                 \/       \/   ")
server = str(input("Please enter the servers name? "))
bill = float(input("enter the total bill: "))
tip = float(input("enter the tip given (%): "))
tippercent = tip/100
tipnumber = bill*tippercent
checktotal = bill+tipnumber
print('Server:', server)
print('Bill:', bill)
print('Tip Percent:', tip)
print('Tip Total:', tipnumber)
print('Bill Total:', checktotal)
    
