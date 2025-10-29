# Lesson 6 Exercise

## Complete QPI Calculator

**File:** `qpi_calculator_complete.py`

**Objective:** Build a complete QPI calculator combining all concepts learned

**Instructions:**

This is your final project! Follow the step-by-step structure to build a complete QPI calculator.

### Step 1: Setup and Student Information
- Print welcome messages
- Get student name from user

### Step 2: Grade Mapping Dictionary
- Create the grade_points dictionary
- Display the grade mapping to the user

### Step 3: Collect Number of Subjects
- Get how many subjects the student has

### Step 4: Collect Grade Data
- Create empty subjects list
- Loop through each subject:
  - Get subject name, grade, and units
  - Store in a dictionary with keys: 'name', 'grade', 'units', 'points'
  - Append to subjects list
  - Print confirmation

### Step 5: Calculate QPI
- Initialize total_quality_points and total_units to 0
- Loop through all subjects:
  - Calculate weighted points for each subject
  - Add to totals
  - Print grade summary
- Calculate QPI = total_quality_points / total_units

### Step 6: Display Results
- Print student name
- Print total quality points
- Print total units
- Print QPI (formatted to 2 decimal places)
- Determine and print academic standing:
  - >= 3.7: "EXCELLENT - Dean's List Level!"
  - >= 3.0: "GOOD - Above Average Performance!"
  - >= 2.0: "SATISFACTORY - Keep Improving!"
  - else: "NEEDS IMPROVEMENT - Focus on Studies!"

**Expected Output:**
```
=== Complete QPI Calculator ===
Let's build a QPI calculator step by step!

--- Step 1: Getting Student Information ---
Enter student name: Juan Dela Cruz

--- Step 2: Grade to Quality Points Mapping ---
Grade mapping:
  A: 4.0
  B+: 3.5
  B: 3.0
  C+: 2.5
  C: 2.0
  D: 1.0
  F: 0.0

--- Step 3: Collecting Grades ---
How many subjects do you have? 3

Subject 1:
Subject name: Math
Grade: A
Number of units: 3
Added: Math - A (3 units)

Subject 2:
Subject name: English
Grade: B+
Number of units: 3
Added: English - B+ (3 units)

Subject 3:
Subject name: Science
Grade: B
Number of units: 2
Added: Science - B (2 units)

--- Step 4: Calculating QPI ---

Grade Summary:
Math: A (3 units, 4.0 points)
English: B+ (3 units, 3.5 points)
Science: B (2 units, 3.0 points)

--- Final Results ---
Student: Juan Dela Cruz
Total Quality Points: 29.5
Total Units: 8
QPI: 3.69

Academic Standing: EXCELLENT - Dean's List Level!
```

## Tips

- Follow the step-by-step structure in the comments
- Test your calculator with the sample data above
- Make sure your output matches the expected format
- Check `answers/qpi_calculator_complete.py` if you get stuck

## Concepts Used

This project combines:
- ✅ Variables
- ✅ User Input
- ✅ Conditionals (if/elif/else)
- ✅ Loops (for)
- ✅ Dictionaries
- ✅ Lists
- ✅ Calculations
- ✅ String Formatting

Congratulations on completing the Python workshop! 🎉
