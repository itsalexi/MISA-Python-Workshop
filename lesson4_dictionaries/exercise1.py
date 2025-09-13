# Exercise 1: Basic Grade Dictionary

# Create a dictionary mapping grades to quality points
grade_points = {
    "A+": 4.0,
    "A": 4.0,
    "A-": 3.7,
    "B+": 3.3,
    "B": 3.0,
    "B-": 2.7,
    "C+": 2.3,
    "C": 2.0,
    "C-": 1.7,
    "D": 1.0,
    "F": 0.0
}

# Get grade from user
grade = input("Enter your grade: ")

# Look up quality points
quality_points = grade_points.get(grade, "Invalid grade")

# Display result
if quality_points != "Invalid grade":
    print(f"Grade: {grade}")
    print(f"Quality Points: {quality_points}")
else:
    print("Invalid grade entered!")
    print("Valid grades:", list(grade_points.keys()))
