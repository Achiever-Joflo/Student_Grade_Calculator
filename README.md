Student Grade Calculator

Project Overview

The Student Grade Calculator is a Python application developed to assist lecturers and students in calculating academic results accurately and efficiently. The application allows users to enter a student's name and three assessment scores, validates all inputs, calculates the total and average scores, assigns a letter grade (A–F), determines the student's pass/fail status, and displays the complete result.

The project was developed incrementally using Git and GitHub while applying Object-Oriented Programming (OOP), functions, loops, conditional statements, and exception handling.

Project Planning

Functional Requirements

The application shall:

1. Accept a student's name.
2. Accept three assessment scores (Assignment, Test, and Examination).
3. Validate all user inputs.
4. Calculate the total and average scores.
5. Assign a grade (A–F) and determine Pass/Fail status.
6. Display the student's complete result.

Planned Classes and Functions

Class

- `StudentGradeCalculator`

Methods

- `calculate_total()`
- `calculate_average()`
- `calculate_grade()`
- `get_status()`
- `display_result()`

Helper Functions

- `get_student_name()`
- `get_score()`
- `main()`

Expected Input and Output

Input

- Student Name
- Assignment Score
- Test Score
- Examination Score

Output

- Student Name
- Assignment Score
- Test Score
- Examination Score
- Total Score
- Average Score
- Grade (A–F)
- Pass/Fail Status

Features

- Student name validation
- Assessment score validation
- Total score calculation
- Average score calculation
- Automatic grade assignment (A–F)
- Pass/Fail determination
- Exception handling
- Object-Oriented Programming
- Git and GitHub version control

Technologies Used

- Python 3
- Visual Studio Code
- Git
- GitHub

Project Structure

Student_Grade_Calculator/
│
├── README.md
├── grade_calculator.py
├── testing.md
└── .gitignore

Program Flow
Start
│
▼
Enter Student Name
│
Validate Name
│
Enter Assignment Score
│
Validate Score
│
Enter Test Score
│
Validate Score
│
Enter Examination Score
│
Validate Score
│
Calculate Total Score
│
Calculate Average Score
│
Assign Grade
│
Determine Pass/Fail
│
Display Result
│
End

Grading Scale

| Average | Grade | Status |
| ------- | ----- | ------ |
| 70–100  | A     | Pass   |
| 60–69   | B     | Pass   |
| 50–59   | C     | Pass   |
| 45–49   | D     | Pass   |
| 40–44   | E     | Pass   |
| 0–39    | F     | Fail   |

Object-Oriented Design

The application uses the `StudentGradeCalculator` class to organize student information and result calculations.

The class stores:

- Student Name
- Assignment Score
- Test Score
- Examination Score

It also provides methods to calculate:

- Total Score
- Average Score
- Grade
- Pass/Fail Status
- Display Final Result

Using a class improves code organization, readability, and maintainability.

Input Validation

The application validates user input by checking for:

Student Name

- Cannot be empty.
- Cannot contain numbers.
- Must contain only alphabetic characters and spaces.

Assessment Scores

- Must be numeric.
- Must be between 0 and 100.
- Rejects negative numbers.
- Rejects values greater than 100.
  Whenever invalid input is detected, the application displays an appropriate error message and requests another input without crashing.

Example Execution

Input

Enter student name: Stella Ezinne

Enter Assignment score: 80

Enter Test score: 75

Enter Examination score: 90

Output

===================================
STUDENT RESULT
===================================

Student Name : Stella Ezinne
Assignment : 80.0
Test : 75.0
Examination : 90.0

Total Score : 245.0
Average : 81.67
Grade : A
Status : Pass

How to Run the Program

1. Clone or download this repository.

2. Open the project folder in Visual Studio Code.

3. Open the terminal.

4. Run the application:

```bash
python grade_calculator.py

5. Follow the prompts displayed on the screen.

 Testing

The application was tested using both normal and unusual inputs.

 Normal Tests

- Valid student names
- Valid assessment scores
- Boundary values (0, 40, 70, and 100)

 Edge Cases

- Empty student name
- Numeric student name
- Student name containing numbers
- Alphabetic score input
- Negative score
- Score greater than 100

Detailed testing results are available in testing.md.

 Version Control

The project was developed incrementally using Git and GitHub.

Major commits include:

- Initial project plan and README
- Student name input and validation
- Assessment score input and validation
- Total and average calculations
- Grade and pass/fail calculation
- Refactoring using the StudentGradeCalculator class
- Documentation updates

 Future Improvements

Possible future enhancements include:

- Multiple student support
- Saving results to a file
- Database integration
- Graphical User Interface (GUI)
- Exporting reports to PDF or Excel

 Author

Name: Stella Ezinne

Course: Python Programming

Project: Student Grade Calculator

Institution: (ESUT)

 License

This project was developed for educational purposes only.
```
