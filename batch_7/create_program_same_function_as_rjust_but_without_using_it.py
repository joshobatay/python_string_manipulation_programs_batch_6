# Prog06. rjust() add space characters at the beginning of the string to complete the number of characters specifies in function parameter. Create a program that do the same functionality without using rjust() function.

# Ask user to enter a string
entered_string = input("Enter a string: ")

# Ask user preferred width of the string
preferred_width = int(input("Enter width of the string: "))

# Process the entered string to add spaces at the beginning to complete the width
if len(entered_string) < preferred_width:
    modified_string = " " * (preferred_width - len(entered_string)) + entered_string
else:
    modified_string = entered_string

# Output the string with spaces at the beginning  
print(f"|{modified_string}|") # Straight lines to visualize added spaces