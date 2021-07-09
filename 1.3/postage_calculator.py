# Author: Anjum, Syed Rehan
# Date: July 8, 2021
# File Name: postage_calculator.py
# Description: This program will calculate the cost of your postage

# Import Statements Here

# Global Variables
cost = 0

# Taking User Input
weight = int(input("Please enter the weight of your package (grams): "))

# Calculating Cost
if (weight <= 30): cost = 0.48
elif (weight <= 50): cost = 0.70
elif (weight <= 100): cost = 0.90
else: cost += 0.90 + (weight - 100) // 50 * 0.18;

# Printing Cost
print("The cost of your postage is $%s" % cost)