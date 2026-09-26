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