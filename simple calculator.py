def calculator():
    while True:
        # Get user input for the first number
        num1 = float(input("Enter the first number: "))
        
        # Get user input for the second number
        num2 = float(input("Enter the second number: "))
        
        # Get user input for the operation
        operation = input("Enter the operation (add, subtract, multiply, divide): ").strip().lower()
        
        # Perform the operation based on user input
        if operation == 'add':
            result = num1 + num2
            print(f"The result of {num1} + {num2} is: {result}")
        elif operation == 'subtract':
            result = num1 - num2
            print(f"The result of {num1} - {num2} is: {result}")
        elif operation == 'multiply':
            result = num1 * num2
            print(f"The result of {num1} * {num2} is: {result}")
        elif operation == 'divide':
            if num2 != 0:
                result = num1 / num2
                print(f"The result of {num1} / {num2} is: {result}")
            else:
                print("Error: Division by zero is not allowed.")
        else:
            print("Invalid operation. Please choose from add, subtract, multiply, or divide.")
        
        # Ask if the user wants to enter the first number again
        again = input("Would you like to enter a new first number? (yes/no): ").strip().lower()
        if again != 'yes':
            print("Thank you for using the calculator. Goodbye!")
            break

if __name__ == "__main__":
    calculator()