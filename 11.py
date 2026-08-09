# 11. To write a Python program to print numbers from 1 to N using a for loop.

num = int(input("Enter a positive integer (N): "))

if num < 1:
    print("Please enter a positive integer.")
else:
    print(f"Numbers from 1 to {num}:")
    for i in range(1, num + 1):
        print(i)
