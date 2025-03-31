# Prog08. count() return how many time the function parameter appear in the string. Create a program that do the same functionality without using count() function.

# Ask user to enter a string
entered_string = input("Enter a string: ")

# Ask user character to count
char_count = input("Enter a character to count: ")

# Initialize a counter variable to zero
counter = 0

# Process the entered string to count the occurrences of the character
for char in entered_string:
    if char == char_count:
        counter += 1

# Output the number of occurrences of the character in the string
print(f"The character '{char_count}' appears {counter} times in the string.")