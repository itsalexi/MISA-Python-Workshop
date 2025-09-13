# Advanced QPI Calculator with Error Handling

def get_valid_grade():
    """Get a valid grade from user with error handling"""
    valid_grades = ["A+", "A", "A-", "B+", "B", "B-", "C+", "C", "C-", "D", "F"]
    
    while True:
        grade = input("Grade: ").upper()
        if grade in valid_grades:
            return grade
        else:
            print("Invalid grade! Valid grades:", ", ".join(valid_grades))

def get_valid_credits():
    """Get valid credits from user with error handling"""
    while True:
        try:
            credits = int(input("Credits: "))
            if credits > 0:
                return credits
            else:
                print("Credits must be positive!")
        except ValueError:
            print("Please enter a valid number!")

def calculate_qpi(subjects):
    """Calculate QPI from list of subjects"""
    if not subjects:
        return 0.0
    
    total_points = sum(sub['points'] * sub['credits'] for sub in subjects)
    total_credits = sum(sub['credits'] for sub in subjects)
    
    return total_points / total_credits if total_credits > 0 else 0.0

def get_grade_level(qpi):
    """Determine grade level based on QPI"""
    if qpi >= 3.7:
        return "Excellent - Dean's List Level!"
    elif qpi >= 3.0:
        return "Good - Above Average!"
    elif qpi >= 2.0:
        return "Satisfactory - Keep Improving!"
    else:
        return "Needs Improvement - Focus on Studies!"

def main():
    print("=== Advanced QPI Calculator ===")
    
    # Grade-to-quality-point mapping
    grade_points = {
        "A+": 4.0, "A": 4.0, "A-": 3.7,
        "B+": 3.3, "B": 3.0, "B-": 2.7,
        "C+": 2.3, "C": 2.0, "C-": 1.7,
        "D": 1.0, "F": 0.0
    }
    
    # Student information
    student_name = input("Enter student name: ")
    course = input("Enter course/program: ")
    
    # Get number of subjects
    while True:
        try:
            num_subjects = int(input("How many subjects? "))
            if num_subjects > 0:
                break
            else:
                print("Number of subjects must be positive!")
        except ValueError:
            print("Please enter a valid number!")
    
    # Collect grades
    subjects = []
    print(f"\nEnter grades for {num_subjects} subjects:")
    
    for i in range(num_subjects):
        print(f"\nSubject {i+1}:")
        subject = input("Subject name: ")
        grade = get_valid_grade()
        credits = get_valid_credits()
        
        subjects.append({
            'name': subject,
            'grade': grade,
            'credits': credits,
            'points': grade_points[grade]
        })
        
        print(f"✓ Added: {subject} - {grade} ({credits} credits)")
    
    # Calculate QPI
    qpi = calculate_qpi(subjects)
    
    # Display comprehensive report
    print(f"\n{'='*50}")
    print(f"QPI REPORT FOR {student_name.upper()}")
    print(f"Course: {course}")
    print(f"{'='*50}")
    
    print(f"\n{'Subject':<20} {'Grade':<6} {'Credits':<8} {'Points':<6}")
    print("-" * 50)
    
    total_credits = 0
    total_weighted_points = 0
    
    for sub in subjects:
        weighted_points = sub['points'] * sub['credits']
        total_weighted_points += weighted_points
        total_credits += sub['credits']
        
        print(f"{sub['name']:<20} {sub['grade']:<6} {sub['credits']:<8} {sub['points']:<6}")
    
    print("-" * 50)
    print(f"{'TOTALS':<20} {'':<6} {total_credits:<8} {total_weighted_points:<6}")
    
    print(f"\nQPI Calculation:")
    print(f"Total Weighted Points: {total_weighted_points}")
    print(f"Total Credits: {total_credits}")
    print(f"QPI: {qpi:.2f}")
    print(f"Grade Level: {get_grade_level(qpi)}")
    
    # Grade distribution
    grade_count = {}
    for sub in subjects:
        grade = sub['grade']
        grade_count[grade] = grade_count.get(grade, 0) + 1
    
    print(f"\nGrade Distribution:")
    for grade, count in sorted(grade_count.items()):
        print(f"{grade}: {count} subject(s)")

if __name__ == "__main__":
    main()
