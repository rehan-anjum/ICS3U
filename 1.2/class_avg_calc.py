# Anjum, Syed Rehan
# July 7, 2021
# Calculating Class Average

# 4. Your teacher needs help calculating the class average. Your application will ask how 
# many students are in the class, and it will then accept that many number of grades, and 
# calculate the class average. Your program will have in-line documentation (a header and 
# in-line comments). Give your program an appropriate name.

print("This program will calculate the average grade of your class.")

# Taking User Input
n = int(input("Number of students the class has: "))

# Total Class Grade Variable
sumOfGrades = 0

# Taking User Input for Grades
for i in range(n):
    print("Please enter student ", i+1, "'s grade: ", sep='')
    sumOfGrades += int(input())

# Class Average
print("Class Average:", sumOfGrades/n)