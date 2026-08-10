# 10. To write a Python program to find the sum of the first N natural numbers.

n = int(input("Enter a positive integer (N): "))
if n < 1:
    print("Please enter a positive integer.")
else:
    sum_natural = 0
    for i in range(1, n + 1):
        sum_natural += i
    print(f"The sum of the first {n} natural numbers is: {sum_natural}")
