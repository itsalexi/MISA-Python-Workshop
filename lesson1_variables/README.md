# Lesson 1: Variables and Data Storage

## Learning Objectives

- Understand what variables are in Python
- Learn different data types (strings, numbers, booleans)
- Practice storing and manipulating data

## What are Variables?

Variables are like containers that store information in your computer's memory. Think of them as labeled boxes where you can put different types of data.

## Creating Variables

In Python, you create a variable by giving it a name and assigning a value using the `=` sign:

```python
# Creating variables
student_name = "Juan"
age = 20
is_enrolled = True
gpa = 3.5
```

## Data Types in Python

Python has several built-in data types:

### 1. Strings (Text)

Strings are sequences of characters enclosed in quotes:

```python
# String examples
name = "Maria"
course = 'Computer Science'
grade = "A+"
```

### 2. Numbers

Python has two main number types:

**Integers** (whole numbers):

```python
age = 19
credits = 3
semester = 2
```

**Floats** (decimal numbers):

```python
gpa = 3.75
percentage = 87.5
average = 85.2
```

### 3. Booleans (True/False)

```python
is_passing = True
is_failing = False
```

## Exercise 1: Variable Practice

Create a Python file called `exercise1.py` and practice creating variables:

```python
# TODO: Create variables for student information
# 1. Create a variable for student name
# 2. Create a variable for student age
# 3. Create a variable for number of subjects
# 4. Create a variable for average grade
# 5. Create a variable for whether student is graduating

# Print all variables to see their values
print("Student Name:", student_name)
print("Age:", age)
print("Number of subjects:", num_subjects)
print("Average grade:", average_grade)
print("Is graduating:", is_graduating)
```

## Exercise 2: Grade Variables

In `exercise2.py`, create variables to store grade information:

```python
# TODO: Create variables for different grades
# Store different letter grades as strings
# Store their corresponding quality points as numbers

# Example:
math_grade = "A+"
math_quality_points = 4.0

# Create more grade variables here...

# Print the information
print("Math Grade:", math_grade, "Quality Points:", math_quality_points)
```

## Key Concepts

1. **Variable Naming**: Use descriptive names that explain what the variable stores
2. **Assignment**: Use `=` to assign values to variables
3. **Data Types**: Python automatically determines the data type based on the value
4. **Case Sensitivity**: Variable names are case-sensitive (`Name` is different from `name`)

## Next Steps

Once you're comfortable with variables, move on to Lesson 2 where you'll learn how to get input from users!
