# Exercise 2: Quality Points Assignment

# Get grade from user
grade = input("Enter your grade (A+, A, B+, B, etc.): ")

# Assign quality points based on grade
if grade == "A+":
    quality_points = 4.0
elif grade == "A":
    quality_points = 4.0
elif grade == "A-":
    quality_points = 3.7
elif grade == "B+":
    quality_points = 3.3
elif grade == "B":
    quality_points = 3.0
elif grade == "B-":
    quality_points = 2.7
elif grade == "C+":
    quality_points = 2.3
elif grade == "C":
    quality_points = 2.0
elif grade == "C-":
    quality_points = 1.7
elif grade == "D":
    quality_points = 1.0
elif grade == "F":
    quality_points = 0.0
else:
    quality_points = None
    print("Invalid grade!")

# Display result
if quality_points is not None:
    print(f"Grade: {grade}")
    print(f"Quality Points: {quality_points}")
