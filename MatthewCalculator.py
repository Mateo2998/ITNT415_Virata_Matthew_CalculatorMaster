def addition(n):
    userValue = 0
    x = n
    programAdd = True
    while programAdd == True:
        userValue = input("Input Value to Add: ")
        if userValue == "q" or userValue == "Q":
            programAdd = False
            return x
        else:
            try:
                x = x + float(userValue)
            except:
                print("Invalid input. Please enter a number.")

def subtraction(n):
    userValue = 0
    x = n
    programSubtract = True
    while programSubtract == True:
        userValue = input("Input Value to Subtract: ")
        if userValue == "q" or userValue == "Q":
            programSubtract = False
            return x
        else:
            try:
                x = x - float(userValue)
            except:
                print("Invalid input. Please enter a number.")

def division(n):
    userValue = 0
    x = n
    programDivide = True

    while programDivide == True:
        userValue = input("Input Value to Divide: ")

        if userValue == "q" or userValue == "Q":
            programDivide = False
            return x
        else:
            try:
                if x == 0:
                    x = float(userValue)
                elif float(userValue) == 0:
                    print("Cannot divide by zero.")
                else:
                    x = x / float(userValue)
            except:
                print("Invalid input. Please enter a number.")

programCalculator = True
n = 0
while programCalculator == True:
    print("Welcome to Matthew's Calculator!\nSelect operations:")
    print("Addition = +\nSubtraction = -\nDivision = /\nMultiplication = *\nClear value = Clear\nOr type Exit to quit")

    
    print("Your current value is", n)

    userChoice = input("\nWhat's your option?")

    if userChoice == "Exit" or userChoice == "exit":
        programCalculator = False

    else:
        if userChoice == "+":
            print("You selected Addition!\nType q if done")
            n = addition(n)
        elif userChoice == "-":
            print("You selected Subtraction!\nType q if done")
            n = subtraction(n)
        elif userChoice == "/":
            print("You selected Division!\nType q if done")
            n = division(n)
        elif userChoice == "*":
            print("You selected Multiplication!\nType q if done")
            n = multiplication(n)
        elif userChoice == "clear" or userChoice == "Clear":
            n = 0
        else:
            print("Invalid option. Select a different one.")