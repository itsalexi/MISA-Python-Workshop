# Exercise 1: Basic Loop Practice

# Get number of subjects
num_subjects = int(input("How many subjects do you have? "))

# Use for loop to get grades
grades = []
for i in range(num_subjects):
    grade = input(f"Enter grade for subject {i+1}: ")
    grades.append(grade)

# Display all grades
print("\n=== Your Grades ===")
for i, grade in enumerate(grades, 1):
    print(f"Subject {i}: {grade}")
