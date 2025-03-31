# Prog07. zfill() add zero characters at the beginning of the string to complete the number of characters specifies in function parameter. Create a program that do the same functionality without using zfill() function.

# Ask user to enter a number
entered_number = input("Enter a number: ")

# Ask user preferred digits
preferred_digits = int(input("Enter preferred digits: "))

# Checks if entered number is negative
is_negative = entered_number.startswith('-')

# Remove the negative sign for processing
if is_negative:
    entered_number = entered_number[1:]

# Process entered number to add zeros at the beginning to complete the digits
if len(entered_number) < preferred_digits:
    modified_string = "0" * (preferred_digits - len(entered_number)) + entered_number
else:
    modified_string = entered_number

# Restore the negative sign if it was removed
if is_negative:
    modified_string = '-' + modified_string

# Output the string with zeros at the beginning to complete the digits
print(modified_string)
