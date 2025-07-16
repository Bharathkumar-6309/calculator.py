def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error: Cannot divide by zero!"
    return x / y

def calculator():
    print("Simple Command-Line Calculator")
    print("Operations: +  -  *  /")
    print("Type 'exit' to quit.\n")

    while True:
        choice = input("Enter operation (+, -, *, /) or 'exit' to quit: ").strip()

        if choice == 'exit':
            print("Exiting calculator. Goodbye!")
            break

        if choice not in ['+', '-', '*', '/']:
            print("Invalid operation. Try again.\n")
            continue

        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))

            if choice == '+':
                result = add(num1, num2)
            elif choice == '-':
                result = subtract(num1, num2)
            elif choice == '*':
                result = multiply(num1, num2)
            elif choice == '/':
                result = divide(num1, num2)

            print("Result:", result, "\n")
        except ValueError:
            print("Invalid input. Please enter numeric values.\n")

# Run the calculator
calculator()
