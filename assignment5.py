import re

# Accept string from user
user_input = input("Enter a string to validate: ")

# Define regex pattern for a-z, A-Z, 0-9
pattern = r"^[a-zA-Z0-9]+$"

# Check if the string matches the pattern
if re.match(pattern, user_input):
    print(f"'{user_input}' contains ONLY valid characters (a-z, A-Z, 0-9).")
else:
    print(f"'{user_input}' contains invalid characters/symbols.")

# Alternatively, using built-in string methods (without regex)
print("\n--- Using Python built-in isalnum() method ---")
if user_input.isalnum():
    print("Valid: Contains only letters and numbers.")
else:
    print("Invalid: Contains special characters or spaces.")
