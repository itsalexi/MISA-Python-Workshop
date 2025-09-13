# Exercise 4: Interactive Grade Entry

# Grade-to-quality-point mapping
grade_points = {
    "A+": 4.0, "A": 4.0, "A-": 3.7,
    "B+": 3.3, "B": 3.0, "B-": 2.7,
    "C+": 2.3, "C": 2.0, "C-": 1.7,
    "D": 1.0, "F": 0.0
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
    
    # Get credits
    while True:
        try:
            credits = int(input("Credits: "))
            if credits > 0:
                break
            else:
                print("Credits must be positive!")
        except ValueError:
            print("Please enter a valid number!")
    
    # Store grade
    all_grades.append({
        'subject': subject,
        'grade': grade,
        'credits': credits,
        'points': grade_points[grade]
    })
    
    print(f"Added: {subject} - {grade} ({credits} credits)")

# Calculate and display QPI
if all_grades:
    total_points = sum(grade['points'] * grade['credits'] for grade in all_grades)
    total_credits = sum(grade['credits'] for grade in all_grades)
    qpi = total_points / total_credits
    
    print(f"\n=== Final QPI Report ===")
    print(f"Total Subjects: {len(all_grades)}")
    print(f"Total Credits: {total_credits}")
    print(f"QPI: {qpi:.2f}")
else:
    print("No grades entered!")
