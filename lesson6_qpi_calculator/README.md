# Lesson 6: Complete QPI Calculator

## Learning Objectives

- Combine all Python concepts learned in previous lessons
- Build a complete, user-friendly QPI calculator
- Practice error handling and input validation
- Create a polished application with clear output

## Project Overview

In this final lesson, you'll build a complete QPI calculator that:

- Gets student information
- Collects multiple subject grades and credits
- Calculates QPI using weighted averages
- Provides detailed grade reports
- Handles errors gracefully
- Offers multiple calculation modes

## QPI Formula

QPI = (Sum of (Grade Points × Credits)) / Total Credits

Where:

- Grade Points: A+ = 4.0, A = 4.0, A- = 3.7, B+ = 3.3, B = 3.0, etc.
- Credits: Number of credit hours for each subject

## Features to Implement

1. **Student Information Entry**
2. **Grade Collection with Validation**
3. **Credit Hours Management**
4. **QPI Calculation**
5. **Grade Reports**
6. **Error Handling**
7. **Multiple Calculation Options**

## Exercise 1: Basic QPI Calculator

Create `qpi_calculator_basic.py`:

```python
# Basic QPI Calculator

def main():
    print("=== QPI Calculator ===")

    # Student information
    student_name = input("Enter student name: ")

    # Grade-to-quality-point mapping
    grade_points = {
        "A+": 4.0, "A": 4.0, "A-": 3.7,
        "B+": 3.3, "B": 3.0, "B-": 2.7,
        "C+": 2.3, "C": 2.0, "C-": 1.7,
        "D": 1.0, "F": 0.0
    }

    # Get number of subjects
    num_subjects = int(input("How many subjects? "))

    # Collect grades
    subjects = []
    for i in range(num_subjects):
        print(f"\nSubject {i+1}:")
        subject = input("Subject name: ")
        grade = input("Grade: ")
        credits = int(input("Credits: "))

        subjects.append({
            'name': subject,
            'grade': grade,
            'credits': credits,
            'points': grade_points.get(grade, 0.0)
        })

    # Calculate QPI
    total_points = sum(sub['points'] * sub['credits'] for sub in subjects)
    total_credits = sum(sub['credits'] for sub in subjects)
    qpi = total_points / total_credits

    # Display results
    print(f"\n=== QPI Report for {student_name} ===")
    for sub in subjects:
        print(f"{sub['name']}: {sub['grade']} ({sub['credits']} credits)")
    print(f"\nQPI: {qpi:.2f}")

if __name__ == "__main__":
    main()
```

## Exercise 2: Advanced QPI Calculator

Create `qpi_calculator_advanced.py`:

