# Prog02. removesuffix() remove the characters at the end of the string that matches the function parameter. Create a program that do the same functionality without using removesuffix() function.

# Ask user to enter a string
entered_string = input("Enter a string: ")

# Ask user to enter a suffix to be removed
suffix = input("Enter a suffix to be removed: ")

# Process entered string to remove the suffix
if entered_string[-len(suffix):] == suffix:
    modified_string = entered_string[:-len(suffix)]
    
    # Output the string with the suffix removed
    print(modified_string)
else:
    # Output the string without any changes
    print(entered_string)