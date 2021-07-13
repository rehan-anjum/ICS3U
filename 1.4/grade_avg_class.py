# Author: Anjum, Syed Rehan
# Date: July 9, 2021
# File Name: grade_avg_class.py
# Description: This program will calculate the class average for letter grades

# Import Statements Here

# Global Variables
totalClassGrade = 0
passCount = 0
failCount = 0

# Functions Here
def convertGrade(grade):
    if (grade == 'A' or grade == 'a'):
        return 80
    elif (grade == 'B' or grade == 'b'):
        return 70
    elif (grade == 'C' or grade == 'c'):
        return 60
    elif (grade == 'D' or grade == 'd'):
        return 50
    elif (grade == 'F' or grade == 'f'):
        return 40

print("This program will calculate the class average for letter grades")

# Taking User Input
numOfStudents = int(input("How many students does your class have: "))

# Converting Letter to Percentage and Calculating Average
for student in range(numOfStudents):
    print("Please enter student ", student+1, "'s grade: ", sep='')
    currentStudentGrade = input()
    if convertGrade(currentStudentGrade) < 50: failCount += 1
    else: passCount += 1
    totalClassGrade += convertGrade(currentStudentGrade)

# Final Output
print("The class's average is", (totalClassGrade/numOfStudents))
if (passCount == 1 and failCount == 1):
    print(passCount, "student is passing and", failCount, "student is failing.")
elif(passCount == 1):
    print(passCount, "student is passing and", failCount, "students are failing.")
elif(failCount == 1):
    print(passCount, "students are passing and", failCount, "student is failing.")
else:
    print(passCount, "students are passing and", failCount, "students are failing.")