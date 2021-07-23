# Author: Anjum, Syed Rehan
# Date: July 15, 2021
# File Name: date_conversion.py
# Description: This program converts a date in the MMDDYYYY format

# Import Statements Here

# Global Variables

# Functions
def month(date):
    mm = int(date[0:2])
    if mm == 1:
        return "January"
    elif mm == 2:
        return "February"
    elif mm == 3:
        return "March"
    elif mm == 4:
        return "April"
    elif mm == 5:
        return "May"
    elif mm == 6:
        return "June"
    elif mm == 7:
        return "July"
    elif mm == 8:
        return "August"
    elif mm == 9:
        return "September"
    elif mm == 10:
        return "October"
    elif mm == 11:
        return "November"
    elif mm == 12:
        return "December"

def day(date):
    dd = date[2:4]
    return int(dd)

def year(date):
    yyyy = date[4:8]
    return yyyy

print("This program will convert a date in the form MMDDYYYY")

# User Input
mmddyyyy = input("Please enter a date in the form MMDDYYYY: ")

# Printing Converted Date
print("Your converted date is:", day(mmddyyyy), month(mmddyyyy), year(mmddyyyy))