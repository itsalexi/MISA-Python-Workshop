# Exercise 1: Grade Categorization

# Get grade from user
grade = input("Enter your grade (A, B+, B, C+, C, etc.): ")

# Categorize the grade
if grade == "A":
    print("Outstanding! Excellent performance!")
elif grade == "B+":
    print("Very Good! Above average performance!")
elif grade == "B":
    print("Good! Satisfactory performance!")
elif grade == "C+":
    print("Fair! Room for improvement!")
elif grade == "C":
    print("Passing! Work harder next time!")
elif grade == "D":
    print("Poor! Must improve significantly!")
elif grade == "F":
    print("Failed! Must retake the course!")
else:
    print("Invalid grade entered!")
