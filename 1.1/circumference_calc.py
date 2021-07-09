# Anjum, Syed Rehan
# July 6, 2021
# Calculating the Circumference of a Circle

# 5. The value PI is more interesting than 3.14. Python provides support for this in a library called math. 
# Calculate the circumference of a circle. Use this formula: circumference = 2PIr. Use the math library to help you with PI. 
# Your program will have in-line documentation (a header and in-line comments). 
# What unit should you use? Give your program an appropriate name.

# Importing Math
import math

# Input for Radius
r = int (input("Radius: "))

# Output Circumference
print("Circumference =", 2*(math.pi)*r, "units")

