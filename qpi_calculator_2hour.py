"""
2-Hour Workshop QPI Calculator
Simplified version for teaching Python fundamentals
"""

print("=== 2-Hour Workshop QPI Calculator ===")
print("Let's build a QPI calculator step by step!")

# Step 1: Variables and Input
print("\n--- Step 1: Getting Student Information ---")
student_name = input("Enter student name: ")

# Step 2: Dictionary for Grade Mapping
print("\n--- Step 2: Grade to Quality Points Mapping ---")
grade_points = {
    "A+": 4.0, "A": 4.0, "A-": 3.7,
    "B+": 3.3, "B": 3.0, "B-": 2.7,
    "C+": 2.3, "C": 2.0, "C-": 1.7,
    "D": 1.0, "F": 0.0
}

print("Grade mapping:")
for grade, points in grade_points.items():
    print(f"  {grade}: {points}")

# Step 3: Get Number of Subjects
print("\n--- Step 3: Collecting Grades ---")
num_subjects = int(input("How many subjects do you have? "))

# Step 4: Collect Grades Using Loops
subjects = []
for i in range(num_subjects):
    print(f"\nSubject {i+1}:")
    subject = input("Subject name: ")
    grade = input("Grade: ")
    credits = int(input("Number of credits: "))
    
    # Store subject information
    subjects.append({
        'name': subject,
        'grade': grade,
        'credits': credits,
        'points': grade_points[grade]
    })
    
    print(f"Added: {subject} - {grade} ({credits} credits)")

# Step 5: Calculate QPI
print("\n--- Step 4: Calculating QPI ---")

# Calculate totals
total_quality_points = 0
total_credits = 0

print("\nGrade Summary:")
for sub in subjects:
    weighted_points = sub['points'] * sub['credits']
    total_quality_points += weighted_points
    total_credits += sub['credits']
    
    print(f"{sub['name']}: {sub['grade']} ({sub['credits']} credits, {sub['points']} points)")

# Calculate QPI
qpi = total_quality_points / total_credits

# Step 6: Display Results
print("\n--- Final Results ---")
print(f"Student: {student_name}")
print(f"Total Quality Points: {total_quality_points}")
print(f"Total Credits: {total_credits}")
print(f"QPI: {qpi}")

# Academic standing
if qpi >= 3.7:
    standing = "EXCELLENT - Dean's List Level!"
elif qpi >= 3.0:
    standing = "GOOD - Above Average Performance!"
elif qpi >= 2.0:
    standing = "SATISFACTORY - Keep Improving!"
else:
    standing = "NEEDS IMPROVEMENT - Focus on Studies!"

print(f"Academic Standing: {standing}")
