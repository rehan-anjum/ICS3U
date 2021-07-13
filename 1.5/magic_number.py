# Author: Anjum, Syed Rehan
# Date: July 12, 2021
# File Name: magic_number.py
# Description: This program will allow the user to guess a number

# Import Statements Here
import random

# Global Variables
randomNum = random.randint(1,10)
guessNum = None
guessCount = 0

print("A random number between 1 and 10 has been selected!")
print("While guessing, enter 0 if you wish to exit the program.")

# While Loop for the User to Guess
while guessNum != randomNum:
    guessNum = int(input("Enter your guess: "))
    guessCount += 1
    if guessNum > randomNum:
        print("Your guess was too high.")
    elif guessNum < randomNum:
        print("Your guess was too low.")
    elif guessNum == 0:
        print("You quit! The program is ending.")
        break
    else:
        print("You guessed the right number!")
        print("It took you", guessCount, "guesses.")

# Final Output Showing Magic Number
print("The magic number was", randomNum)




    

