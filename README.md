STUDENT GRADE CALCULATOR FOR STELLA EZINNE
Project Plan

1. Project Title
   Student Grade Calculator
2. Project Description
   The Student Grade Calculator is a small Python application designed to help students and lecturers calculate academic results quickly and accurately. The application accepts a student’s name and scores from three academic assessments, calculates the student’s total score and average score, assigns a letter grade from A to F, and determines whether the student has passed or failed.
   The application will use input validation to prevent invalid entries, such as empty student names, non-numeric scores, and scores outside the valid range. The project will also demonstrate the use of Python classes, methods, loops, conditional statements, and error handling.
3. Target Users
   The application is designed primarily for:
   • Students who want to calculate and check their academic results.
   • Lecturers who want to quickly calculate a student’s total, average, grade, and pass/fail status.
4. Project Objectives
   The objectives of the project are to:
5. Develop a simple application that calculates student academic results.
6. Allow users to enter a student’s name and at least three assessment scores.
7. Automatically calculate the student’s total and average score.
8. Automatically assign an appropriate letter grade from A to F.
9. Determine and display whether the student passed or failed.
10. Apply input validation and error handling to improve the reliability of the application.
11. Demonstrate the use of Python programming concepts learned during the course.
12. Use Git and GitHub to manage and document the development process.
13. Functional Requirements
    The application must be able to:
    Requirement 1: Input Student Name
    The application must allow the user to enter the student’s name. The application should reject an empty name.
    Requirement 2: Input Assessment Scores
    The application must allow the user to enter at least three assessment scores. Each score must be a valid numerical value within the accepted range of 0 to 100.
    Requirement 3: Calculate Total Score
    The application must add the three assessment scores and display the student’s total score.
    Requirement 4: Calculate Average Score
    The application must calculate and display the student’s average score based on the assessment scores entered.
    Requirement 5: Assign Grade
    The application must assign a letter grade from A to F based on the student’s average score.
    Requirement 6: Display Pass/Fail Status
    The application must determine and display whether the student has passed or failed based on the defined pass mark.
14. Proposed Grading Scale
    The following grading scale will be used:
    Average Score Grade Status
    70–100 A Pass
    60–69 B Pass
    50–59 C Pass
    45–49 D Pass
    40–44 E Pass
    0–39 F Fail
    Pass Mark: 40%
15. Expected Input and Output
    Feature 1: Student Name
    Input:
    Enter student name: Stella Ezinne
    Expected Output:
    Student name: Stella Ezinne
    The application should reject an empty name and request the user to enter a valid name.

Feature 2: Assessment Scores
Input:
Enter-Assignment-score:80
Enter-Test-score:75
Enter Examination score: 90
Expected Output:
Assessment scores successfully recorded.
The application should reject invalid inputs such as letters, negative values, and scores greater than 100.

Feature 3: Calculate Total Score
Input:
Assignment= 80
Test= 75
Examination = 90
Expected Output:
Total Score: 245

Feature 4: Calculate Average Score
Input:
Assignment=80
Test =75
Examination = 90
Expected Output:
Average Score: 81.67

Feature 5: Assign Grade
Input:
Average Score: 81.67
Expected Output:
Grade: A

Feature 6: Display Pass/Fail Status
Input:
Average Score: 81.67
Expected Output:
Status: Pass

8. Proposed Classes and Functions
   The project will use a class-based structure to demonstrate object-oriented programming.
   Class: StudentGradeCalculator
   This class will represent the student’s academic result and contain the methods needed to process the result.
   Proposed Methods
   **init**()
   Initializes the student’s name and assessment scores.
   calculate_total()
   Calculates the total score from the three assessment scores.
   calculate_average()
   Calculates the average score.
   calculate_grade()
   Determines the student’s letter grade based on the average score.
   get_status()
   Determines whether the student has passed or failed.
   display_result()
   Displays the student’s complete result, including name, total score, average, grade, and pass/fail status.
9. Additional Functions
   The application may also use separate functions to improve input validation and organization.
   get_student_name()
   Collects and validates the student’s name.
   get_score()
   Collects and validates each assessment score.
   main()
   Controls the overall flow of the application and connects the different parts of the program.
10. Python Concepts to Be Demonstrated
    The application will demonstrate:
    • Classes
    • Methods
    • Functions
    • Variables
    • User input
    • Data types
    • Loops
    • Conditional statements (if, elif, else)
    • Exception handling (try and except)
    • Input validation
    • Arithmetic operations
    • Formatted output using f-strings
11. Proposed Application Flow
    The expected flow of the application is:
    Start
    ↓
    Enter Student Name
    ↓
    Validate Student Name
    ↓
    Enter Assessment_1 Score
    ↓
    Validate Score
    ↓
    Enter Assessment_2 Score
    ↓
    Validate Score
    ↓
    Enter Assessment 3 Score
    ↓
    Validate Score
    ↓
    Calculate Total Score
    ↓
    Calculate Average Score
    ↓
    Assign Grade (A-F)
    ↓
    Determine Pass/Fail Status
    ↓
    Display Complete Result
    ↓
    End
12. Input Validation and Error Handling
    The application will validate user input to ensure reliable operation.
    The following situations will be handled:
    • Empty student name.
    • Non-numeric assessment score.
    • Negative assessment score.
    • Assessment score greater than 100.
    • Invalid input that cannot be converted into a number.
    For invalid input, the application will display an appropriate error message and ask the user to enter the value again instead of crashing.
13. Version Control Plan
    Git and GitHub will be used to track the development of the application.
    The repository will be created before application coding begins.
    The planned development process will include multiple commits, such as:
14. Initial commit: Add project plan and README
15. Add student name input and validation
16. Add assessment score input and validation
17. Add total and average score calculations
18. Add grade and pass/fail calculation
19. Add result display and improve error handling
20. Add testing documentation
    Each commit will represent a meaningful stage of development.
21. Testing Plan
    The application will be tested using both normal and unusual inputs.
    Normal Input Testing
    The application will be tested with valid student names and valid scores between 0 and 100.
    Example:
    Name: Stella Ezinne
    Assignment: 80
    Test: 75
    Examination: 90
    Expected result:
    Total:245
    Average:81.67
    Grade: A
    Status: Pass
    Unusual and Invalid Input Testing
    The application will be tested with:
    • Empty student name.
    • Letters entered instead of numbers.
    • Negative scores.
    • Scores above 100.
    • Boundary scores such as 0, 40, 49, 50, 69, 70, and 100.
    The results of the tests and at least one bug discovered and fixed during development will be documented before final submission.
22. Expected Final Outcome
    At the end of the project, the Student Grade Calculator should be a functional Python application that accepts student information and assessment scores, processes the results correctly, assigns the appropriate grade, and displays the student’s pass/fail status.
    The final project will be stored in a GitHub repository with a clear README, documented development history, multiple meaningful commits, and evidence of testing.
