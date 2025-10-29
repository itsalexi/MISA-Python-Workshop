# Lesson 5: Loops for Processing Multiple Grades

## Learning Objectives

- Understand for loops and while loops
- Learn how to process multiple grades efficiently
- Practice calculating QPI using loops
- Combine loops with dictionaries for grade processing

## What are Loops?

Loops allow you to repeat a block of code multiple times. This is essential for processing multiple grades in our QPI calculator.

## For Loops

For loops iterate over a sequence (like a list, string, or range):

```python
# Basic for loop
for i in range(5):
    print(f"Number: {i}")

# Loop through a list
grades = ["A", "B+", "A-", "B"]
for grade in grades:
    print(f"Grade: {grade}")
```

## While Loops

While loops continue as long as a condition is true:

```python
# Basic while loop
count = 0
while count < 5:
    print(f"Count: {count}")
    count += 1

# While loop with user input
grades = []
while True:
    grade = input("Enter grade (or 'done' to finish): ")
    if grade.lower() == 'done':
        break
    grades.append(grade)
```

## Range Function

The `range()` function creates a sequence of numbers:

```python
# range(stop)
for i in range(5):  # 0, 1, 2, 3, 4
    print(i)

# range(start, stop)
for i in range(1, 6):  # 1, 2, 3, 4, 5
    print(i)

# range(start, stop, step)
for i in range(0, 10, 2):  # 0, 2, 4, 6, 8
    print(i)
```

## Exercise 1: Basic Loop Practice

Create `exercise1.py`:

```python
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
```

## Exercise 2: Grade Input with Validation

Create `exercise2.py`:

```python
# Exercise 2: Grade Input with Validation

# Valid grades
valid_grades = ["A", "B+", "B", "C+", "C", "D", "F"]

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

# Get number of subjects
num_subjects = int(input("How many subjects do you have? "))

# Collect grades with validation
subject_grades = {}
for i in range(num_subjects):
    subject = input(f"\nEnter subject {i+1} name: ")

    # Keep asking until valid grade is entered
    while True:
        grade = input(f"Enter grade for {subject}: ")
        if grade in valid_grades:
            subject_grades[subject] = grade
            break
        else:
            print("Invalid grade! Valid grades are:", ", ".join(valid_grades))

# Display results
print("\n=== Your Grades ===")
total_points = 0
for subject, grade in subject_grades.items():
    points = grade_points[grade]
    total_points += points
    print(f"{subject}: {grade} ({points} quality points)")

print(f"\nTotal Quality Points: {total_points}")
```

## Exercise 3: QPI Calculation with Loops

Create `exercise3.py`:

```python
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

    # Get units
    while True:
        try:
            units = int(input("Enter number of units: "))
            if units > 0:
                break
            else:
                print("Units must be positive!")
        except ValueError:
            print("Please enter a valid number!")

    # Store subject information
    subjects.append({
        'name': subject,
        'grade': grade,
        'units': units,
        'points': grade_points[grade]
    })

# Calculate QPI
total_quality_points = 0
total_units = 0

print("\n=== Grade Summary ===")
for subject in subjects:
    weighted_points = subject['points'] * subject['units']
    total_quality_points += weighted_points
    total_units += subject['units']

    print(f"{subject['name']}: {subject['grade']} "
          f"({subject['units']} units, {subject['points']} points)")

# Calculate and display QPI
if total_units > 0:
    qpi = total_quality_points / total_units
    print(f"\n=== QPI Calculation ===")
    print(f"Total Quality Points: {total_quality_points}")
    print(f"Total Units: {total_units}")
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
```

## Exercise 4: Interactive Grade Entry

Create `exercise4.py`:

```python
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
```

## Key Concepts

1. **For Loops**: Use when you know how many times to repeat
2. **While Loops**: Use when you don't know how many times to repeat
3. **Range Function**: Creates sequences for counting
4. **Enumerate**: Get both index and value in loops
5. **Break Statement**: Exit loops early
6. **Validation**: Always validate user input in loops

## Loop Control

```python
# Break - exit loop early
for i in range(10):
    if i == 5:
        break
    print(i)

# Continue - skip current iteration
for i in range(10):
    if i % 2 == 0:
        continue
    print(i)  # Only prints odd numbers
```

## Common Loop Patterns

```python
# Pattern 1: Process each item in a list
for item in my_list:
    print(item)

# Pattern 2: Count with index
for i, item in enumerate(my_list):
    print(f"{i}: {item}")

# Pattern 3: Process a specific number of times
for i in range(num_times):
    print(f"Processing {i}")

# Pattern 4: Continue until condition is met
while condition:
    # do something
    pass
```

## Next Steps

Now that you can process multiple grades with loops, let's combine everything in Lesson 6 to build the complete QPI calculator!
