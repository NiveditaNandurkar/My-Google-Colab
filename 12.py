# 12. To write a Python program to print numbers in reverse order from N to 1.

num = int(input("Enter a positive integer (N): "))

if num < 1:
    print("Please enter a positive integer.")
else:
    print(f"Numbers from {num} to 1 (in reverse order):")
    for i in range(num, 0, -1):
        print(i)
