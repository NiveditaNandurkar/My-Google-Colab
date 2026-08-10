# 19. To write a Python program to check whether a string is a palindrome.

input_string = input("Enter a string: ")
# Remove non-alphanumeric characters and convert to lowercase for a case-insensitive and punctuation-insensitive check
processed_string = "".join(char for char in input_string if char.isalnum()).lower()

# Reverse the processed string
reversed_string = processed_string[::-1]

# Check if it's a palindrome
if processed_string == reversed_string:
    print(f"'{input_string}' is a palindrome.")
else:
    print(f"'{input_string}' is not a palindrome.")
