# Anjum, Syed Rehan
# July 6, 2021
# Converting Temperature from Fahrenheit to Celsius

# 6. Convert a temperature given in Fahrenheit to Celsius. Use this formula Celsius = 5/9 (F - 32). 
# Your program will have in-line documentation (a header and in-line comments). What unit should you use? 
# Give your program an appropriate name.

print("This program will convert temperature from Fahrenheit to Celsius.")

# Input for Temperature
f = float(input("Temperature in Fahrenheit: "))

# Convert Temperature
t = (5/9)*(f-32)

# Output Temperature
print("Temperature =", t, "degrees Celsius")
