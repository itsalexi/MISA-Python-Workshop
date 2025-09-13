# Lesson 4: Dictionaries for Grade Mapping

## Learning Objectives

- Understand what dictionaries are and how they work
- Learn how to create and use dictionaries
- Practice mapping grades to quality points using dictionaries
- Make grade-to-quality-point conversion more efficient

## What are Dictionaries?

Dictionaries are data structures that store key-value pairs. Think of them like a phone book where you look up a name (key) to find a phone number (value).

## Creating Dictionaries

```python
# Creating a dictionary
grade_points = {
    "A+": 4.0,
    "A": 4.0,
    "A-": 3.7,
    "B+": 3.3,
    "B": 3.0
}

# Empty dictionary
empty_dict = {}
```

## Accessing Dictionary Values

```python
# Get value using key
grade_points = {"A+": 4.0, "A": 4.0, "B+": 3.3}

# Access values
points = grade_points["A+"]  # Returns 4.0
points = grade_points["B+"]  # Returns 3.3
```

## Safe Dictionary Access

```python
# Using get() method (safer)
grade_points = {"A+": 4.0, "A": 4.0}

# Returns value if key exists, otherwise returns default
points = grade_points.get("A+", 0.0)  # Returns 4.0
points = grade_points.get("Z", 0.0)   # Returns 0.0 (default)
```

## Dictionary Methods

```python
grade_points = {"A+": 4.0, "A": 4.0, "B+": 3.3}

# Get all keys
keys = grade_points.keys()

# Get all values
values = grade_points.values()

# Get all key-value pairs
items = grade_points.items()

# Check if key exists
if "A+" in grade_points:
    print("A+ exists in dictionary")
```

## Exercise 1: Basic Grade Dictionary

Create `exercise1.py`:

```python
# Exercise 1: Basic Grade Dictionary

# Create a dictionary mapping grades to quality points
grade_points = {
    "A+": 4.0,
    "A": 4.0,
    "A-": 3.7,
    "B+": 3.3,
    "B": 3.0,
    "B-": 2.7,
    "C+": 2.3,
    "C": 2.0,
    "C-": 1.7,
    "D": 1.0,
    "F": 0.0
}

# Get grade from user
grade = input("Enter your grade: ")

# Look up quality points
quality_points = grade_points.get(grade, "Invalid grade")

# Display result
if quality_points != "Invalid grade":
    print(f"Grade: {grade}")
    print(f"Quality Points: {quality_points}")
else:
    print("Invalid grade entered!")
    print("Valid grades:", list(grade_points.keys()))
```

## Exercise 2: Subject Grade Dictionary

Create `exercise2.py`:

```python
# Exercise 2: Subject Grade Dictionary

# Dictionary for grade-to-quality-point mapping
grade_points = {
    "A+": 4.0, "A": 4.0, "A-": 3.7,
    "B+": 3.3, "B": 3.0, "B-": 2.7,
    "C+": 2.3, "C": 2.0, "C-": 1.7,
    "D": 1.0, "F": 0.0
}

# Dictionary to store subject grades
subject_grades = {}

# Get number of subjects
num_subjects = int(input("How many subjects do you have? "))

# Get grades for each subject
for i in range(num_subjects):
    subject = input(f"Enter subject {i+1} name: ")
    grade = input(f"Enter grade for {subject}: ")

    # Validate grade
    if grade in grade_points:
        subject_grades[subject] = grade
        print(f"Added: {subject} - {grade}")
    else:
        print(f"Invalid grade '{grade}' for {subject}")

# Display all grades
print("\n=== Your Grades ===")
for subject, grade in subject_grades.items():
    points = grade_points[grade]
    print(f"{subject}: {grade} ({points} quality points)")
```

## Exercise 3: Grade Statistics

Create `exercise3.py`:

```python
# Exercise 3: Grade Statistics

# Grade-to-quality-point mapping
grade_points = {
    "A+": 4.0, "A": 4.0, "A-": 3.7,
    "B+": 3.3, "B": 3.0, "B-": 2.7,
    "C+": 2.3, "C": 2.0, "C-": 1.7,
    "D": 1.0, "F": 0.0
}

# Store grades
grades = []

# Get grades from user
print("Enter your grades (type 'done' when finished):")
while True:
    grade = input("Grade: ")
    if grade.lower() == 'done':
        break
    if grade in grade_points:
        grades.append(grade)
        print(f"Added: {grade}")
    else:
        print("Invalid grade!")

# Calculate statistics
if grades:
    total_points = sum(grade_points[grade] for grade in grades)
    average_points = total_points / len(grades)

    print(f"\n=== Grade Statistics ===")
    print(f"Number of grades: {len(grades)}")
    print(f"Total quality points: {total_points}")
    print(f"Average quality points: {average_points:.2f}")

    # Count grade distribution
    grade_count = {}
    for grade in grades:
        grade_count[grade] = grade_count.get(grade, 0) + 1

    print("\nGrade Distribution:")
    for grade, count in sorted(grade_count.items()):
        print(f"{grade}: {count} time(s)")
else:
    print("No grades entered!")
```

## Key Concepts

1. **Key-Value Pairs**: Dictionaries store data as key-value pairs
2. **Efficient Lookup**: Much faster than long if-elif chains
3. **Flexible Keys**: Can use strings, numbers, or other types as keys
4. **Safe Access**: Use `get()` method to avoid errors
5. **Dynamic Storage**: Can add, modify, and remove entries

## Dictionary vs If-Elif Chain

**Old way (if-elif chain):**

```python
if grade == "A+":
    points = 4.0
elif grade == "A":
    points = 4.0
# ... many more elif statements
```

**New way (dictionary):**

```python
grade_points = {"A+": 4.0, "A": 4.0, ...}
points = grade_points.get(grade, 0.0)
```

## Common Dictionary Operations

```python
# Create
grades = {"Math": "A", "Science": "B+"}

# Access
math_grade = grades["Math"]

# Safe access
english_grade = grades.get("English", "Not found")

# Update
grades["Math"] = "A+"

# Add new
grades["History"] = "B"

# Remove
del grades["Science"]

# Check existence
if "Math" in grades:
    print("Math grade exists")
```

## Next Steps

Now that you can efficiently map grades to quality points using dictionaries, let's learn about loops in Lesson 5 to process multiple grades and calculate QPI!
