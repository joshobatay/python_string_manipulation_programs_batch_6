# Prog01. rstrip() remove the space characters at the end of the string. Create a program that do the same functionality without using rstrip() function.

# Import built-in module textwrap
import textwrap

# Ask user to enter a string with spaces at the end
entered_string = input("Enter a string with spaces at the end: ")

# Process the entered string by reversing, removing spaces, and then reversing it back
modified_string = textwrap.dedent(entered_string[::-1])[::-1]

# Output the string without spaces at the end
print(f"Modified String:\n|{modified_string}|")  # Vertical bars to visualize removed spaces