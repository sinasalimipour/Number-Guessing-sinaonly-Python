#v.1

# import random
# userguss = int(input("guss the number between 0 and 2 you got 1 change"))
# pcnumber = random.randint(0, 2)
# if (userguss == pcnumber):
#     print("nice")
# else:print("wrong")


#v.2

import random
pcnumber = random.randint(1,100)
attempts=1
print("Guess your number (1-100)")
print("You have only 9 attempt ")
while(True):
    userguss=int(input("Enter your guess"))
    if(userguss==pcnumber):
        remain = 9 - attempts
        print("you guess correct \nGuess attempt :",attempts,"Remaining:",remain)
        break
    elif(attempts==9):
        print("GAME OVER")
        break
    elif(userguss<pcnumber):
        print("guess greater number")
        count=attempts + 1
    else:
        print("guess lesser number")
        count = attempts + 1






