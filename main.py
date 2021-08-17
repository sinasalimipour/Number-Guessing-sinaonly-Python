import random

pcnumber = random(0, 2);
print(pcnumber)
userguss = input("guss the number")

if userguss == pcnumber:
    print("nice")
else:
    print("your worng")
