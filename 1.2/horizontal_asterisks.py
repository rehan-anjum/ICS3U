# Anjum, Syed Rehan
# July 7, 2021
# Printing Asterisks in One Line

# 2. Ask the user for a number and print that many '*' characters in a horizontal line. You are going 
# to have to override the default function of print(). Here's how to avoid the newline character from
# printing: print('*', end=''). Your program will have in-line documentation (a header and in-line comments). 
# Give your program an appropriate name.

print("This program will take a number and then print that number of asterisks on one line.")

# Taking User Input
n = int(input("Number: "))

#Printing Asterisks
for i in range(n):
    print('*', end='') 