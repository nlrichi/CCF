from wsgiref.validate import InputWrapper


Userinput = input("What would you like to convert?")

def CtoF():
    farenheit = (inputf*9/5)+32
    print(farenheit)

if "celcius to farenheit" in Userinput:
    inputf = int(input("Enter the temperature in celcius"))
    CtoF()