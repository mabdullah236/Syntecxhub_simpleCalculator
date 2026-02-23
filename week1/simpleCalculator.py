import os

def add(a,b):
    return a+b
def subtract(a,b):
    return a-b
def multiply(a,b):
    return a*b
def division(a,b):
    if b==0:
        print("Error! Cannot divide by Zero")
    return a/b

def getInput(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a numeric value.")
            
def calculator():
    while True:
        print("\n--- Simple Command-Line Calculator ---")
        print("Operations: +, -, *, /")
        print("Type 'c' to clear or 'q' to quit.")
        
        operator = input("Choose an operator (+, -, *, /) or 'q': ").strip().lower()
        
        if operator == 'q':
            print("Exiting. Goodbye!")
            break
        elif operator == 'c':
            print("Calculator cleared.")
            continue    
        if operator not in ['+', '-', '*', '/']:
            print("Invalid operator. Please try again.")
            continue
        
        num1 = getInput("Enter first number: ")
        num2 = getInput("Enter second number: ")

        if operator == '+': 
            result = add(num1, num2)
        elif operator == '-': 
            result = subtract(num1, num2)
        elif operator == '*': 
            result = multiply(num1, num2)
        elif operator == '/': 
            result = division(num1, num2)
            
        print(f"\nResult: {result}")

if __name__ == "__main__":
    calculator()