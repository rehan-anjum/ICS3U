# Anjum, Syed Rehan
# July 6, 2021
# Calculating the Velocity of a Baseball Thrown in Space

# 4. Write a program in Python that calculates the velocity of a baseball thrown in space. Use this formula: velocity = d/t. 
# Your program will have in-line documentation (a header and in-line comments). 
# What unit should you use? Name your program velocity_calc.py

print("This program will calculate the velocity of a baseball thrown in space.")

# Input for Base and Height
d = int(input("Displacement: "))
t = int (input("Time: "))

# Output Velocity
print("Velocity =", d/t, "m/s")