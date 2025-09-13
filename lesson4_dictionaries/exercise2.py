# Exercise 2: Subject Grade Dictionary

# Dictionary for grade-to-quality-point mapping
grade_points = {
    "A+": 4.0, "A": 4.0, "A-": 3.7,
    "B+": 3.3, "B": 3.0, "B-": 2.7,
    "C+": 2.3, "C": 2.0, "C-": 1.7,
    "D": 1.0, "F": 0.0
}

# Dictionary to store subject grades
subject_grades = {}

# Get number of subjects
num_subjects = int(input("How many subjects do you have? "))

# Get grades for each subject
for i in range(num_subjects):
    subject = input(f"Enter subject {i+1} name: ")
    grade = input(f"Enter grade for {subject}: ")
    
    # Validate grade
    if grade in grade_points:
        subject_grades[subject] = grade
        print(f"Added: {subject} - {grade}")
    else:
        print(f"Invalid grade '{grade}' for {subject}")

# Display all grades
print("\n=== Your Grades ===")
for subject, grade in subject_grades.items():
    points = grade_points[grade]
    print(f"{subject}: {grade} ({points} quality points)")
