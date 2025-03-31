# Prog05. startswith() check if the string beginning part matches the function parameter. Create a program that do the same functionality without using startswith() function.

# Ask user to enter a string
entered_string = input("Enter a string: ")

# Ask user what string to check if it starts with
prefix = input("Enter a string to check: ")

# Process entered string to check if it starts with the parameter string
if entered_string[:len(prefix)] == prefix:
    print(f"The entered string starts with the prefix: {prefix}") # Output the result
else:
    print(f"The entered string does not start with {prefix}")