```python
# Advanced QPI Calculator with Error Handling

def get_valid_grade():
    """Get a valid grade from user with error handling"""
    valid_grades = ["A+", "A", "A-", "B+", "B", "B-", "C+", "C", "C-", "D", "F"]

    while True:
        grade = input("Grade: ").upper()
        if grade in valid_grades:
            return grade
        else:
            print("Invalid grade! Valid grades:", ", ".join(valid_grades))

def get_valid_credits():
    """Get valid credits from user with error handling"""
    while True:
        try:
            credits = int(input("Credits: "))
            if credits > 0:
                return credits
            else:
                print("Credits must be positive!")
        except ValueError:
            print("Please enter a valid number!")

def calculate_qpi(subjects):
    """Calculate QPI from list of subjects"""
    if not subjects:
        return 0.0

    total_points = sum(sub['points'] * sub['credits'] for sub in subjects)
    total_credits = sum(sub['credits'] for sub in subjects)

    return total_points / total_credits if total_credits > 0 else 0.0

def get_grade_level(qpi):
    """Determine grade level based on QPI"""
    if qpi >= 3.7:
        return "Excellent - Dean's List Level!"
    elif qpi >= 3.0:
        return "Good - Above Average!"
    elif qpi >= 2.0:
        return "Satisfactory - Keep Improving!"
    else:
        return "Needs Improvement - Focus on Studies!"

def main():
    print("=== Advanced QPI Calculator ===")

    # Grade-to-quality-point mapping
    grade_points = {
        "A+": 4.0, "A": 4.0, "A-": 3.7,
        "B+": 3.3, "B": 3.0, "B-": 2.7,
        "C+": 2.3, "C": 2.0, "C-": 1.7,
        "D": 1.0, "F": 0.0
    }

    # Student information
    student_name = input("Enter student name: ")
    course = input("Enter course/program: ")

    # Get number of subjects
    while True:
        try:
            num_subjects = int(input("How many subjects? "))
            if num_subjects > 0:
                break
            else:
                print("Number of subjects must be positive!")
        except ValueError:
            print("Please enter a valid number!")

    # Collect grades
    subjects = []
    print(f"\nEnter grades for {num_subjects} subjects:")

    for i in range(num_subjects):
        print(f"\nSubject {i+1}:")
        subject = input("Subject name: ")
        grade = get_valid_grade()
        credits = get_valid_credits()

        subjects.append({
            'name': subject,
            'grade': grade,
            'credits': credits,
            'points': grade_points[grade]
        })

        print(f"✓ Added: {subject} - {grade} ({credits} credits)")

    # Calculate QPI
    qpi = calculate_qpi(subjects)

    # Display comprehensive report
    print(f"\n{'='*50}")
    print(f"QPI REPORT FOR {student_name.upper()}")
    print(f"Course: {course}")
    print(f"{'='*50}")

    print(f"\n{'Subject':<20} {'Grade':<6} {'Credits':<8} {'Points':<6}")
    print("-" * 50)

    total_credits = 0
    total_weighted_points = 0

    for sub in subjects:
        weighted_points = sub['points'] * sub['credits']
        total_weighted_points += weighted_points
        total_credits += sub['credits']

        print(f"{sub['name']:<20} {sub['grade']:<6} {sub['credits']:<8} {sub['points']:<6}")

    print("-" * 50)
    print(f"{'TOTALS':<20} {'':<6} {total_credits:<8} {total_weighted_points:<6}")

    print(f"\nQPI Calculation:")
    print(f"Total Weighted Points: {total_weighted_points}")
    print(f"Total Credits: {total_credits}")
    print(f"QPI: {qpi:.2f}")
    print(f"Grade Level: {get_grade_level(qpi)}")

    # Grade distribution
    grade_count = {}
    for sub in subjects:
        grade = sub['grade']
        grade_count[grade] = grade_count.get(grade, 0) + 1

    print(f"\nGrade Distribution:")
    for grade, count in sorted(grade_count.items()):
        print(f"{grade}: {count} subject(s)")

if __name__ == "__main__":
    main()
```

## Exercise 3: Interactive QPI Calculator

Create `qpi_calculator_interactive.py`:

