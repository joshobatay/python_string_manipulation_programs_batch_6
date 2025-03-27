# center() add space characters at the beginning and at the end of the string to print the string at the center. Create a program that do the same functionality without using center() function.

# Ask user to enter a string
entered_string = input("Enter a string: ")

# Ask user width of the string
preferred_width = int(input("Enter width of the string: "))

# Process the entered string to add spaces at the beginning and at the end 
total_padding = max(0, preferred_width - len(entered_string)) # max for ensuring padding is not negative

# Distributes padding evenly on both sides
padding_left = total_padding // 2
padding_right = total_padding - padding_left

# Constructs the modified string
modified_string = " " * padding_left + entered_string + " " * padding_right

# Output the string with spaces at the beginning and at the end to print the string at the center
print(f"Modified String:\n|{modified_string}|") # Straight lines to visualize added spaces at the beginning and at the end