"""
Final QPI Calculator - Complete Implementation
This calculator demonstrates all Python concepts learned in the workshop:
- Variables and data storage
- User input handling
- Conditional statements
- Dictionaries for grade mapping
- Loops for processing multiple grades
- Error handling and validation
- Functions and modular programming
"""

class QPICalculator:
    def __init__(self):
        """Initialize the QPI Calculator with grade mappings"""
        self.grade_points = {
            "A+": 4.0, "A": 4.0, "A-": 3.7,
            "B+": 3.3, "B": 3.0, "B-": 2.7,
            "C+": 2.3, "C": 2.0, "C-": 1.7,
            "D": 1.0, "F": 0.0
        }
        self.subjects = []
        self.student_name = ""
        self.course = ""
        self.semester = ""
    
    def display_welcome(self):
        """Display welcome message and QPI information"""
        print("=" * 60)
        print("           WELCOME TO QPI CALCULATOR")
        print("=" * 60)
        print("QPI (Quality Point Index) is calculated using:")
        print("QPI = (Sum of Grade Points × Credits) / Total Credits")
        print("\nGrade to Quality Point Mapping:")
        for grade, points in self.grade_points.items():
            print(f"  {grade}: {points}")
        print("=" * 60)
    
    def get_student_info(self):
        """Get student information"""
        print("\n--- Student Information ---")
        self.student_name = input("Enter student name: ")
        self.course = input("Enter course/program: ")
        self.semester = input("Enter semester: ")
    
    def get_valid_grade(self):
        """Get a valid grade from user with error handling"""
        valid_grades = list(self.grade_points.keys())
        while True:
            grade = input("Enter grade (A+, A, A-, B+, B, B-, C+, C, C-, D, F): ").upper()
            if grade in valid_grades:
                return grade
            else:
                print("Invalid grade! Valid grades:", ", ".join(valid_grades))
    
    def get_valid_credits(self):
        """Get valid credits from user with error handling"""
        while True:
            try:
                credits = int(input("Enter number of credits: "))
                if credits > 0:
                    return credits
                else:
                    print("Credits must be positive!")
            except ValueError:
                print("Please enter a valid number!")
    
    def add_subject(self):
        """Add a new subject with validation"""
        print("\n--- Add New Subject ---")
        subject = input("Enter subject name: ")
        grade = self.get_valid_grade()
        credits = self.get_valid_credits()
        
        subject_data = {
            'name': subject,
            'grade': grade,
            'credits': credits,
            'points': self.grade_points[grade]
        }
        
        self.subjects.append(subject_data)
        print(f"✓ Successfully added: {subject} - {grade} ({credits} credits)")
        
        return subject_data
    
    def display_current_grades(self):
        """Display all current grades in a formatted table"""
        if not self.subjects:
            print("\nNo grades entered yet!")
            return
        
        print(f"\n--- Current Grades for {self.student_name} ---")
        print(f"Course: {self.course} | Semester: {self.semester}")
        print("-" * 70)
        print(f"{'Subject':<25} {'Grade':<6} {'Credits':<8} {'Points':<8} {'Weighted':<10}")
        print("-" * 70)
        
        total_credits = 0
        total_weighted_points = 0
        
        for sub in self.subjects:
            weighted = sub['points'] * sub['credits']
            total_credits += sub['credits']
            total_weighted_points += weighted
            
            print(f"{sub['name']:<25} {sub['grade']:<6} {sub['credits']:<8} {sub['points']:<8} {weighted:<10.1f}")
        
        print("-" * 70)
        print(f"{'TOTALS':<25} {'':<6} {total_credits:<8} {'':<8} {total_weighted_points:<10.1f}")
    
    def calculate_qpi(self):
        """Calculate and display QPI with detailed analysis"""
        if not self.subjects:
            print("\nNo grades to calculate! Please add some subjects first.")
            return None
        
        total_weighted_points = sum(sub['points'] * sub['credits'] for sub in self.subjects)
        total_credits = sum(sub['credits'] for sub in self.subjects)
        qpi = total_weighted_points / total_credits
        
        print(f"\n--- QPI Calculation ---")
        print(f"Total Weighted Points: {total_weighted_points}")
        print(f"Total Credits: {total_credits}")
        print(f"QPI: {qpi:.3f}")
        
        # Determine academic standing
        if qpi >= 3.7:
            standing = "EXCELLENT - Dean's List Level!"
            color = "🌟"
        elif qpi >= 3.0:
            standing = "GOOD - Above Average Performance!"
            color = "👍"
        elif qpi >= 2.0:
            standing = "SATISFACTORY - Keep Improving!"
            color = "📈"
        else:
            standing = "NEEDS IMPROVEMENT - Focus on Studies!"
            color = "📚"
        
        print(f"Academic Standing: {color} {standing}")
        
        return qpi
    
    def show_grade_distribution(self):
        """Display grade distribution analysis"""
        if not self.subjects:
            print("\nNo grades to analyze!")
            return
        
        grade_count = {}
        for sub in self.subjects:
            grade = sub['grade']
            grade_count[grade] = grade_count.get(grade, 0) + 1
        
        print(f"\n--- Grade Distribution ---")
        total_subjects = len(self.subjects)
        
        for grade in ["A+", "A", "A-", "B+", "B", "B-", "C+", "C", "C-", "D", "F"]:
            count = grade_count.get(grade, 0)
            percentage = (count / total_subjects) * 100 if total_subjects > 0 else 0
            bar = "█" * int(percentage / 2)  # Simple bar chart
            print(f"{grade}: {count:2d} subjects ({percentage:5.1f}%) {bar}")
    
    def edit_subject(self):
        """Edit an existing subject"""
        if not self.subjects:
            print("\nNo subjects to edit!")
            return
        
        self.display_current_grades()
        
        try:
            index = int(input(f"\nEnter subject number to edit (1-{len(self.subjects)}): ")) - 1
            if 0 <= index < len(self.subjects):
                print(f"\nEditing: {self.subjects[index]['name']}")
                print("Enter new values (press Enter to keep current value)")
                
                # Get new subject name
                new_name = input(f"Subject name [{self.subjects[index]['name']}]: ")
                if new_name.strip():
                    self.subjects[index]['name'] = new_name.strip()
                
                # Get new grade
                print("Current grade:", self.subjects[index]['grade'])
                new_grade = self.get_valid_grade()
                self.subjects[index]['grade'] = new_grade
                self.subjects[index]['points'] = self.grade_points[new_grade]
                
                # Get new credits
                print(f"Current credits: {self.subjects[index]['credits']}")
                new_credits = self.get_valid_credits()
                self.subjects[index]['credits'] = new_credits
                
                print(f"✓ Successfully updated: {self.subjects[index]['name']}")
            else:
                print("Invalid subject number!")
        except ValueError:
            print("Please enter a valid number!")
    
    def delete_subject(self):
        """Delete a subject"""
        if not self.subjects:
            print("\nNo subjects to delete!")
            return
        
        self.display_current_grades()
        
        try:
            index = int(input(f"\nEnter subject number to delete (1-{len(self.subjects)}): ")) - 1
            if 0 <= index < len(self.subjects):
                deleted_subject = self.subjects.pop(index)
                print(f"✓ Deleted: {deleted_subject['name']}")
            else:
                print("Invalid subject number!")
        except ValueError:
            print("Please enter a valid number!")
    
    def clear_all_grades(self):
        """Clear all grades with confirmation"""
        if not self.subjects:
            print("\nNo grades to clear!")
            return
        
        confirm = input(f"\nAre you sure you want to clear all {len(self.subjects)} subjects? (yes/no): ").lower()
        if confirm in ['yes', 'y']:
            self.subjects = []
            print("✓ All grades cleared!")
        else:
            print("Operation cancelled.")
    
    def save_report(self):
        """Save QPI report to a text file"""
        if not self.subjects:
            print("\nNo grades to save!")
            return
        
        filename = f"qpi_report_{self.student_name.replace(' ', '_')}.txt"
        
        try:
            with open(filename, 'w') as file:
                file.write("=" * 60 + "\n")
                file.write("           QPI CALCULATOR REPORT\n")
                file.write("=" * 60 + "\n\n")
                file.write(f"Student Name: {self.student_name}\n")
                file.write(f"Course: {self.course}\n")
                file.write(f"Semester: {self.semester}\n")
                file.write(f"Generated: {__import__('datetime').datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
                
                # Grade details
                file.write("--- Grade Details ---\n")
                file.write(f"{'Subject':<25} {'Grade':<6} {'Credits':<8} {'Points':<8} {'Weighted':<10}\n")
                file.write("-" * 70 + "\n")
                
                total_credits = 0
                total_weighted_points = 0
                
                for sub in self.subjects:
                    weighted = sub['points'] * sub['credits']
                    total_credits += sub['credits']
                    total_weighted_points += weighted
                    
                    file.write(f"{sub['name']:<25} {sub['grade']:<6} {sub['credits']:<8} {sub['points']:<8} {weighted:<10.1f}\n")
                
                file.write("-" * 70 + "\n")
                file.write(f"{'TOTALS':<25} {'':<6} {total_credits:<8} {'':<8} {total_weighted_points:<10.1f}\n\n")
                
                # QPI calculation
                qpi = total_weighted_points / total_credits if total_credits > 0 else 0
                file.write("--- QPI Calculation ---\n")
                file.write(f"Total Weighted Points: {total_weighted_points}\n")
                file.write(f"Total Credits: {total_credits}\n")
                file.write(f"QPI: {qpi:.3f}\n")
                
                # Academic standing
                if qpi >= 3.7:
                    standing = "EXCELLENT - Dean's List Level!"
                elif qpi >= 3.0:
                    standing = "GOOD - Above Average Performance!"
                elif qpi >= 2.0:
                    standing = "SATISFACTORY - Keep Improving!"
                else:
                    standing = "NEEDS IMPROVEMENT - Focus on Studies!"
                
                file.write(f"Academic Standing: {standing}\n")
            
            print(f"✓ Report saved to: {filename}")
        except Exception as e:
            print(f"Error saving report: {e}")
    
    def show_menu(self):
        """Display the main menu"""
        print(f"\n{'='*60}")
        print(f"           QPI CALCULATOR MENU")
        print(f"{'='*60}")
        print(f"Student: {self.student_name}")
        print(f"Course: {self.course}")
        print(f"Semester: {self.semester}")
        print(f"Subjects: {len(self.subjects)}")
        print(f"{'='*60}")
        print("1. Add Subject")
        print("2. View Current Grades")
        print("3. Calculate QPI")
        print("4. Show Grade Distribution")
        print("5. Edit Subject")
        print("6. Delete Subject")
        print("7. Clear All Grades")
        print("8. Save Report to File")
        print("9. Exit")
        print("-" * 60)
    
    def run(self):
        """Main program loop"""
        self.display_welcome()
        self.get_student_info()
        
        while True:
            self.show_menu()
            try:
                choice = input("Enter your choice (1-9): ").strip()
                
                if choice == "1":
                    self.add_subject()
                elif choice == "2":
                    self.display_current_grades()
                elif choice == "3":
                    self.calculate_qpi()
                elif choice == "4":
                    self.show_grade_distribution()
                elif choice == "5":
                    self.edit_subject()
                elif choice == "6":
                    self.delete_subject()
                elif choice == "7":
                    self.clear_all_grades()
                elif choice == "8":
                    self.save_report()
                elif choice == "9":
                    print("\nThank you for using the QPI Calculator!")
                    print("Good luck with your studies! 🎓")
                    break
                else:
                    print("Invalid choice! Please enter a number from 1-9.")
                    
            except KeyboardInterrupt:
                print("\n\nProgram interrupted. Goodbye!")
                break
            except Exception as e:
                print(f"An error occurred: {e}")
                print("Please try again.")

def main():
    """Main function to start the QPI Calculator"""
    try:
        calculator = QPICalculator()
        calculator.run()
    except Exception as e:
        print(f"Fatal error: {e}")
        print("Please restart the program.")

if __name__ == "__main__":
    main()
