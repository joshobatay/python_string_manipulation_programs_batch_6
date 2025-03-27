# Prog06. ljust() add space characters at the end of the string to complete the number of characters specifies in function parameter. Create a program that do the same functionality without using ljust() function.

# Ask user to enter a string
entered_string = input("Enter a string: ")

# Ask user width of the string
preferred_width = int(input("Enter width of the string: "))

# Process the entered string to add spaces at the end to complete the width
if len(entered_string) < preferred_width:
    modified_string = entered_string + " " * (preferred_width - len(entered_string))
else:
    modified_string = entered_string

# Output the string with spaces at the end to complete the width
print(f"Modified String:\n|{modified_string}|")