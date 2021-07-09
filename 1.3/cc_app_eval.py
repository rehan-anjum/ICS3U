# Author: Anjum, Syed Rehan
# Date: July 8, 2021
# File Name: cc_app_eval.py
# Description: This program will evaluate your credit card application and return your eligibility

#import statements here

# Global Variables
score = 0
eligibility = ''

print("This program will evaluate your credit card application and return your eligibility")

# Taking User Input
age = int(input("Please enter your age: "))
currentAddress = int(input("How many years have you been living at your current address for: "))
annualIncome = int(input("What is your annual income ($): "))
yearsAtJob = int(input("How many years have you been working at your current job for: "))

# Evaluating Age
if (age <= 20): score -= 10
elif (31 <= age <= 50): score += 20
elif (age > 50): score += 25

# Evaluating Current Address
if (currentAddress < 1): score -= 5
elif (currentAddress <= 3): score += 5
elif (currentAddress <= 8): score += 12
else: score += 20

# Evaluating Annual Income
if (annualIncome < 25000): score += 12
elif (annualIncome < 40000): score += 24
else: score += 30

# Evaluating Years at Job
if (yearsAtJob < 2): score -= 4
elif (yearsAtJob <= 4): score += 8
else: score += 15

# Printing Eligibility
print("You are eligible for: ", end='')
if (score < 20): print("no card")
elif (score <= 35): print("card with $500 limit")
elif (score <= 60): print("card with $2000 limit")
else: print("card with $5000 limit")