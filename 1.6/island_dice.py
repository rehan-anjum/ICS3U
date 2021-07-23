# Author: Anjum, Syed Rehan
# Date: July 13, 2021
# File Name: island_dice.py
# Description: This program is the island dice roll game

# Import Statements Here
import random
import sys

# Global Variables
user_score = 1000

# Functions
# Showing the Score
def show_score():
    print("You have", user_score, "shells.")

# Showing the Amount of Shells at Risk
def show_bet():
    print("You have", shells_at_risk, "shells at risk.")

# Letting the User Choose High or Low
def user_turn():
    choice = input("Choose high or low: ")
    if choice == "exit":
        print("The game is ending.")
        sys.exit()
    return choice

# Rolling the Dice
def dice_roll():
    dice_1 = random.randint(1, 6)
    dice_2 = random.randint(1, 6)
    dice_total = dice_1 + dice_2
    return dice_total

# Checking if the Dice Total is High, Low, or Neither
def check_dice_total(dice_total):
    dice_total_checked = ""
    if 2 <= dice_total <= 6:
        dice_total_checked += "low"
    elif dice_total == 7:
        dice_total_checked += "neither"
    else:
        dice_total_checked += "high"
    return dice_total_checked

# Printing That The User Won Shells
def won_shells(shells_amount):
    print("You won", shells_amount, "shells.")

# Printing That The User Lost Shells
def lost_shells(shells_amount):
    print("You lost", shells_amount, "shells.")

# Printing What The Dice Rolled
def dice_call(dice_outcome):
    if dice_outcome == "high":
        print("The dice rolled high.")
    elif dice_outcome == "low":
        print("The dice rolled low.")
    else:
        print("The dice rolled neither high or low.")

print("This is the Island Dice Roll Game.")
print("You have a starting score of 1000 shells.")
print("Enter \"exit\" at any time to stop the program.")

# User Input, How Many Shells The User Wants To Risk
shells_at_risk = int(input("How many shells would you like to risk? "))

# Playing The Game While The User Score Is Greater Than 0
while (user_score > 0):
    
    user_choice = user_turn()
    dice_total = dice_roll()  

    if check_dice_total(dice_total) == "high" and user_choice == "high":
        shells_at_risk *= 2
        user_score += shells_at_risk
        dice_call(check_dice_total(dice_total))
        won_shells(shells_at_risk)
        
    elif check_dice_total(dice_total) == "low" and user_choice == "low":
        shells_at_risk *= 2
        user_score += shells_at_risk
        dice_call(check_dice_total(dice_total))
        won_shells(shells_at_risk)

    elif check_dice_total(dice_total) == "high" and user_choice == "low":
        user_score -= shells_at_risk
        dice_call(check_dice_total(dice_total))
        lost_shells(shells_at_risk)
    
    elif check_dice_total(dice_total) == "low" and user_choice == "high":
        user_score -= shells_at_risk
        dice_call(check_dice_total(dice_total))
        lost_shells(shells_at_risk)
    
    else:
        user_score -= shells_at_risk
        dice_call(check_dice_total(dice_total))
        lost_shells(shells_at_risk)
    
    show_score()
    show_bet()

print("You have no shells remaining, the game is ending.")