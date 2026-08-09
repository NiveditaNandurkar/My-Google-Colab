# 13. To write a Python program to print all even numbers up to a given limit.

limit = int(input("Enter an upper limit: "))

if limit < 1:
    print("Please enter a positive integer as the limit.")
else:
    print(f"Even numbers up to {limit}:")
    for i in range(1, limit + 1):
        if i % 2 == 0:
            print(i)
