# Exercise 2: Grade Input

# Get grade information from user
print("=== Grade Entry ===")

# Get subject and grade
subject = input("Enter subject name: ")
grade = input("Enter grade (A+, A, B+, B, etc.): ")

# Get number of credits
credits = int(input("Enter number of credits: "))

# Display the information
print(f"\nSubject: {subject}")
print(f"Grade: {grade}")
print(f"Credits: {credits}")
