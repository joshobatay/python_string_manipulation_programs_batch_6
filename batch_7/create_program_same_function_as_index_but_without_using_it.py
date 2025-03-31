# Prog09. index() return the first location of the function parameter in the string. Create a program that do the same functionality without using index() function.

# Ask user to enter a string
entered_string = input("Enter a string: ")

# Ask user a character to find its index
char_index = input("Enter a character to find its index: ")

# Initialize a variable to store the index
index_pos = -1

# Process the entered string to find the index of the character
for i in range(len(entered_string)):
    if entered_string[i] == char_index:
        index_pos = i
        break

# Output the index of the character in the string
if index_pos != -1:
    print(f"The character '{char_index}' is found at index {index_pos} in the string.")
else:
    print(f"The character '{char_index}' is not found in the string.")