""" 5. To write a Python program to determine whether a number is positive, negative,
or zero."""

num = float(input("Enter a number: "))

if num > 0:
    print(f"The number {num} is positive.")
elif num < 0:
    print(f"The number {num} is negative.")
else:
    print(f"The number {num} is zero.")
