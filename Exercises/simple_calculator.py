num1 = float(input("First number: "))
num2 = float(input("Second number: "))

arithmetic = input("Operation (add, subtract, multiply, divide): ")

if arithmetic == "add":
    print(f"Addition: {num1 + num2}")
elif arithmetic == "subtract":
    print(f"Subtraction: {num1 - num2}")
elif arithmetic == "multiply":
    print(f"Multiplication: {num1 * num2}")
elif arithmetic == "divide":
    print(f"Division: {num1 / num2}")
else:
    print("Invalid operation")
    