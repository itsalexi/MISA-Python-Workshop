# Exercise 3: Grade Statistics

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

# Store grades
grades = []

# Get grades from user
print("Enter your grades (type 'done' when finished):")
while True:
    grade = input("Grade: ")
    if grade.lower() == 'done':
        break
    if grade in grade_points:
        grades.append(grade)
        print(f"Added: {grade}")
    else:
        print("Invalid grade!")

# Calculate statistics
if grades:
    total_points = sum(grade_points[grade] for grade in grades)
    average_points = total_points / len(grades)
    
    print(f"\n=== Grade Statistics ===")
    print(f"Number of grades: {len(grades)}")
    print(f"Total quality points: {total_points}")
    print(f"Average quality points: {average_points:.2f}")
    
    # Count grade distribution
    grade_count = {}
    for grade in grades:
        grade_count[grade] = grade_count.get(grade, 0) + 1
    
    print("\nGrade Distribution:")
    for grade, count in sorted(grade_count.items()):
        print(f"{grade}: {count} time(s)")
else:
    print("No grades entered!")
