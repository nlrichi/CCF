import random
Userinput = int(input("Guess my number between 1 and 10"))
snum = random.randint(1,10)
print(snum)
if Userinput == snum:
    print("You got it right")
else:
    print("you're nearly there")

