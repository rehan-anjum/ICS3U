# Author: Anjum, Syed Rehan
# Date: July 15, 2021
# File Name: first_five_names.py
# Description: This program stores 5 first names and allows you to edit them

# Import Statements Here
import sys

# Global Variables

# Functions
# Function to leave the program
def leave_program():
    print("The program is now ending.")
    sys.exit()
    
# Function to edit a specific name
def edit_name(names):
    name = input("What name would you like to edit? ")
    if name in names:
        index = names.index(name)
        new_name = input("What would you like to change the name to? ")
        names[index] = new_name
    else:
        print("Sorry, that name does not exist!")

# Function to display a specific name
def display_name(names):
    print("What name would you like to display?")
    index = int(input("Please enter the index of the name: "))
    print("The name is:", names[index-1])

# Function to delete a specific name
def delete_name(names):
    name = input("What name would you like to delete? ")
    if name in names:
        index = names.index(name)
        names.remove(name)
    else:
        print("Sorry, that name does not exist!")

# Function to display all names
def display_all_names(names):
    for name in names:
        print(name)

# Starting output
print("This program will allow you to store 5 first names and then let you edit them.")
print("Please enter your 5 names.")
names = input().split(' ', 5)

# While loop displaying all options
while True:
    print("What would you like to do?")
    print("Enter /'l/' to exit the program")
    print("Enter /'e/' to edit a name")
    print("Enter /'dis/' to display a specific name")
    print("Enter /'disp/' to display all names")
    print("Enter /'del/' to delete a name")
    choice = input()
    if choice == "l":
        leave_program()
    elif choice == "e":
        edit_name(names)
    elif choice == "dis":
        display_name(names)
    elif choice == "disp":
        display_all_names(names)
    elif choice == "del":
        delete_name(names)
    else:
        print("Please enter a correct value.")
