# 20. To write a Python program to check whether a given number is an Armstrong
# number.

num_str = input("Enter a positive integer: ")

try:
    num = int(num_str)
    order = len(num_str)
    sum_of_powers = 0
    temp_num = num

    while temp_num > 0:
        digit = temp_num % 10
        sum_of_powers += digit ** order
        temp_num //= 10

    if num == sum_of_powers:
        print(f"{num} is an Armstrong number.")
    else:
        print(f"{num} is not an Armstrong number.")

except ValueError:
    print("Invalid input. Please enter a valid positive integer.")
