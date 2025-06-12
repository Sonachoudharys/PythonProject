'''
Task: Temperature Conversion:
 Create a Python program that converts temperatures between Celsius and Fahrenheit. 
 Prompt the user to enter a temperature value and the unit of measurement, and then display the converted temperature
'''

def celsius_to_fahrenheit(celsius):
    return (celsius*9/5)+32  # celsius : C
def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit-32)*5/9  # fahrenheit : F

#user input
temp = float(input("Enter a temperature value :"))
unit = input("Enter the unit of measurement (C or F) :").upper()

# Convert and display result
if unit=='C':
    converted_temp = celsius_to_fahrenheit(temp)
    print(f"{temp}°C is equal to {converted_temp:.2f}°F")
elif unit=='F':
    converted_temp = fahrenheit_to_celsius(temp)
    print(f"{temp}°F is equal to {converted_temp:.2f}°C")
else:
    print("Invalid unit ")

'''
output:
Enter a temperature value :100
Enter the unit of measurement (C or F) :C
100.0°C is equal to 212.00°F

or

Enter a temperature value :100
Enter the unit of measurement (C or F) :F
100.0°F is equal to 37.78°C

or

Enter a temperature value :100
Enter the unit of measurement (C or F) :X
Invalid unit 
'''