```python
# Interactive QPI Calculator with Menu System

class QPICalculator:
    def __init__(self):
        self.grade_points = {
            "A+": 4.0, "A": 4.0, "A-": 3.7,
            "B+": 3.3, "B": 3.0, "B-": 2.7,
            "C+": 2.3, "C": 2.0, "C-": 1.7,
            "D": 1.0, "F": 0.0
        }
        self.subjects = []
        self.student_name = ""
        self.course = ""

    def add_subject(self):
        """Add a new subject"""
        print("\n--- Add New Subject ---")
        subject = input("Subject name: ")
        grade = self.get_valid_grade()
        credits = self.get_valid_credits()

        self.subjects.append({
            'name': subject,
            'grade': grade,
            'credits': credits,
            'points': self.grade_points[grade]
        })

        print(f"✓ Added: {subject} - {grade} ({credits} credits)")

    def get_valid_grade(self):
        """Get valid grade from user"""
        valid_grades = list(self.grade_points.keys())
        while True:
            grade = input("Grade: ").upper()
            if grade in valid_grades:
                return grade
            else:
                print("Invalid grade! Valid grades:", ", ".join(valid_grades))

    def get_valid_credits(self):
        """Get valid credits from user"""
        while True:
            try:
                credits = int(input("Credits: "))
                if credits > 0:
                    return credits
                else:
                    print("Credits must be positive!")
            except ValueError:
                print("Please enter a valid number!")

    def display_grades(self):
        """Display all current grades"""
        if not self.subjects:
            print("No grades entered yet!")
            return

        print(f"\n--- Current Grades ---")
        print(f"{'Subject':<20} {'Grade':<6} {'Credits':<8}")
        print("-" * 40)
        for sub in self.subjects:
            print(f"{sub['name']:<20} {sub['grade']:<6} {sub['credits']:<8}")

    def calculate_qpi(self):
        """Calculate and display QPI"""
        if not self.subjects:
            print("No grades to calculate!")
            return

        qpi = sum(sub['points'] * sub['credits'] for sub in self.subjects) / sum(sub['credits'] for sub in self.subjects)

        print(f"\n--- QPI Calculation ---")
        print(f"QPI: {qpi:.2f}")

        if qpi >= 3.7:
            print("Excellent! Dean's List Level!")
        elif qpi >= 3.0:
            print("Good! Above Average Performance!")
        elif qpi >= 2.0:
            print("Satisfactory! Keep Improving!")
        else:
            print("Needs Improvement! Focus on Studies!")

    def clear_grades(self):
        """Clear all grades"""
        self.subjects = []
        print("All grades cleared!")

    def show_menu(self):
        """Display main menu"""
        print(f"\n=== QPI Calculator ===")
        print(f"Student: {self.student_name}")
        print(f"Course: {self.course}")
        print(f"Subjects: {len(self.subjects)}")
        print("\n1. Add Subject")
        print("2. View Grades")
        print("3. Calculate QPI")
        print("4. Clear All Grades")
        print("5. Exit")

    def run(self):
        """Main program loop"""
        print("Welcome to the QPI Calculator!")
        self.student_name = input("Enter student name: ")
        self.course = input("Enter course/program: ")

        while True:
            self.show_menu()
            choice = input("\nEnter your choice (1-5): ")

            if choice == "1":
                self.add_subject()
            elif choice == "2":
                self.display_grades()
            elif choice == "3":
                self.calculate_qpi()
            elif choice == "4":
                self.clear_grades()
            elif choice == "5":
                print("Thank you for using QPI Calculator!")
                break
            else:
                print("Invalid choice! Please enter 1-5.")

if __name__ == "__main__":
    calculator = QPICalculator()
    calculator.run()
```

## Key Features Implemented

1. **Error Handling**: Validates all user input
2. **User-Friendly Interface**: Clear menus and prompts
3. **Comprehensive Reports**: Detailed grade analysis
4. **Modular Design**: Functions for different operations
5. **Interactive System**: Menu-driven interface
6. **Grade Validation**: Ensures only valid grades are entered
7. **Credit Validation**: Ensures positive credit values

## Testing Your Calculator

Test your calculator with these sample inputs:

**Student:** Juan Dela Cruz
**Course:** Computer Science
**Subjects:**

- Mathematics: A+ (3 credits)
- Physics: B+ (3 credits)
- Programming: A (3 credits)
- English: B (3 credits)
- History: A- (2 credits)

**Expected QPI:** (4.0×3 + 3.3×3 + 4.0×3 + 3.0×3 + 3.7×2) / 14 = 3.64

## Congratulations!

You've successfully built a complete QPI calculator using all the Python concepts you learned:

- Variables and data storage
- User input handling
- Conditional statements
- Dictionaries for grade mapping
- Loops for processing multiple grades
- Error handling and validation
- Modular programming with functions

This project demonstrates how different Python concepts work together to create a useful application!
