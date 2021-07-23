# Author: Anjum, Syed Rehan
# Date: July 15, 2021
# File Name: morse_code.py
# Description: This program converts text into Morse Code

# Import Statements Here

# Global Variables

# Functions

morse_code_dictionary = { 
    'A':'.-', 'B':'-...',
    'C':'-.-.', 'D':'-..', 'E':'.',
    'F':'..-.', 'G':'--.', 'H':'....',
    'I':'..', 'J':'.---', 'K':'-.-',
    'L':'.-..', 'M':'--', 'N':'-.',
    'O':'---', 'P':'.--.', 'Q':'--.-',
    'R':'.-.', 'S':'...', 'T':'-',
    'U':'..-', 'V':'...-', 'W':'.--',
    'X':'-..-', 'Y':'-.--', 'Z':'--..',
    '1':'.----', '2':'..---', '3':'...--',
    '4':'....-', '5':'.....', '6':'-....',
    '7':'--...', '8':'---..', '9':'----.',
    '0':'-----'
}

def convert(string):
    converted_string = ""
    for char in string:
        if char != ' ':
            converted_string += morse_code_dictionary[char]
        elif char == ' ':
            converted_string += ' '
    return converted_string

print("This program converts a given message into Morse Code.")

# User Input
print("Please enter the message you would like to convert: ")
message = input()

# Converting the Message and Final Output
print("Your converted message is:", convert(message), sep='\n')


