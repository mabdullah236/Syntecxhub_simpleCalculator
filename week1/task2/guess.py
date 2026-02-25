import random

def generateRandNum(level):
    if level == 'e':
        return random.randint(1, 10)
    elif level == 'm':
        return random.randint(1, 50)
    elif level == 'h':
        return random.randint(1, 100)

def getLevel():
    while True:
        level = input("Enter level (e/m/h): ").strip().lower()
        if level in ['e', 'm', 'h']:
            return level
        else:
            print("Invalid choice! Please choose e, m, or h.")

def getNumberInput(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Please choose number only.")

def guess():
    print("\n ----Welcome in Guessing number game----")
    
    while True:  
        
        print("\nEnter 'e' for easy level.")
        print("Enter 'm' for medium level.")
        print("Enter 'h' for hard level")

        level = getLevel()
        randomNum = generateRandNum(level)

        if level == 'e':
            maxRange = 10
        elif level == 'm':
            maxRange = 50
        else:
            maxRange = 100

        print(f"\nComputer chose a number between 1-{maxRange}")
        attempts = 0

        while True:
            userInput = getNumberInput("Enter your Number: ")

            if userInput < 1 or userInput > maxRange:
                print(f"Please enter number between 1 and {maxRange}")
                continue

            attempts += 1

            if userInput == randomNum:
                print(f"You got it in {attempts} attempts!")
                break
            elif userInput > randomNum:
                print("Choose smaller number please.")
            else:
                print("Choose larger number please.")

        replay = input("\nDo you want to play again? (y/n): ").lower()
        if replay != 'y':
            print("Thanks for playing!")
            break

if __name__ == "__main__":
    guess()
