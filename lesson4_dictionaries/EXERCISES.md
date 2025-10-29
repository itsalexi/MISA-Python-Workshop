# Lesson 4 Exercises

## Exercise 1: Basic Grade Dictionary

**File:** `exercise1.py`

**Objective:** Create and use a dictionary to map grades to quality points

**Instructions:**
1. Create a dictionary called `grade_points` with these mappings:
   - A: 4.0, B+: 3.5, B: 3.0, C+: 2.5, C: 2.0, D: 1.0, F: 0.0
2. Get a grade from the user
3. Look up the quality points in the dictionary
4. Print the grade and its quality points

**Expected Output:**
```
Enter grade: B+
Grade: B+
Quality Points: 3.5
```

---

## Exercise 2: Grade Dictionary with Validation

**File:** `exercise2.py`

**Objective:** Use dictionary's `.get()` method for safe lookups

**Instructions:**
1. Create the `grade_points` dictionary
2. Get a grade from the user
3. Use `.get()` method with "Invalid" as the default value
4. Check if the result is "Invalid":
   - If valid: print grade and quality points
   - If invalid: print error and show valid grades

**Expected Output (Valid):**
```
Enter grade: A
Grade: A
Quality Points: 4.0
```

**Expected Output (Invalid):**
```
Enter grade: A+
Invalid grade!
Valid grades: A, B+, B, C+, C, D, F
```

---

## Exercise 3: Subject Grade Storage

**File:** `exercise3.py`

**Objective:** Store multiple pieces of information in a dictionary

**Instructions:**
1. Create the `grade_points` dictionary
2. Get subject name, grade, and units from user
3. Look up quality points for the grade
4. Create a `subject_info` dictionary with keys:
   - 'name': subject name
   - 'grade': grade
   - 'units': units
   - 'points': quality points
5. Print all the subject information

**Expected Output:**
```
Enter subject name: Mathematics
Enter grade: A
Enter units: 3

Subject Information:
Name: Mathematics
Grade: A
Units: 3
Quality Points: 4.0
```
