'''
Task: Calculator Program
Create a Python program that acts as a basic
calculator. It should prompt the user to
enter two numbers and an operator (+, -, *, /, %),
and then display the result of the operation.
'''

def calculator():
    # Input from user
    num1 = float(input("Enter first number: "))
    operator = input("Enter operator (+, -, *, /, %): ")
    num2 = float(input("Enter second number: "))

    # Perform operation
    if operator == '+':
        result = num1 + num2
    elif operator == '-':
        result = num1 - num2
    elif operator == '*':
        result = num1 * num2
    elif operator == '/':
        if num2 != 0:
            result = num1 / num2
        else:
            return "Error: Division by zero!"
    elif operator == '%':
        if num2 != 0:
            result = num1 % num2
        else:
            return "Error: Modulo by zero!"
    else:
        return "Invalid operator!"

    return f"Result: {result}"

# Run the calculator
print(calculator())

'''
Output:

Enter first number: 8
Enter operator (+, -, *, /, %): -
Enter second number: 9
Result: -1.0
'''