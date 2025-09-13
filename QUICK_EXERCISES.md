# Quick Exercises for 2-Hour Workshop

## Exercise 1: Variables and Input (5 minutes)

```python
# Create these variables
student_name = "Juan Dela Cruz"
age = 20
course = "Computer Science"

# Get input from user
new_name = input("Enter your name: ")
print(f"Hello, {new_name}!")
```

## Exercise 2: Conditional Statements (10 minutes)

```python
# Get a grade from user and assign quality points
grade = input("Enter your grade: ")

if grade == "A+":
    quality_points = 4.0
elif grade == "A":
    quality_points = 4.0
elif grade == "A-":
    quality_points = 3.7
elif grade == "B+":
    quality_points = 3.3
elif grade == "B":
    quality_points = 3.0
else:
    quality_points = 0.0

print(f"Grade: {grade}, Quality Points: {quality_points}")
```

## Exercise 3: Dictionary (10 minutes)

```python
# Create grade dictionary
grade_points = {
    "A+": 4.0, "A": 4.0, "A-": 3.7,
    "B+": 3.3, "B": 3.0, "B-": 2.7,
    "C+": 2.3, "C": 2.0, "C-": 1.7,
    "D": 1.0, "F": 0.0
}

# Get grade and look up points
grade = input("Enter grade: ")
points = grade_points.get(grade, "Invalid grade")
print(f"Quality Points: {points}")
```

## Exercise 4: Loop with Multiple Grades (15 minutes)

```python
# Get number of subjects
num_subjects = int(input("How many subjects? "))

# Collect grades
subjects = []
for i in range(num_subjects):
    subject = input(f"Subject {i+1}: ")
    grade = input("Grade: ")
    credits = int(input("Credits: "))

    subjects.append({
        'name': subject,
        'grade': grade,
        'credits': credits
    })

# Display all grades
print("\nYour Grades:")
for sub in subjects:
    print(f"{sub['name']}: {sub['grade']} ({sub['credits']} credits)")
```

## Exercise 5: Complete QPI Calculator (20 minutes)

```python
# Complete QPI Calculator
grade_points = {
    "A+": 4.0, "A": 4.0, "A-": 3.7,
    "B+": 3.3, "B": 3.0, "B-": 2.7,
    "C+": 2.3, "C": 2.0, "C-": 1.7,
    "D": 1.0, "F": 0.0
}

# Student info
name = input("Student name: ")
num_subjects = int(input("How many subjects? "))

# Collect grades
subjects = []
for i in range(num_subjects):
    print(f"\nSubject {i+1}:")
    subject = input("Subject: ")
    grade = input("Grade: ")
    credits = int(input("Credits: "))

    subjects.append({
        'name': subject,
        'grade': grade,
        'credits': credits,
        'points': grade_points[grade]
    })

# Calculate QPI
total_points = 0
total_credits = 0

for sub in subjects:
    weighted = sub['points'] * sub['credits']
    total_points += weighted
    total_credits += sub['credits']

qpi = total_points / total_credits

# Display results
print(f"\nQPI Report for {name}:")
for sub in subjects:
    print(f"{sub['name']}: {sub['grade']} ({sub['credits']} credits)")
print(f"QPI: {qpi:.2f}")
```

## Sample Test Data

Use this data to test the calculator:

**Student:** Juan Dela Cruz  
**Subjects:**

- Mathematics: A+ (3 credits)
- Physics: B+ (3 credits)
- Programming: A (3 credits)
- English: B (3 credits)
- History: A- (2 credits)

**Expected QPI:** 3.64

**Calculation:**

- Math: 4.0 × 3 = 12.0
- Physics: 3.3 × 3 = 9.9
- Programming: 4.0 × 3 = 12.0
- English: 3.0 × 3 = 9.0
- History: 3.7 × 2 = 7.4
- Total: 50.3 ÷ 14 = 3.593 ≈ 3.59
