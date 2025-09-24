import re

# Take password input
password = input("Enter your password: ")

# Initialize strength score
strength = 0
suggestions = []

# Check for length
if len(password) >= 8:
    strength += 1
else:
    suggestions.append("Increase password length to 8 or more characters")

# Check for lowercase letters
if re.search(r"[a-z]", password):
    strength += 1
else:
    suggestions.append("Add lowercase letters")

# Check for uppercase letters
if re.search(r"[A-Z]", password):
    strength += 1
else:
    suggestions.append("Add uppercase letters")

# Check for digits
if re.search(r"\d", password):
    strength += 1
else:
    suggestions.append("Add numbers")

# Check for special characters
if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
    strength += 1
else:
    suggestions.append("Add special characters")

# Display password strength
if strength == 5:
    print("Your password strength is: Very Strong")
elif strength >= 4:
    print("Your password strength is: Strong")
elif strength >= 3:
    print("Your password strength is: Moderate")
else:
    print("Your password strength is: Weak")

# Display suggestions if password is not very strong
if suggestions:
    print("Suggestions to improve your password:")
    for s in suggestions:
        print("-", s)
