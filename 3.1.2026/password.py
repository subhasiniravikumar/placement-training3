import re

def check_password(password):
    if len(password) < 8:
        return "Weak: Minimum 8 characters required"
    if not re.search("[A-Z]", password):
        return "Weak: Add uppercase letter"
    if not re.search("[a-z]", password):
        return "Weak: Add lowercase letter"
    if not re.search("[0-9]", password):
        return "Weak: Add digit"
    if not re.search("[@#$!]", password):
        return "Weak: Add special character"

    return "Strong Password"

pwd = input("Enter password: ")
print(check_password(pwd))
