# Prog03. lower() converts all characters of the string into lower case. Create a program that do the same functionality without using lower() function.

# Ask user to enter a string in upper case
entered_string = input("Enter string in upper case: ")

# Initialize an empty string
result = ""

# Process the entered string to convert all characters into lower case
for char in entered_string:
    if "A" <= char <= "Z":
        # ord converts character to ASCII, and 32 is added to convert to lower case, and chr converts ASCII chars to strings
        result += chr(ord(char) + 32) 
    else:
        result += char # Does not change the character if it is not an upper case letter

# Output the string in lower case
print(f"String in lower case:\n{result}")