import math

def calculator():
    print("Welcome to the Calculator")
    print("==============================")
    print("Select the operation")
    print("==============================")
    print("1: Basic Arthimetic Operations (Addition , Subtraction, Multiplication, Division)")
    print("2: Advanced Mathematical functions (Power, Root, Modulus, Factorial)")
    print("3: Trigonometric & Inverse Trignometric Functions")
    print("4: Memory Functions")
    print("5: Exit")
    print("==============================")
    while True:
        choice = int(input("Enter your mode from 1-5: "))
        if choice == 1:
            basic()

        elif choice == 2:
            advance()

        elif choice == 3:
            trigonometric()

        elif choice == 4:
            memory()

        elif choice == 5:
            print("==============================")
            print("Exiting the Calculator...")
            print("Thank you for using Calculator")
            print("==============================")
            break

        else:
            print("Invalid choice. Enter your choice from 1-5")

def basic():
    print("==============================")
    print("You selected Basic operations")
    print("==============================")
    print("1: Addition")
    print("2: Subtraction")
    print("3: Multiplication")
    print("4: Division")
    print("5: Exit")
    print("==============================")
    choice = int(input("Enter your mode from 1-5: "))
    if choice == 1:
        result = add()
        print("Result: ", result)

    elif choice == 2:
        result = subtract()
        print("Result: ", result)

    elif choice == 3:
        result = multiply()
        print("Result: ", result)

    elif choice == 4:
        result = divide()
        print("Result: ", result)

    elif choice == 5:
        print("==============================")
        print("Exiting the Basic Operations...")
        print("==============================")

    else:
        print("Invalid choice. Enter your choice from 1-5")
    
def add():
    num1 = float(input("Enter first number : "))
    num2 = float(input("Enter second number : "))
    return num1 + num2

def subtract():
    num1 = float(input("Enter first number : "))
    num2 = float(input("Enter second number : "))
    return num1 - num2

def multiply():
    num1 = float(input("Enter first number : "))
    num2 = float(input("Enter second number : "))
    return num1 * num2

def divide():
    num1 = float(input("Enter first number : "))
    num2 = float(input("Enter second number : "))
    if num2 != 0:
        return num1 / num2
    else:
        return "Cannot divide by Zero"

def advance():
    print("==============================")
    print("You selected Advance operations")
    print("==============================")
    print("1: Power")
    print("2: Square Root")
    print("3: Modulus")
    print("4: Factorial")
    print("5: Exit")
    print("==============================")
    choice = int(input("Enter your mode from 1-5: "))
    if choice == 1:
        result = power()
        print("Result: ", result)

    elif choice == 2:
        result = root()
        print("Result: ", result)

    elif choice == 3:
        result = modulus()
        print("Result: ", result)

    elif choice == 4:
        result = factorial()
        print("Result: ", result)

    elif choice == 5:
        print("==============================")
        print("Exiting the Advance Operations...")
        print("==============================")

    else:
        print("Invalid choice. Enter your choice from 1-5")
    
def power():
    base = float(input("Enter the Base: "))
    exponent = float(input("Enter the Exponent: "))
    return math.pow(base, exponent)

def root():
    num = float(input("Enter number: "))
    if num > 0:
        return math.sqrt(num)
    else:
        return "Cannot find Square Root of Negative numbers"
    
def modulus():
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    if num1 > num2:
        if num2 > 0:
            return num1 % num2
        else:
            return "Cannot find modulus of zero or negative in denominator"
    else:
        return "Cannot find modulus when denominator is greater than nominator"
            
def factorial():
    num = int(input("Enter the number: "))
    if num > 0:
        return math.factorial(num)
    else:
        return "Factorial of negative numbers and zero does not exists"

def trigonometric():
    print("==============================")
    print("You selected Trigonometric operations")
    print("==============================")
    print("1: Sine")
    print("2: Cosine")
    print("3: Tangent")
    print("4: Sine Inverse")
    print("5: Cosine Inverse")
    print("6: Tangent Inverse")
    print("7: Exit")
    print("==============================")
    choice = int(input("Enter your mode from 1-7: "))
    if choice == 1:
        result = sin()
        print("Result: ", result)

    elif choice == 2:
        result = cos()
        print("Result: ", result)

    elif choice == 3:
        result = tan()
        print("Result: ", result)

    elif choice == 4:
        result = sin_in()
        print("Result: ", result)

    elif choice == 5:
        result = cos_in()
        print("Result: ", result)

    elif choice == 6:
        result = tan_in()
        print("Result: ", result)

    elif choice == 7:
        print("==============================")
        print("Exiting the Trigonometric Operations...")
        print("==============================")

    else:
        print("Invalid choice. Enter your choice from 1-7")

def sin():
    angle = float(input("Enter the angle in degree: "))
    return math.sin(math.radians(angle))

def cos():
    angle = float(input("Enter the angle in degree: "))
    return math.cos(math.radians(angle))

def tan():
    angle = float(input("Enter the angle in degree: "))
    return math.tan(math.radians(angle))

def sin_in():
    value = float(input("Enter the value: "))
    if value < 1 or value > -1:       
        return math.degrees(math.asin(value))
    else:
        return "Enter the value ranging from -1 to 1"

def cos_in():
    value = float(input("Enter the value: "))
    if value < 1 or value > -1:       
        return math.degrees(math.acos(value))
    else:
        return "Enter the value ranging from -1 to 1"

def tan_in():
    value = float(input("Enter the value: "))
    return math.degrees(math.atan(value))

def memory():
    print("==============================")
    print("You selected Memory operations")
    print("==============================")
    print("1: Store value")
    print("2: Recall value")
    print("3: Clear memory")
    print("4: Exit")
    print("==============================")
    choice = int(input("Enter your mode from 1-4: "))
    if choice == 1:
        result = store()

    elif choice == 2:
        result = recall()

    elif choice == 3:
        result = clear()

    elif choice == 5:
        print("==============================")
        print("Exiting the Memory Operations...")
        print("==============================")

    else:
        print("Invalid choice. Enter your choice from 1-4")

def store():
    global memory_store
    memory_store = float(input("Enter value to store: "))  
    print("Value stored successfully")

def recall():
    if memory_store is not None:
        print("Stored Value: ", memory_store)
    else:
        print("No Value Stored")

def clear():
    global memory_store
    memory_store = None
    print("Memory Cleared")


calculator()