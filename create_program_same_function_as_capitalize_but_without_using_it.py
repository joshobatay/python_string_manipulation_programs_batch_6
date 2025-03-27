# capitalize() makes the first letter of the string, capital letter. And all other letter in small case. Create a program that do the same functionality without using capitalize() function.

# Ask user to enter a string
entered_string = input("Enter a string: ")

# Process entered string to capitalize the first letter
if entered_string:
    modified_string = entered_string[0].upper() + entered_string[1:].lower()
else:
    modified_string = entered_string

# Output the string with the first letter capitalized
print(f"String with first letter capitalized:\n{modified_string}")