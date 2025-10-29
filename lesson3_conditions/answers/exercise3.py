# Exercise 3: Grade Validation

# Get grade from user
grade = input("Enter your grade: ")

# Validate grade and assign quality points
valid_grades = ["A", "B+", "B", "C+", "C", "D", "F"]

if grade in valid_grades:
    # Grade is valid, assign quality points
    if grade == "A":
        quality_points = 4.0
    elif grade == "B+":
        quality_points = 3.5
    elif grade == "B":
        quality_points = 3.0
    elif grade == "C+":
        quality_points = 2.5
    elif grade == "C":
        quality_points = 2.0
    elif grade == "D":
        quality_points = 1.0
    else:  # F
        quality_points = 0.0
    
    print(f"Valid grade: {grade}")
    print(f"Quality Points: {quality_points}")
else:
    print("Invalid grade! Please enter a valid grade.")
    print("Valid grades are:", ", ".join(valid_grades))
