# Author: Anjum, Syed Rehan
# Date: July 12, 2021
# File Name: coin_toss_game.py
# Description: This program will allow the user to toss a coin and use a counter

# Import Statements Here
import random

# Global Variables
coinTossTurns = random.randint(1000,1000000)
counter = 0
head_count = 0
tail_count = 0

print("This program will flip a coin a random number of times.")
print("If the coin flips heads, the counter will increase by 1.")
print("If the coin flips tails, the counter will decrease by 1.")

# For Loop to Flip Coin 
# 1 Represents Heads
# 0 Represents Tails
for flip in range(coinTossTurns):
    if random.choice([1, 0]) == 1:
        counter += 1
        head_count += 1
    else:
        counter -= 1
        tail_count += 1

# Final Output, Displaying Head Count, Tail Count and Final Counter
print("After", coinTossTurns, "tosses, the counter displays", counter)
print("Heads was flipped", head_count, "times.")
print("Tails was flipped", tail_count, "times.")