# Exercise 3: QPI Calculation with Loops

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

# Store subject information
subjects = []

# Get number of subjects
num_subjects = int(input("How many subjects do you have? "))

# Collect subject information
for i in range(num_subjects):
    print(f"\nSubject {i+1}:")
    subject = input("Enter subject name: ")
    
    # Get grade with validation
    while True:
        grade = input("Enter grade: ")
        if grade in grade_points:
            break
        else:
            print("Invalid grade! Please enter a valid grade.")
    
    # Get credits
    while True:
        try:
            credits = int(input("Enter number of credits: "))
            if credits > 0:
                break
            else:
                print("Credits must be positive!")
        except ValueError:
            print("Please enter a valid number!")
    
    # Store subject information
    subjects.append({
        'name': subject,
        'grade': grade,
        'credits': credits,
        'points': grade_points[grade]
    })

# Calculate QPI
total_quality_points = 0
total_credits = 0

print("\n=== Grade Summary ===")
for subject in subjects:
    weighted_points = subject['points'] * subject['credits']
    total_quality_points += weighted_points
    total_credits += subject['credits']
    
    print(f"{subject['name']}: {subject['grade']} "
          f"({subject['credits']} credits, {subject['points']} points)")

# Calculate and display QPI
if total_credits > 0:
    qpi = total_quality_points / total_credits
    print(f"\n=== QPI Calculation ===")
    print(f"Total Quality Points: {total_quality_points}")
    print(f"Total Credits: {total_credits}")
    print(f"QPI: {qpi:.2f}")
    
    # Grade QPI
    if qpi >= 3.7:
        print("Excellent! Dean's List Level!")
    elif qpi >= 3.0:
        print("Good! Above Average Performance!")
    elif qpi >= 2.0:
        print("Satisfactory! Keep Improving!")
    else:
        print("Needs Improvement! Focus on Studies!")
else:
    print("No subjects entered!")
