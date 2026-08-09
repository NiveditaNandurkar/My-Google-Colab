# 17. To write a Python program to check whether a given number is prime.

num = int(input("Enter a positive integer: "))

# Prime numbers are greater than 1
if num <= 1:
    print(f"{num} is not a prime number.")
elif num == 2:
    print(f"{num} is a prime number.")
else:
    is_prime = True
    # Check for factors from 2 up to the square root of num
    # Any factor larger than sqrt(num) would have a corresponding smaller factor already found
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            is_prime = False
            break

    if is_prime:
        print(f"{num} is a prime number.")
    else:
        print(f"{num} is not a prime number.")
