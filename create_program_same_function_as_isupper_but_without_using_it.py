# Prog04. isupper() check if all characters of the string is on upper case. Create a program that do the same functionality without using isupper() function.

# Ask user to enter a string
entered_string = input("Enter a string: ")

# Assumes the string is in upper case
is_upper = True

# Process entered string to check if it is in upper case
for char in entered_string:
    if "a" <= char <= "z": # If lower case letters are found
        is_upper = False 
        break

# Output the result if the string is in upper case or not
if is_upper:
    print("The entered string is in upper case")
else:
    print("The entered string is not in upper case")