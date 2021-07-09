# Anjum, Syed Rehan
# July 7, 2021
# Printing a Square of Asterisks Given a Number

# 3. Ask a user for a number and print a solid square of '*' characters. 
# Your program will have in-line documentation (a header and in-line comments). 
# Give your program an appropriate name.

print("This program will take a number and then print a square of asterisks with that number of rows and columns.")

# Taking User Input
n = int(input("Number: "))

# Printing Asterisks
for i in range(n):
    for j in range(n):
        print('*', end='')
    print()
        