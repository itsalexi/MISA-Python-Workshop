# Lesson 3 Exercises

## Exercise 1: Grade Categorization

**File:** `exercise1.py`

**Objective:** Use if/elif/else statements to categorize grades

**Instructions:**
1. Get a grade from the user
2. Use if/elif/else to print different messages based on the grade:
   - A: "Outstanding! Excellent performance!"
   - B+: "Very Good! Above average performance!"
   - B: "Good! Satisfactory performance!"
   - C+: "Fair! Room for improvement!"
   - C: "Passing! Work harder next time!"
   - D: "Poor! Must improve significantly!"
   - F: "Failed! Must retake the course!"
   - Anything else: "Invalid grade entered!"

**Expected Output:**
```
Enter your grade (A, B+, B, C+, C, etc.): A
Outstanding! Excellent performance!
```

---

## Exercise 2: Quality Points Assignment

**File:** `exercise2.py`

**Objective:** Assign quality points based on grades using conditionals

**Instructions:**
1. Get a grade from the user
2. Use if/elif/else to assign quality points:
   - A: 4.0
   - B+: 3.5
   - B: 3.0
   - C+: 2.5
   - C: 2.0
   - D: 1.0
   - F: 0.0
   - Invalid: Set to None and print error
3. Display the grade and quality points (only if valid)

**Expected Output:**
```
Enter your grade (A, B+, B, C+, C, etc.): B+

Grade: B+
Quality Points: 3.5
```

---

## Exercise 3: Grade Validation

**File:** `exercise3.py`

**Objective:** Validate user input against a list of valid grades

**Instructions:**
1. Get a grade from the user
2. Create a list of valid grades: `["A", "B+", "B", "C+", "C", "D", "F"]`
3. Check if the grade is in the valid list using `in` operator
4. If valid:
   - Assign quality points using if/elif/else
   - Print the grade and quality points
5. If invalid:
   - Print error message
   - Print the list of valid grades

**Expected Output (Valid):**
```
Enter your grade: A

Valid grade: A
Quality Points: 4.0
```

**Expected Output (Invalid):**
```
Enter your grade: A+

Invalid grade! Please enter a valid grade.
Valid grades are: A, B+, B, C+, C, D, F
```
