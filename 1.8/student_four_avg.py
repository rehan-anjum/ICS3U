# Author: Anjum, Syed Rehan
# Date: July 15, 2021
# File Name: student_four_avg.py
# Description: This program calculates a students average of 4 classes

# Import Statements Here

# Global Variables

# Functions
# Function to Calculate Average
def calculate_avg(grades):
    cnt = 0
    for grade in grades:
        cnt += grade
    cnt /= 4
    return cnt

print("This program will calculate your average based on your average from 4 classes.")

# User Input as a List
print("Please enter your 4 grades.")
grades = input().split(' ', 4)

# Final Output
print("Your average is", calculate_avg(grades))