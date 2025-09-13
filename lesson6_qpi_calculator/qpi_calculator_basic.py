# Basic QPI Calculator

def main():
    print("=== QPI Calculator ===")
    
    # Student information
    student_name = input("Enter student name: ")
    
    # Grade-to-quality-point mapping
    grade_points = {
        "A+": 4.0, "A": 4.0, "A-": 3.7,
        "B+": 3.3, "B": 3.0, "B-": 2.7,
        "C+": 2.3, "C": 2.0, "C-": 1.7,
        "D": 1.0, "F": 0.0
    }
    
    # Get number of subjects
    num_subjects = int(input("How many subjects? "))
    
    # Collect grades
    subjects = []
    for i in range(num_subjects):
        print(f"\nSubject {i+1}:")
        subject = input("Subject name: ")
        grade = input("Grade: ")
        credits = int(input("Credits: "))
        
        subjects.append({
            'name': subject,
            'grade': grade,
            'credits': credits,
            'points': grade_points.get(grade, 0.0)
        })
    
    # Calculate QPI
    total_points = sum(sub['points'] * sub['credits'] for sub in subjects)
    total_credits = sum(sub['credits'] for sub in subjects)
    qpi = total_points / total_credits
    
    # Display results
    print(f"\n=== QPI Report for {student_name} ===")
    for sub in subjects:
        print(f"{sub['name']}: {sub['grade']} ({sub['credits']} credits)")
    print(f"\nQPI: {qpi:.2f}")

if __name__ == "__main__":
    main()
