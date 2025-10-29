# Exercise 2: Grade Input with Validation

# Valid grades
valid_grades = ["A", "B+", "B", "C+", "C", "D", "F"]

# Grade-to-quality-point mapping
grade_points = {
    "A": 4.0,
    "B+": 3.5,
    "B": 3.0,
    "C+": 2.5,
    "C": 2.0,
    "D": 1.0,
    "F": 0.0
}

# Get number of subjects
num_subjects = int(input("How many subjects do you have? "))

# Collect grades with validation
subject_grades = {}
for i in range(num_subjects):
    subject = input(f"\nEnter subject {i+1} name: ")
    
    # Keep asking until valid grade is entered
    while True:
        grade = input(f"Enter grade for {subject}: ")
        if grade in valid_grades:
            subject_grades[subject] = grade
            break
        else:
            print("Invalid grade! Valid grades are:", ", ".join(valid_grades))

# Display results
print("\n=== Your Grades ===")
total_points = 0
for subject, grade in subject_grades.items():
    points = grade_points[grade]
    total_points += points
    print(f"{subject}: {grade} ({points} quality points)")

print(f"\nTotal Quality Points: {total_points}")
