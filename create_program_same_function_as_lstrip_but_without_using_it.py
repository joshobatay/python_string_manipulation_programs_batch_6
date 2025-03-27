# Prog01. lstrip() remove the space characters at the beginning of the string. Create a program that do the same functionality without using lstrip() function.

# Import built in module textwrap
import textwrap

# Ask user to enter a string with spaces at the beginning
entered_string = input("Enter a string with spaces at the beginning: ")

# Process entered string to remove the spaces at the beginning
cleaned_string = textwrap.dedent(entered_string)

# Output the string without spaces at the beginning
print(f"Cleaned String:\n{cleaned_string}")
