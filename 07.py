# 7. To write a Python program to perform basic arithmetic operations using
# operators.

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Addition
sum_result = num1 + num2
print(f"{num1} + {num2} = {sum_result}")

# Subtraction
difference_result = num1 - num2
print(f"{num1} - {num2} = {difference_result}")

# Multiplication
product_result = num1 * num2
print(f"{num1} * {num2} = {product_result}")

# Division
if num2 != 0:
    quotient_result = num1 / num2
    print(f"{num1} / {num2} = {quotient_result}")
else:
    print("Cannot divide by zero!")

# Floor Division (optional, integer division)
if num2 != 0:
    floor_division_result = num1 // num2
    print(f"{num1} // {num2} = {floor_division_result}")

# Modulus (optional, remainder)
if num2 != 0:
    modulus_result = num1 % num2
    print(f"{num1} % {num2} = {modulus_result}")

# Exponentiation (optional)
power_result = num1 ** num2
print(f"{num1} ** {num2} = {power_result}")
