# Anjum, Syed Rehan
# July 7, 2021
# Password Checker

# 5. Write a password checker. Your password checker will first ask for a password, then 
# repetitively ask the user to guess at the password. When the user types the same password, 
# acknowledge that the right password was provided. Your program will have in-line documentation 
# (a header and in-line comments). Give your program an appropriate name. DO NOT USE AN IF STATEMENT.

print("This program will check your password.")

# Taking User Input
password = input("Enter your password: ")

# Declaring Initial Guess Variable
guess = ''

# While Loop for User to Guess Password
while guess != password:
    guess = input("Enter your guess: ")

# Output for Correct Password Provided
print("The correct password was provided.")