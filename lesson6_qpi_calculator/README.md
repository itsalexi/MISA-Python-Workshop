# Lesson 6: Complete QPI Calculator

## Learning Objectives

- Combine all Python concepts learned in previous lessons
- Build a complete, user-friendly QPI calculator
- Practice implementing a real-world application step by step
- Create a polished program with clear output

## Project Overview

In this final lesson, you'll build a complete QPI calculator by combining everything you've learned. We'll build it step by step, adding one feature at a time.

## QPI Formula

QPI = (Sum of (Grade Points × Credits)) / Total Credits

Where:
- Grade Points: A = 4.0, B+ = 3.5, B = 3.0, C+ = 2.5, C = 2.0, D = 1.0, F = 0.0
- Credits: Number of credit hours for each subject

## Building the Calculator Step by Step

Create `qpi_calculator_complete.py` and follow along!

### Part 1: Setup and Student Information

Start with the basic structure and get student information:

```python
"""
Complete QPI Calculator
Combines all Python concepts learned in previous lessons
"""

print("=== Complete QPI Calculator ===")
print("Let's build a QPI calculator step by step!")

# Step 1: Variables and Input
print("\n--- Step 1: Getting Student Information ---")
student_name = input("Enter student name: ")
```

**Concepts used:** Variables, user input, string formatting

---

### Part 2: Grade Mapping Dictionary

Add the grade-to-quality-point mapping:

```python
# Step 2: Dictionary for Grade Mapping
print("\n--- Step 2: Grade to Quality Points Mapping ---")
grade_points = {
    "A": 4.0,
    "B+": 3.5,
    "B": 3.0,
    "C+": 2.5,
    "C": 2.0,
    "D": 1.0,
    "F": 0.0
}

print("Grade mapping:")
for grade, points in grade_points.items():
    print(f"  {grade}: {points}")
```

**Concepts used:** Dictionaries, loops (for iterating through dictionary)

---

### Part 3: Collecting Subject Data

Get the number of subjects and prepare to collect data:

```python
# Step 3: Get Number of Subjects
print("\n--- Step 3: Collecting Grades ---")
num_subjects = int(input("How many subjects do you have? "))

# Step 4: Collect Grades Using Loops
subjects = []
```

**Concepts used:** Type conversion (int), lists

---

### Part 4: Loop to Collect Multiple Subjects

Use a loop to collect information for each subject:

```python
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
```

**Concepts used:** For loops, range(), dictionaries (nested), list append, dictionary lookup

---

### Part 5: Calculate QPI

Calculate the weighted average:

```python
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
```

**Concepts used:** Loops (iterating through list), calculations, accumulator pattern

---

### Part 6: Display Results and Academic Standing

Show the final results and determine academic standing:

```python
# Step 6: Display Results
print("\n--- Final Results ---")
print(f"Student: {student_name}")
print(f"Total Quality Points: {total_quality_points}")
print(f"Total Credits: {total_credits}")
print(f"QPI: {qpi:.2f}")

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
```

**Concepts used:** Conditional statements (if/elif/else), string formatting

---

## Complete Code

Here's the complete program with all parts combined:

```python
"""
Complete QPI Calculator
Combines all Python concepts learned in previous lessons
"""

print("=== Complete QPI Calculator ===")
print("Let's build a QPI calculator step by step!")

# Step 1: Variables and Input
print("\n--- Step 1: Getting Student Information ---")
student_name = input("Enter student name: ")

# Step 2: Dictionary for Grade Mapping
print("\n--- Step 2: Grade to Quality Points Mapping ---")
grade_points = {
    "A": 4.0,
    "B+": 3.5,
    "B": 3.0,
    "C+": 2.5,
    "C": 2.0,
    "D": 1.0,
    "F": 0.0
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
print(f"QPI: {qpi:.2f}")

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
```

## Congratulations! 🎉

You've successfully built a complete QPI calculator! This project demonstrates how different Python concepts work together to create a useful, real-world application.

Great job completing the Python workshop! 🐍
