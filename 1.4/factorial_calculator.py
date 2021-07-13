# Author: Anjum, Syed Rehan
# Date: July 9, 2021
# File Name: factorial_calculator.py
# Description: This program will calculate the factorial of any number

# Import Statements Here

# Global Variables

# Functions here
def factorial(n):
    return n * factorial(n - 1) if n > 1 else 1

print("This program will calculate the factorial of any number")

# Taking User Input
num = int(input("Please enter the number that you would like to calculate the factorial for: "))

# Final Output
print("The factorial of", num, "is", factorial(num))