##### DICE ROLLING GAME #####
# ASK A USER TO ROLL A DICE (Y/N)
# IF ANY OTHER LETTER, THEN INVALID CHOICE
# IF USER ANSWERED Y, THEN GENERATE 2 RANDOM INTEGERS (x, y)
# IF ANSWERED  N, THEN THANKS FOR PLAYING

import random 

#playing = True # You can remove this variable. It is just for the demonstration.
counter = 0 # To keep track of the dice rolled
# You can write ""while(True)"" instead of the variable.
diceCount = int(input("how many dice do you want to roll?: "))
while (diceCount):
    choice = input("Do you want to roll a dice? Y/N: ").lower()
    if(choice == "y"):
        die1 = random.randint(1,20)
        die2 = random.randint(1,20)
        print(f'({die1}, {die2})')
        counter += 1
        print(f'You have rolled the dice {counter} times...')
        
    elif(choice == "n"):
        print("Thank you for playing!")
        break
    else:
        print("Invalid choice!")