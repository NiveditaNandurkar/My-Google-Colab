"""3. To write a Python program to find the largest among three numbers using
conditional statements."""
a = 10
b = 20
c = 30
if a >= b and a >= c:
    print("Largest number is:", a)
elif b >= a and b >= c:
    print("Largest number is:", b)
else:
    print("Largest number is:", c)