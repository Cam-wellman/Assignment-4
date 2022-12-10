import random

while True:
    outcome = random.randint(0, 1)
    print("Predict if the coin will land on heads or tails (enter the corresponding number)")
    print("1) Heads")
    print("2) Tails")
    print("3) Quit")
    userInput = int(input("Choice: "))
    if userInput == 1:
        if outcome == 0:
            print("Correct it was Heads")
        elif outcome == 1:
            print("Incorrect it was Tails")
    elif userInput == 2:
        if outcome == 0:
            print("Incorrect it was Heads")
        elif outcome == 1:
            print("Correct it was Tails")
    elif userInput == 3:
        print("Quitting")
        break
    elif userInput < 1 or userInput > 3:
        print("Invalid input, Please Try Again")
