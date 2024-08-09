import re

def password_strength(password):
    if len(password) < 8:
        return "Too short"
    if not re.search("[a-z]", password):
        return "Missing lowercase characters"
    if not re.search("[A-Z]", password):
        return "Missing uppercase characters"
    if not re.search("[0-9]", password):
        return "Missing numbers"
    if not re.search("[!@#$%^&*()_+-=;:'\"<>,.?/\\|]", password):
        return "Missing special characters"
    return "Strong password"

password = input("Enter a password: ")
print(password_strength(password))