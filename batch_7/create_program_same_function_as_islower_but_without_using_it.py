# Prog04. islower() check if all characters of the string is on lower case. Create a program that do the same functionality without using islower() function.

# Ask user to enter a string
entered_string = input("Enter a string: ")

# Process entered_string to check if it is lower case
for char in entered_string:
    if not ("a" <= char <= "z"):
        print("String is not lower case.") # Output the result
        break
else:
    print("String is lower case.") # Output the result

