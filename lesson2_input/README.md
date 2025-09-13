# Lesson 2: Getting User Input

## Learning Objectives

- Learn how to use the `input()` function
- Understand how to convert input to different data types
- Practice getting user input for our QPI calculator

## The `input()` Function

The `input()` function allows your program to get information from the user. When the program runs, it will pause and wait for the user to type something and press Enter.

## Basic Input

```python
# Get text input from user
name = input("Enter your name: ")
print("Hello,", name)
```

## Converting Input to Numbers

By default, `input()` returns a string (text). If you need numbers, you must convert them:

```python
# Converting to integer
age = int(input("Enter your age: "))

# Converting to float (decimal number)
gpa = float(input("Enter your GPA: "))

# Converting to string (this is automatic)
name = input("Enter your name: ")
```

## Important: Input Validation

When converting input, always handle potential errors:

```python
# Safe way to get a number
try:
    age = int(input("Enter your age: "))
    print("You are", age, "years old")
except ValueError:
    print("Please enter a valid number")
```

## Exercise 1: Basic Input Practice

Create `exercise1.py`:

```python
# Exercise 1: Basic Input Practice

# Get student information from user
print("=== Student Information ===")
student_name = input("Enter student name: ")
age = int(input("Enter age: "))
course = input("Enter course: ")

# Display the information
print("\nStudent Information:")
print("Name:", student_name)
print("Age:", age)
print("Course:", course)
```

## Exercise 2: Grade Input

Create `exercise2.py`:

```python
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
```

## Exercise 3: Multiple Grade Input

Create `exercise3.py`:

```python
# Exercise 3: Multiple Grade Input

print("=== Grade Entry System ===")

# Get number of subjects
num_subjects = int(input("How many subjects do you have? "))

# Initialize variables
total_credits = 0

# Loop to get each subject's information
for i in range(num_subjects):
    print(f"\nSubject {i+1}:")
    subject = input("Enter subject name: ")
    grade = input("Enter grade: ")
    credits = int(input("Enter credits: "))

    total_credits += credits

    print(f"Added: {subject} - {grade} ({credits} credits)")

print(f"\nTotal credits: {total_credits}")
```

## Key Concepts

1. **`input()` function**: Gets text from user
2. **Type conversion**: Convert strings to numbers with `int()` and `float()`
3. **Error handling**: Use `try/except` for safe input conversion
4. **User prompts**: Always provide clear instructions to users

## Common Input Patterns

```python
# Pattern 1: Simple text input
name = input("Enter name: ")

# Pattern 2: Number input with conversion
age = int(input("Enter age: "))

# Pattern 3: Safe number input
while True:
    try:
        grade = float(input("Enter grade: "))
        break
    except ValueError:
        print("Please enter a valid number")
```

## Next Steps

Now that you can get input from users, let's learn about conditional statements in Lesson 3 to categorize grades!
