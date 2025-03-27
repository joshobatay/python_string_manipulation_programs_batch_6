# Prog02. removeprefix() remove the characters at the beginning of the string that matches the function parameter. Create a program that do the same functionality without using removeprefix() function.

# Ask user to enter a string with characters at the beginning
entered_string = input("Enter a string with characters at the beginning: ")

# Initiate what string to be removed and process
prefix = "www."

if entered_string.startswith(prefix):
    cleaned_string = entered_string[len(prefix):]
else:
    cleaned_string = entered_string

# Output the string without the characters at the beginning
print(f"Cleaned String:\n{cleaned_string}")