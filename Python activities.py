#question 2
import math

userinput = float(input("Enter a decimal number"))

contorad = (math.pi/180)
radians = userinput*contorad
print (radians)
###############################################
#question 3 

userinput = int(input("Enter a decimal number"))

if userinput>0:
    print ("positive")
else
    print("negative")
##################################################
userinput = int(input("Enter a decimal number"))
if userinput>=80:
    print ("A")
elif userinput>70 and userinput<80:
    print("B")
elif userinput>60 and userinput<70:
    print("C")
elif userinput>50 and userinput<60:
    print("D")
elif userinput<50:
    print ("F")
