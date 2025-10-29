# Exercise 3: Multiple Grade Input

print("=== Grade Entry System ===")

# Get number of subjects
num_subjects = int(input("How many subjects do you have? "))

# Initialize variables
total_units = 0

# Loop to get each subject's information
for i in range(num_subjects):
    print(f"\nSubject {i+1}:")
    subject = input("Enter subject name: ")
    grade = input("Enter grade: ")
    units = int(input("Enter units: "))
    
    total_units += units
    
    print(f"Added: {subject} - {grade} ({units} units)")

print(f"\nTotal units: {total_units}")
