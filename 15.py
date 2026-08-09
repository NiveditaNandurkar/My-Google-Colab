# 15. To write a Python program to count the number of digits in a given integer.

num_input = input("Enter an integer: ")

try:
    # Convert input to an integer
    num_int = int(num_input)

    # Convert the absolute value of the number to a string to count digits
    # This handles negative numbers (e.g., -123 has 3 digits) and zero (0 has 1 digit).
    num_str = str(abs(num_int))

    num_digits = len(num_str)

    print(f"The number {num_int} has {num_digits} digits.")

except ValueError:
    print("Invalid input. Please enter a valid integer.")
