import random
userguss = int(input("guss the number between 0 and 2 you got 1 change"))
pcnumber = random.randint(0, 2)
if (userguss == pcnumber):
    print("nice")
else:print("wrong")
