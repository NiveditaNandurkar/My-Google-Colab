# 18. To write a Python program to generate the Fibonacci series up to N terms.

n_terms = int(input("Enter the number of terms for the Fibonacci series: "))

a, b = 0, 1
count = 0

if n_terms <= 0:
    print("Please enter a positive integer.")
elif n_terms == 1:
    print("Fibonacci series up to 1 term:")
    print(a)
else:
    print(f"Fibonacci series up to {n_terms} terms:")
    while count < n_terms:
        print(a, end=' ')
        nth = a + b
        a = b
        b = nth
        count += 1
    print()
