# 16. To write a Python program to calculate the sum of digits of a given number.

num_input = input("Enter an integer: ")

try:
    num_int = int(num_input)
    original_num = num_int
    sum_of_digits = 0

    # Handle negative numbers by taking the absolute value for digit sum
    if num_int < 0:
        num_int = abs(num_int)

    # If the number is 0, the sum of digits is 0
    if num_int == 0:
        sum_of_digits = 0
    else:
        # Calculate sum of digits
        while num_int > 0:
            digit = num_int % 10
            sum_of_digits += digit
            num_int //= 10

    print(f"The sum of the digits of {original_num} is: {sum_of_digits}")

except ValueError:
    print("Invalid input. Please enter a valid integer.")
