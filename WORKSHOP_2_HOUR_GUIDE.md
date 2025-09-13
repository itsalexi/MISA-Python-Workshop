# Python Workshop: QPI Calculator (2-Hour Version)

## Workshop Schedule (120 minutes total)

### **Setup & Introduction (10 minutes)**

- Welcome and introductions
- Workshop overview and objectives
- QPI system explanation
- Python environment setup verification

### **Lesson 1: Variables & Basic Input (20 minutes)**

- **Variables (10 min)**: What are variables, data types, creating variables
- **User Input (10 min)**: `input()` function, type conversion
- **Quick Exercise**: Create variables for student info and get one grade

### **Lesson 2: Conditional Statements (25 minutes)**

- **If/elif/else (15 min)**: Basic conditionals, grade categorization
- **Grade Mapping (10 min)**: Map grades to quality points using if statements
- **Exercise**: Grade categorization with quality point assignment

### **Lesson 3: Dictionaries (20 minutes)**

- **Dictionary Basics (10 min)**: Key-value pairs, accessing values
- **Grade Dictionary (10 min)**: Replace if-elif chains with dictionary lookup
- **Exercise**: Create grade-to-quality-point dictionary

### **Lesson 4: Loops & QPI Calculation (30 minutes)**

- **For Loops (10 min)**: Processing multiple grades
- **QPI Formula (5 min)**: Weighted average calculation
- **Complete Calculator (15 min)**: Build basic QPI calculator
- **Exercise**: Calculate QPI for 3-4 subjects

### **Lesson 5: Final Calculator & Features (10 minutes)**

- **Error Handling (5 min)**: Input validation basics
- **Final Calculator (5 min)**: Run the complete calculator
- **Demo**: Show advanced features

### **Wrap-up & Q&A (5 minutes)**

- Review key concepts
- Answer questions
- Provide resources for continued learning

---

## Condensed Lesson Plans

### **Lesson 1: Variables & Input (20 min)**

**Variables (10 min)**

```python
# Quick demo
student_name = "Juan"
grade = "A+"
credits = 3
```

**Input (10 min)**

```python
# Quick demo
name = input("Enter name: ")
grade = input("Enter grade: ")
credits = int(input("Enter credits: "))
```

**Quick Exercise (5 min)**

```python
# Students do this
student = input("Student name: ")
subject = input("Subject: ")
grade = input("Grade: ")
print(f"{student} got {grade} in {subject}")
```

### **Lesson 2: Conditional Statements (25 min)**

**If Statements (15 min)**

```python
# Demo
if grade == "A+":
    points = 4.0
elif grade == "A":
    points = 4.0
elif grade == "B+":
    points = 3.3
# ... etc
```

**Exercise (10 min)**

```python
# Students complete this
grade = input("Enter grade: ")
if grade == "A+":
    quality_points = 4.0
elif grade == "A":
    quality_points = 4.0
elif grade == "A-":
    quality_points = 3.7
elif grade == "B+":
    quality_points = 3.3
elif grade == "B":
    quality_points = 3.0
else:
    quality_points = 0.0

print(f"Grade: {grade}, Quality Points: {quality_points}")
```

### **Lesson 3: Dictionaries (20 min)**

**Dictionary Demo (10 min)**

```python
# Show the magic of dictionaries
grade_points = {
    "A+": 4.0, "A": 4.0, "A-": 3.7,
    "B+": 3.3, "B": 3.0, "B-": 2.7,
    "C+": 2.3, "C": 2.0, "C-": 1.7,
    "D": 1.0, "F": 0.0
}

grade = "A+"
points = grade_points[grade]  # Much simpler!
```

**Exercise (10 min)**

```python
# Students create their own
grade_points = {
    "A+": 4.0, "A": 4.0, "A-": 3.7,
    "B+": 3.3, "B": 3.0, "B-": 2.7,
    "C+": 2.3, "C": 2.0, "C-": 1.7,
    "D": 1.0, "F": 0.0
}

grade = input("Enter grade: ")
points = grade_points.get(grade, "Invalid")
print(f"Quality Points: {points}")
```

### **Lesson 4: Loops & QPI (30 min)**

**For Loop Demo (10 min)**

