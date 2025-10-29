# Lesson 2 Exercises

## Exercise 1: Basic Input Practice

**File:** `exercise1.py`

**Objective:** Practice getting user input and displaying it

**Instructions:**
1. Print a header "=== Student Information ==="
2. Get student name from user using `input()`
3. Get age from user and convert to integer using `int()`
4. Get course from user
5. Display all the information in a formatted way

**Expected Output:**
```
=== Student Information ===
Enter student name: Juan Dela Cruz
Enter age: 20
Enter course: Computer Science

Student Information:
Name: Juan Dela Cruz
Age: 20
Course: Computer Science
```

---

## Exercise 2: Grade Input

**File:** `exercise2.py`

**Objective:** Get grade information from user

**Instructions:**
1. Print header "=== Grade Entry ==="
2. Get subject name from user
3. Get grade from user
4. Get number of units from user (convert to integer)
5. Display the subject, grade, and units

**Expected Output:**
```
=== Grade Entry ===
Enter subject name: Mathematics
Enter grade (A+, A, B+, B, etc.): A
Enter number of units: 3

Subject: Mathematics
Grade: A
Units: 3
```

---

## Exercise 3: Multiple Grade Input

**File:** `exercise3.py`

**Objective:** Use loops to collect multiple grades

**Instructions:**
1. Print header "=== Grade Entry System ==="
2. Get number of subjects from user
3. Initialize a variable to track total units
4. Use a `for` loop to collect information for each subject:
   - Print which subject number
   - Get subject name, grade, and units
   - Add units to total
   - Print confirmation message
5. Print the total units

**Expected Output:**
```
=== Grade Entry System ===
How many subjects do you have? 3

Subject 1:
Enter subject name: Math
Enter grade: A
Enter units: 3
Added: Math - A (3 units)

Subject 2:
Enter subject name: English
Enter grade: B+
Enter units: 3
Added: English - B+ (3 units)

Subject 3:
Enter subject name: Science
Enter grade: B
Enter units: 2
Added: Science - B (2 units)

Total units: 8
```
