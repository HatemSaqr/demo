from pickle import TRUE


print("Calculator")


def add(y,x):
    return y + x

def mines (y,x):
    return y - x

def mult (y,x):
    return y * x

def g (y,x):
    return y / x

calculator = True

while calculator:
    
    print("   ")
    print("type +,-,*,/,exit")
    choies = input("choise: ")
    if choies == "exit":
        calculator = False
        break
    
    
    print("   ")
    
    num1 = float(input("enter first number:"))
    
    print("   ")
    
    num2 = float(input("enter sacend number:"))
    
    
    if choies == "+":
        print(add(num1,num2))
   
    elif choies == "-":
        print(mines(num1,num2))

    elif choies == "*":
        print(mult(num1,num2))

    elif choies == "/":
        print(g(num1,num2))

    else:
        print("error")

