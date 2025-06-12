'''
Task: Password Strength Checker
Create a Python function that evaluates
the strength of a password entered by the
user. Implement checks for factors such as
length, presence of uppercase and
lowercase letters, digits, and special
characters.
'''

import re

def check_password_strength(password):
    strength = "Weak"
    remarks = []

    # Conditions
    length_error = len(password) < 8
    upper_error = re.search(r"[A-Z]", password) is None
    lower_error = re.search(r"[a-z]", password) is None
    digit_error = re.search(r"\d", password) is None
    special_error = re.search(r"[!@#$%^&*(),.?\":{}|<>]", password) is None

    # Collect remarks
    if length_error:
        remarks.append("• Less than 8 characters")
    if upper_error:
        remarks.append("• Missing uppercase letter")
    if lower_error:
        remarks.append("• Missing lowercase letter")
    if digit_error:
        remarks.append("• Missing digit")
    if special_error:
        remarks.append("• Missing special character")

    # Determine strength
    if not (length_error or upper_error or lower_error or digit_error or special_error):
        strength = "Strong"
    elif not (length_error or (upper_error and lower_error)):
        strength = "Moderate"

    return strength, remarks

# Main code
password = input("Enter your password: ")
strength, feedback = check_password_strength(password)

print(f"\nPassword Strength: {strength}")
if feedback:
    print("Suggestions to improve:")
    for f in feedback:
        print(f)
else:
    print("Your password looks great!")


'''
Output:

Enter your password: Digit@45

Password Strength: Strong
Your password looks great!

OR

Enter your password: gifu

Password Strength: Weak
Suggestions to improve:
• Less than 8 characters
• Missing uppercase letter
• Missing digit
• Missing special character
'''