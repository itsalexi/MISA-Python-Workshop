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
