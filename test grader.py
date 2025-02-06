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
else:
    print("out of range")