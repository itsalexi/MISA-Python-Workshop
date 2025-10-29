# Lesson 5 Exercises

## Exercise 2: Grade Input with Validation

**File:** `exercise2.py`

**Objective:** Use loops to validate input and collect multiple grades

**Instructions:**
1. Create a list of valid grades and the grade_points dictionary
2. Get number of subjects from user
3. Create an empty dictionary called `subject_grades`
4. Use a `for` loop to collect grades for each subject:
   - Get subject name
   - Use a `while` loop to keep asking for grade until valid
   - Get units
   - Store in dictionary with subject name as key
5. Print all collected grades

**Expected Output:**
```
How many subjects do you have? 2

Subject 1:
Enter subject name: Math
Enter grade: A
Enter units: 3

Subject 2:
Enter subject name: English
Enter grade: X
Invalid grade! Please enter a valid grade.
Enter grade: B+
Enter units: 3

Collected Grades:
Math: A (3 units) - 4.0 points
English: B+ (3 units) - 3.5 points
```

---

## Exercise 3: QPI Calculation with Loops

**File:** `exercise3.py`

**Objective:** Calculate QPI using loops and lists

**Instructions:**
1. Create grade_points dictionary and empty subjects list
2. Get number of subjects from user
3. Loop to collect subject information with validation:
   - Get subject name
   - Validate grade (while loop)
   - Validate units (while loop, must be positive integer)
   - Append dictionary to subjects list
4. Calculate QPI:
   - Initialize totals to 0
   - Loop through subjects
   - Calculate weighted points for each
   - Compute final QPI
5. Print grade summary and QPI
6. Print academic standing based on QPI

**Expected Output:**
```
How many subjects do you have? 3

Subject 1:
Enter subject name: Math
Enter grade: A
Enter number of units: 3

Subject 2:
Enter subject name: English
Enter grade: B+
Enter number of units: 3

Subject 3:
Enter subject name: Science
Enter grade: B
Enter number of units: 2

=== Grade Summary ===
Math: A (3 units, 4.0 points)
English: B+ (3 units, 3.5 points)
Science: B (2 units, 3.0 points)

=== QPI Calculation ===
Total Quality Points: 29.5
Total Units: 8
QPI: 3.69

Excellent! Dean's List Level!
```

---

## Exercise 4: Interactive Grade Entry

**File:** `exercise4.py`

**Objective:** Create an interactive system using while loops

**Instructions:**
1. Create grade_points dictionary and empty all_grades list
2. Print instructions (enter 'done' to finish)
3. Use infinite `while` loop for interactive entry:
   - Print current entry number
   - Get subject name
   - If 'done', break the loop
   - Validate grade (while loop)
   - Validate units (while loop)
   - Append to list
   - Print confirmation
4. Calculate and display QPI if grades were entered

**Expected Output:**
```
=== Interactive Grade Entry ===
Enter 'done' to finish entering grades

Grade Entry #1
Subject name: Math
Grade: A
Units: 3
Added: Math - A (3 units)

Grade Entry #2
Subject name: English
Grade: B+
Units: 3
Added: English - B+ (3 units)

Grade Entry #3
Subject name: done

=== Final QPI Report ===
Total Subjects: 2
Total Units: 6
QPI: 3.75
```
