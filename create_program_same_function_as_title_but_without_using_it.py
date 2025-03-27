# title() makes all first letter of each word in the string, capital letter. And all other letter in small case. Create a program that do the same functionality without using title() function.

# Ask user to enter a string
entered_string = input("Enter a string: ")

# Split the entered string into words
words = entered_string.split()

# Initialize an empty string for result
result = ""

# Process the entered string to capitalize the first letter of each word
for word in words:
    modified_word = word[0].upper() + word[1:].lower()
    result += modified_word + " "
 
# Remove the trailing spaces from the result
result = result.strip()

# Output the string with the first letter of each word capitalized
print(f"String with first letter of each word capitalized:\n{result}")