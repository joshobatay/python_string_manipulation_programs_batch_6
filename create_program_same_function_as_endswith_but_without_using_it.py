# Prog05. endswith() check if the string end part matches the function parameter. Create a program that do the same functionality without using endswith() function.

# Ask user to input a string
entered_string = input("Enter a string: ")

# Ask user what string to check if it ends with
suffix = input("Enter a string to check if the entered string ends with: ")

# Process the entered string to check if it ends with the parameter string
if entered_string[-len(suffix):] == suffix:
    # Output the result if the string ends with the parameter string or not
    print(f"The entered string ends with the suffix: {suffix}")
else:
    print(f"The entered string does not end with {suffix}")


