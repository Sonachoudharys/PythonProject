'''
Task: Palindrome Checker
Write a Python function that checks whether
a given string is a palindrome. A palindrome
is a word, phrase, or sequence that reads the
same backward as forward (e.g., "madam" or "racecar").
'''

def is_palindrome(text):
    # Remove spaces and convert to lowercase for uniformity
    cleaned = ''.join(text.lower().split())

    # Check if string is equal to its reverse
    return cleaned == cleaned[::-1]

# Example usage
user_input = input("Enter a word or phrase: ")

if is_palindrome(user_input):
    print("It's a palindrome!")
else:
    print("Not a palindrome.")

'''
Output:

Enter a word or phrase: madam
It's a palindrome!

OR

Enter a word or phrase: racecar
It's a palindrome!

OR

Enter a word or phrase: hello
Not a palindrome.
'''