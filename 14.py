# 14. To write a Python program to reverse the digits of a given number.

num_str_input = input("Enter an integer: ")

try:
    # Convert to integer to handle potential leading zeros gracefully if it were a string like '007'
    num_int = int(num_str_input)

    # Preserve the sign
    is_negative = False
    if num_int < 0:
        is_negative = True
        num_str_input = str(abs(num_int))
    else:
        num_str_input = str(num_int)

    # Reverse the string
    reversed_str = num_str_input[::-1]

    # Convert back to integer
    reversed_num = int(reversed_str)

    # Re-apply the sign if it was negative
    if is_negative:
        reversed_num *= -1

    print(f"The original number was: {num_int}")
    print(f"The reversed number is: {reversed_num}")

except ValueError:
    print("Invalid input. Please enter a valid integer.")
