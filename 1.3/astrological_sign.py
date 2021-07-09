# Author: Anjum, Syed Rehan
# Date: July 8, 2021
# File Name: astrological_sign.py
# Description: This program will tell you your astrological sign based on your birthday

# Import Statements Here

# Global Variables
astrologicalSign = ''

print("This program will tell you your astrological sign based on your birthday")

# Taking User Input
year = int(input("Please enter your year of birth: "))
month = int(input("Please enter your month of birth: "))
day = int(input("Please enter your day of birth: "))

# Aquarius Jan 20-Feb 18
# Pisces Feb 19-Mar 20
# Aries Mar 21-Apr 19
# Taurus Apr 20-May 20
# Gemini May 21-Jun 21
# Cancer Jun 22-Jul 22
# Leo Jul 23-Aug 22
# Virgo Aug 23-Sep 22
# Libra Sep 23-Oct 23
# Scorpio Oct 24-Nov 21
# Sagittarius Nov 22-Dec 21
# Capricorn Dec 22-Jan 19

# Checking for All Months
if (month == 1):
    if (day <= 19): astrologicalSign = 'Capricorn'
    else: astrologicalSign = 'Aquarius'

elif (month == 2):
    if (day <= 18): astrologicalSign = 'Aquarius'
    else: astrologicalSign = 'Pisces'

elif (month == 3):
    if (day <= 20): astrologicalSign = 'Pisces'
    else: astrologicalSign = 'Aries'

elif (month == 4):
    if (day <= 19): astrologicalSign = 'Aries'
    else: astrologicalSign = 'Taurus'

elif (month == 5):
    if (day <= 20): astrologicalSign = 'Taurus'
    else: astrologicalSign = 'Gemini'

elif (month == 6):
    if (day <= 21): astrologicalSign = 'Gemini'
    else: astrologicalSign = 'Cancer'

elif (month == 7):
    if (day <= 22): astrologicalSign = 'Cancer'
    else: astrologicalSign = 'Leo'

elif (month == 8):
    if (day <= 22): astrologicalSign = 'Leo'
    else: astrologicalSign = 'Virgo'

elif (month == 9):
    if (day <= 22): astrologicalSign = 'Virgo'
    else: astrologicalSign = 'Libra'

elif (month == 10):
    if (day <= 23): astrologicalSign = 'Libra'
    else: astrologicalSign = 'Scorpio'

elif (month == 11):
    if (day <= 21): astrologicalSign = 'Scorpio'
    else: astrologicalSign = 'Sagittarius'

elif (month == 12):
    if (day <= 21): astrologicalSign = 'Sagittarius'
    else: astrologicalSign = 'Capricorn'

# Final Output
print("Your astrological sign is %s" % astrologicalSign)
print("Program ending.")