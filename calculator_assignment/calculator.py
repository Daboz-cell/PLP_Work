# Two inputs from users
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

# Get operation from user
operation = input("Enter operation (+, -, *, /): ")

# Perfoming operation chosen
if operation == "+":
    result = num1 + num2
    print(num1, "+", num2, "=", result)
elif operation == "-":
    result = num1 - num2
    print(num1, "-", num2, "=", result)
elif operation == "*":
    result = num1 * num2
    print(num1, "*", num2, "=", result)
elif operation == "/":
    if num2 != 0:
        result = num1 / num2
        print(num1, "/", num2, "=", result)
    else:
        print("Cannot divide by zero!")
else:
    print("Invalid operation! Please use +, -, *, or /")
    