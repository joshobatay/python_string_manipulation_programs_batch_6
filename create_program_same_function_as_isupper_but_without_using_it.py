# Prog04. isupper() check if all characters of the string is on upper case. Create a program that do the same functionality without using isupper() function.

# Ask user to enter a string
entered_string = input("Enter a string: ")

# Process entered string to check if it is in upper case
for char in entered_string:
    if "a" <= char <= "z":  # If lower case letters are found
        # Output the result if the string is in upper case or not
        print("The entered string is not in upper case")
        break
else:
    print("The entered string is in upper case")

