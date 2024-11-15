# Program to check the ASCII code of an alphabet

# Input from the user
char = input("Enter a single alphabet: ")

# Check if the input is a single character and an alphabet
if len(char) == 1 and char.isalpha():
    # Get and display the ASCII value
    ascii_value = ord(char)
    print(f"The ASCII code for '{char}' is: {ascii_value}")
else:
    print("Please enter a valid single alphabet.")
