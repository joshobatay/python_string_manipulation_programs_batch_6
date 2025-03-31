# Prog03. upper() converts all characters of the string into upper case. Create a program that do the same functionality without using upper() function.

# Ask user to enter a string in lower case
entered_string = input("Enter a string in lower case: ")

# Initialize an empty string
result = ""

# Process entered string to convert all characters into upper case
for char in entered_string:
    if "a" <= char <= "z":
        # ord converts character to ASCII, and 32 is subtracted to convert to upper case, and chr converts ASCII chars to strings
        result += chr(ord(char) - 32)
    else:
        result += char # Does not change the character if it is not a lower case letter

# Output the string in upper case
print(result)