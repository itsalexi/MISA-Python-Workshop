# Python Workshop: Building a QPI Calculator

Welcome to the MISA Python Workshop! This hands-on workshop teaches fundamental Python programming concepts by building a practical QPI (Quality Point Index) calculator.

## 🎯 Workshop Overview

This workshop is designed for beginners with little to no programming experience. You'll learn Python fundamentals progressively, with each lesson building on the previous one, culminating in a complete QPI calculator application.

### What You'll Learn

- Python variables and data types
- Getting user input
- Conditional statements (if/elif/else)
- Dictionaries for data mapping
- Loops for processing multiple items
- Building real-world applications

### What You'll Build

A complete QPI calculator that:
- Collects student information and grades
- Calculates weighted grade point averages
- Determines academic standing
- Provides detailed grade reports

## 📚 Workshop Structure

### Lesson 1: Variables and Data Storage
- Understanding variables in Python
- Different data types (strings, numbers, booleans)
- Storing and manipulating data

### Lesson 2: Getting User Input
- Using the `input()` function
- Converting input to different data types
- Basic data handling

### Lesson 3: Conditional Statements
- Understanding if/elif/else statements
- Logical operators
- Making decisions in code
- Categorizing grades

### Lesson 4: Loops
- For loops and while loops
- Processing multiple grades
- Iterating through data structures
- The `range()` function

### Lesson 5: Dictionaries
- Creating and using dictionaries
- Mapping grades to quality points
- Key-value relationships
- Dictionary methods

### Lesson 6: Complete QPI Calculator
This final project combines all the concepts you've learned:

1. **Variables** - Storing student information and grades
2. **User Input** - Getting data from the user
3. **Conditionals** - Determining academic standing
4. **Loops** - Collecting multiple subjects
5. **Dictionaries** - Mapping grades to quality points
6. **Lists** - Storing subject information
7. **Calculations** - Computing weighted averages
- Building the final application
- Step-by-step implementation

## 🚀 Getting Started

### Prerequisites

- Python 3.6 or higher installed on your computer
- A text editor or IDE (VS Code, PyCharm, or any text editor)
- Basic computer skills

### Installation

1. **Clone or download this repository:**
   ```bash
   git clone https://github.com/yourusername/MISA-Python-Workshop.git
   cd MISA-Python-Workshop
   ```

2. **Verify Python installation:**
   ```bash
   python --version
   # or
   python3 --version
   ```

3. **You're ready to start!**


## 📖 Lesson Guide

Navigate through the lessons in this order:

```
lesson1_variables/       → Learn about variables and data types
lesson2_input/          → Get user input
lesson3_conditions/     → Make decisions with if/elif/else
lesson4_loops/          → Process multiple items
lesson5_dictionaries/   → Map grades to quality points
lesson6_qpi_calculator/ → Build the complete calculator
```

Each lesson folder contains:
- `README.md` - Lesson content and explanations
- `exercise*.py` - Practice exercises
- Example code and solutions

## 🎓 QPI System Reference

The QPI system uses the following grade-to-quality-point mapping:

| Grade | Quality Points |
|-------|----------------|
| A     | 4.0            |
| B+    | 3.5            |
| B     | 3.0            |
| C+    | 2.5            |
| C     | 2.0            |
| D     | 1.0            |
| F     | 0.0            |

**QPI Formula:**
```
QPI = (Sum of (Grade Points × Units)) / Total Units
```

**Example:**
- Math: A (3 units) = 4.0 × 3 = 12.0
- English: B+ (3 units) = 3.5 × 3 = 10.5
- History: B (2 units) = 3.0 × 2 = 6.0
- **Total:** 28.5 ÷ 8 = **3.56 QPI**

## 🙏 Acknowledgments

Created for the MISA Python Workshop to introduce students to programming through practical, hands-on learning.

## 📞 Support

If you encounter any issues or have questions:

- Review the lesson README files
- Check the example code in each lesson
- Ask your workshop instructor for help

---

**Happy Coding! 🐍**

Start with `lesson1_variables/` and work your way through each lesson.