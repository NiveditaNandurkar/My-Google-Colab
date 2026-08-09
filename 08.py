# 8. To write a Python program to display the multiplication table of a given
# number.

num = int(input("Enter a number: "))
limit = int(input("Enter the limit for the multiplication table (e.g., 10): "))

print(f"\nMultiplication Table for {num} up to {limit}:")
for i in range(1, limit + 1):
    print(f"{num} x {i} = {num * i}")
