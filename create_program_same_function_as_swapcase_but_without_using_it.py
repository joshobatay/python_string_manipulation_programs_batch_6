# swapcase() reverse the casing of each of the character of the string. Create a program that do the same functionality without using swapcase() function.

# Ask user to enter a string
entered_string = input("Enter a string: ")

# Initiate an empty string
result = ""

# Process the entered string to reverse the casing of each character
for char in entered_string:
    if "A" <= char <= "Z":
        # 32 is added to convert to lower case
        result += chr(ord(char) + 32) 
        # 32 is subtracted to convert to upper case
    elif "a" <= char <= "z":
        result += chr(ord(char) - 32)
    else:
        result += char # Does not change the character if it is not a letter
    
# Output the string with reversed casing
print(f"String with reversed casing:\n{result}")