# Exercise 1: Grade Categorization

# Get grade from user
grade = input("Enter your grade (A+, A, B+, B, etc.): ")

# Categorize the grade
if grade == "A+":
    print("Outstanding! Perfect performance!")
elif grade == "A":
    print("Excellent! Great job!")
elif grade == "A-":
    print("Very Good! Above average!")
elif grade == "B+":
    print("Good! Above average performance!")
elif grade == "B":
    print("Good! Satisfactory performance!")
elif grade == "B-":
    print("Satisfactory! Keep improving!")
elif grade == "C+":
    print("Fair! Room for improvement!")
elif grade == "C":
    print("Passing! Work harder next time!")
elif grade == "C-":
    print("Passing! Needs improvement!")
elif grade == "D":
    print("Poor! Must improve significantly!")
elif grade == "F":
    print("Failed! Must retake the course!")
else:
    print("Invalid grade entered!")
