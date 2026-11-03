
print("Simple Calculator")

# 1. Prompt for first and second number
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

# 2. Choose operator (+, -, *, /)
op = input("Choose operation (+, -, *, /): ")

# 3. Conditional logic to process calculation and display clear math result
if op == "+":
    print("Result:", num1 + num2)
elif op == "-":
    print("Result:", num1 - num2)
elif op == "*":
    print("Result:", num1 * num2)
elif op == "/":
    # Optional safety check to prevent division by zero
    if num2 == 0:
        print("Error: Division by zero is not allowed.")
    else:
        print("Result:", num1 / num2)
else:
    print("Invalid operation")
