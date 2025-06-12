'''
Task: String Reversal
 Create a Python function that takes a
 string as input and returns the reverse of
 that string. For example, if the input is
 "hello" the function should return
 "olleh."

'''


def reverse_string(text):
    return text[::-1]

input_text = input("Enter a string: ")
reversed_text = reverse_string(input_text)

print("Reversed string:", reversed_text)


'''
output:
Enter a string: hello
Reversed string: olleh
'''