# calculator.py

import math_tools

def main():
    print("Hello, welcome to my calculator!")

    while True:
        try:
            num1 = float(input("Enter the first number: "))
            
            num2 = float(input("Enter the second number: "))
            
            operation = input("Choose an operation (+, -, *, /): ")

            if operation == "+":
                result = math_tools.add(num1, num2)
            elif operation == "-":
                result = math_tools.subtract(num1, num2)
            elif operation == "*":
                result = math_tools.multiply(num1, num2)
            elif operation == "/":
                result = math_tools.divide(num1, num2)
            else:
                print("Invalid operation. Please choose one of (+, -, *, /).")
                continue

            print("Result:", result)

            again = input("Do you want to perform another calculation? (y/n): ").lower()
            if again != 'y':
                print("Goodbye!")
                break

        except ValueError:
            print("Invalid input. Please enter a valid number.")
if __name__ == "__main__":
    main()
