# Exercise 4: Interactive Grade Entry

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

# Store all grades
all_grades = []

# Interactive grade entry
print("=== Interactive Grade Entry ===")
print("Enter 'done' to finish entering grades")

while True:
    print(f"\nGrade Entry #{len(all_grades) + 1}")
    subject = input("Subject name: ")
    
    if subject.lower() == 'done':
        break
    
    # Get grade
    while True:
        grade = input("Grade: ")
        if grade in grade_points:
            break
        else:
            print("Invalid grade!")
    
    # Get units
    while True:
        try:
            units = int(input("Units: "))
            if units > 0:
                break
            else:
                print("Units must be positive!")
        except ValueError:
            print("Please enter a valid number!")
    
    # Store grade
    all_grades.append({
        'subject': subject,
        'grade': grade,
        'units': units,
        'points': grade_points[grade]
    })
    
    print(f"Added: {subject} - {grade} ({units} units)")

# Calculate and display QPI
if all_grades:
    total_points = sum(grade['points'] * grade['units'] for grade in all_grades)
    total_units = sum(grade['units'] for grade in all_grades)
    qpi = total_points / total_units
    
    print(f"\n=== Final QPI Report ===")
    print(f"Total Subjects: {len(all_grades)}")
    print(f"Total Units: {total_units}")
    print(f"QPI: {qpi:.2f}")
else:
    print("No grades entered!")
