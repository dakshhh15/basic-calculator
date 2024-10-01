#defining functions

def add(a, b):
    return int(a) + int(b)

def sub(a, b):
    return int(a)- int(b)

def mul(a, b):
    return int(a) * int(b)

def div(a, b):
    return int(a) / int(b)

print("Here is the list of operations: \n A. Addition \n B. Subtraction \n C. Multiplication \n D. Division \n E. Exit")

choice = input("Enter the operation you wish to execute: ")
if choice == "a" or choice == "A":
    print("Addition: ")
    a = input("Enter first number: ")
    b = input("Enter second number: ")
    print(add(a,b))
elif choice == "b" or choice == "B":
    print("Subtraction: ")
    a = input("Enter first number: ")
    b = input("Enter second number: ")
    print(sub(a,b))
elif choice == "c" or choice == "C":
    print("Multiplication: ")
    a = input("Enter first number: ")
    b = input("Enter second number: ")
    print(mul(a,b))
elif choice == "d" or choice == "D":
    print("Division: ")
    a = input("Enter first number: ")
    b = input("Enter second number: ")
    print(div(a,b))
elif choice == "e" or choice == "E":
    print("Exiting calculator.")
    quit()
else:
    print("Enter one of the given operations.")
    pass