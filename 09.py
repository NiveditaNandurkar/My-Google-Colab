# 9. To write a Python program to calculate the factorial of a number using a loop.

num = int(input("Enter a non-negative integer: "))

factorial = 1

# check if the number is negative, zero or positive
if num < 0:
    print("Factorial does not exist for negative numbers.")
elif num == 0:
    print("The factorial of 0 is 1.")
else:
    for i in range(1, num + 1):
        factorial = factorial * i
    print(f"The factorial of {num} is {factorial}.")
