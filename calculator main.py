print("Simple Calculator")

operation = input("Enter operation (1-Addition, 2-Subtraction, 3-Multiply, 4-Division): ")

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

if operation == "1":
    print("Result =", num1 + num2)

elif operation == "2":
    print("Result =", num1 - num2)

elif operation == "3":
    print("Result =", num1 * num2)

elif operation == "4":
    if num2 != 0:
        print("Result =", num1 / num2)
    else:
        print("Error! Division by zero is not allowed.")

else:
    print("Invalid operation!")
