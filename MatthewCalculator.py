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
            