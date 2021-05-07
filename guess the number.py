# guess the number

import random

comp = random.randint(1,50)

while 0 !=  comp :
    user = int(input("Enter a number between 1 to 50 : "))
    print(" ")
    if user != comp :
        if user > comp :
            print("Oh no ! ... To much high number")
            print("==============================================================================")
        if user < comp :
            print("Oh no ! ... To much low number")
            print("==============================================================================")
    if user == comp :
        print("WoW ! you got it !")
        break


            


