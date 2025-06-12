'''
Task: Email Validator
Develop a Python function that validates
whether a given string is a valid email
address. Implement checks for the format,
including the presence of an "@" symbol and
a domain name
'''

import re

def is_valid_email(email):
    # Regular expression for basic email validation
    pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z]{2,}$'
    
    if re.match(pattern, email):
        return True
    else:
        return False

# Ask user to enter email
email = input("Enter an email address to validate: ")

# Validate and print result
if is_valid_email(email):
    print("Valid Email Address")
else:
    print("Invalid Email Address")

'''
Output:
Enter an email address to validate: test@example.com
Valid Email Address

OR

Enter an email address to validate: user@domain
Invalid Email Address

OR

Enter an email address to validate: abc@.com
Invalid Email Address

'''

