def add(a1, b1):
    print('Result:', a1 + b1)


def subtract(a2, b2):
    print('Result:', a2 - b2)


def multiply(a3, b3):
    print('Result:', a3 * b3)


def divide(a4, b4):
    if b4 != 0:
        print('Result:', a4 / b4)
    else:
        print("cannot divide by 0")


def power(a5, b5):
    if b5 > 0:
        print('Result:', a5 ** b5)
    else:
        print('invalid power')


def squares(a6, b6):
    print("List of Squares")
    for i in range(a6, b6 + 1):
        print(i * i, end=" ")
    print()


##Definitions, this will likely be butchered as i make the HTML work##

 if Option =='1':
        a1=int(input('enter the first number for addition: '))
        b1 = int(input('enter the second number for addition: '))
        add(a1,b1)
    elif Option == '2':
        a2 = int(input('enter the first number for subtraction: '))
        b2 = int(input('enter the second number for subtraction: '))
        subtract(a2, b2)
    elif Option == '3':
        a3 = int(input('enter the first number for multiplication: '))
        b3 = int(input('enter the second number for multiplication: '))
        multiply(a3, b3)
    elif Option == '4':
        a4 = int(input('enter the first number for division: '))
        b4 = int(input('enter the second number for division: '))
        divide(a4, b4)
    elif Option == '5':
        a5 = int(input('enter the first number to be multiplied to the power of the second number: '))
        b5 = int(input('enter the second number: '))
        power(a5, b5)
    elif Option == '6':
        a6 = int(input('enter the lower limit: '))
        b6 = int(input('enter the upper limit: '))
        squares(a6, b6)

##This is how it works, very basic and will 100 percent need to be changed when i make the HTML, was originally made for just being run in python.##

