# Prog07. zfill() add zero characters at the beginning of the string to complete the number of characters specifies in function parameter. Create a program that do the same functionality without using zfill() function.

# Ask user to enter a number
entered_number = input("Enter a number: ")

# Ask user preferred digits
preferred_digits = int(input("Enter preferred digits: "))

# Process entered number to add zeros at the beginning to complete the digits
if len(entered_number) < preferred_digits:
    modified_string = "0" * (preferred_digits - len(entered_number)) + entered_number
else:
    modified_string = entered_number

# Output the string with zeros at the beginning to complete the digits
print(modified_string)