```python
# Get multiple grades
num_subjects = int(input("How many subjects? "))
subjects = []

for i in range(num_subjects):
    subject = input(f"Subject {i+1}: ")
    grade = input("Grade: ")
    credits = int(input("Credits: "))
    subjects.append({
        'name': subject,
        'grade': grade,
        'credits': credits,
        'points': grade_points[grade]
    })
```

**QPI Calculation (10 min)**

```python
# Calculate QPI
total_points = 0
total_credits = 0

for sub in subjects:
    weighted_points = sub['points'] * sub['credits']
    total_points += weighted_points
    total_credits += sub['credits']

qpi = total_points / total_credits
print(f"QPI: {qpi:.2f}")
```

**Complete Exercise (10 min)**

```python
# Students build complete calculator
grade_points = {
    "A+": 4.0, "A": 4.0, "A-": 3.7,
    "B+": 3.3, "B": 3.0, "B-": 2.7,
    "C+": 2.3, "C": 2.0, "C-": 1.7,
    "D": 1.0, "F": 0.0
}

# Get student info
name = input("Student name: ")
num_subjects = int(input("How many subjects? "))

# Collect grades
subjects = []
for i in range(num_subjects):
    subject = input(f"Subject {i+1}: ")
    grade = input("Grade: ")
    credits = int(input("Credits: "))
    subjects.append({
        'name': subject,
        'grade': grade,
        'credits': credits,
        'points': grade_points[grade]
    })

# Calculate QPI
total_points = sum(sub['points'] * sub['credits'] for sub in subjects)
total_credits = sum(sub['credits'] for sub in subjects)
qpi = total_points / total_credits

# Display results
print(f"\nQPI Report for {name}:")
for sub in subjects:
    print(f"{sub['name']}: {sub['grade']} ({sub['credits']} credits)")
print(f"QPI: {qpi:.2f}")
```

### **Lesson 5: Final Features (10 min)**

**Show Advanced Calculator (10 min)**

- Run the final calculator
- Demonstrate error handling
- Show additional features
- Let students try it

---

## Teaching Tips for 2-Hour Workshop

### **Time Management**

- ⏰ **Stick to time limits** - Use a timer
- 🎯 **Focus on core concepts** - Don't get sidetracked
- 📝 **Provide code templates** - Students can copy-paste and modify
- 🚀 **Move quickly** - Less theory, more hands-on

### **Student Engagement**

- 👥 **Pair programming** - Students work in pairs
- 🎪 **Live coding** - Instructor demonstrates, students follow
- ✅ **Frequent check-ins** - "Everyone got that? Any questions?"
- 🏆 **Celebrate wins** - "Great job! You just built a calculator!"

### **Adaptation Strategies**

- 📚 **Beginner-friendly** - Start simple, add complexity
- 🔄 **Skip advanced topics** - Focus on core concepts
- 📋 **Provide solutions** - Give working code if students struggle
- 🎯 **One goal** - Get everyone to calculate QPI successfully

### **Materials Needed**

- 💻 **Laptops/computers** with Python installed
- 📝 **Code templates** (provided)
- ⏰ **Timer/clock** for time management
- 🎯 **Sample data** for testing

---

## Quick Reference Cards

### **Variables**

```python
name = "Juan"        # String
age = 20             # Integer
gpa = 3.5            # Float
is_passing = True    # Boolean
```

### **Input**

```python
name = input("Enter name: ")
age = int(input("Enter age: "))
```

### **Conditionals**

```python
if grade == "A+":
    points = 4.0
elif grade == "A":
    points = 4.0
else:
    points = 0.0
```

### **Dictionaries**

```python
grade_points = {"A+": 4.0, "A": 4.0, "B+": 3.3}
points = grade_points["A+"]  # Gets 4.0
```

### **Loops**

```python
for i in range(3):
    print(f"Subject {i+1}")

for subject in subjects:
    print(subject['name'])
```

### **QPI Formula**

```python
qpi = (sum of grade_points × credits) / total_credits
```

---

## Success Metrics

**By the end of 2 hours, students should be able to:**

- ✅ Create variables and get user input
- ✅ Use if statements to categorize grades
- ✅ Use dictionaries to map grades to points
- ✅ Use loops to process multiple grades
- ✅ Calculate QPI using weighted averages
- ✅ Build a working QPI calculator

**Workshop is successful if:**

- 🎯 80%+ of students complete the basic calculator
- 🎪 Students are engaged and asking questions
- 🚀 Students understand the core Python concepts
- 📈 Students feel confident to continue learning Python
