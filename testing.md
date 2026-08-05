Testing Report

Project: Student Grade Calculator

Introduction

Testing was carried out throughout the development of the Student Grade Calculator to ensure that all features worked correctly under both normal and unusual conditions.

The application was tested using valid inputs, boundary values, and invalid inputs. Any issues discovered during testing were corrected before the final version.

Test Environment

| Item                 | Details            |
| -------------------- | ------------------ |
| Programming Language | Python 3           |
| IDE                  | Visual Studio Code |
| Operating System     | Windows 10/11      |
| Version Control      | Git & GitHub       |

Normal Test Cases

| Test No. | Test Description          | Input                 | Expected Result | Actual Result | Status  |
| -------- | ------------------------- | --------------------- | --------------- | ------------- | ------- |
| 1        | Valid student information | Joseph, 80, 75, 90    | Grade A, Pass   | Grade A, Pass | ✅ Pass |
| 2        | Average score of 50       | Joseph, 50, 50, 50    | Grade C, Pass   | Grade C, Pass | ✅ Pass |
| 3        | Average score of 40       | Joseph, 40, 40, 40    | Grade E, Pass   | Grade E, Pass | ✅ Pass |
| 4        | Perfect scores            | Joseph, 100, 100, 100 | Grade A, Pass   | Grade A, Pass | ✅ Pass |
| 5        | Zero scores               | Joseph, 0, 0, 0       | Grade F, Fail   | Grade F, Fail | ✅ Pass |

Boundary Value Testing

| Input | Expected Result | Actual Result | Status  |
| ----- | --------------- | ------------- | ------- |
| 0     | Accepted        | Accepted      | ✅ Pass |
| 40    | Grade E         | Grade E       | ✅ Pass |
| 70    | Grade A         | Grade A       | ✅ Pass |
| 100   | Accepted        | Accepted      | ✅ Pass |

Invalid / Edge Case Testing

| Test No. | Invalid Input            | Expected Behavior                       | Actual Behavior | Status  |
| -------- | ------------------------ | --------------------------------------- | --------------- | ------- |
| 1        | Empty student name       | Display error and request another input | Works correctly | ✅ Pass |
| 2        | Student name = 123       | Reject input                            | Works correctly | ✅ Pass |
| 3        | Student name = Joseph123 | Reject input                            | Works correctly | ✅ Pass |
| 4        | Assignment score = abc   | Display error message                   | Works correctly | ✅ Pass |
| 5        | Assignment score = -10   | Reject input                            | Works correctly | ✅ Pass |
| 6        | Assignment score = 150   | Reject input                            | Works correctly | ✅ Pass |

Bug Found During Development

Bug Description

During the early stage of development, the application accepted numeric values as student names.
Example:

Enter student name:
123

The program incorrectly accepted the input and continued execution.

Cause

The validation only checked whether the input was empty.

Original code:

````python
if name:
    return name

Since `"123"` is not an empty string, Python considered it valid.

 Fix Applied

The validation logic was improved by checking whether the name contains only alphabetic characters (and spaces).

Updated code:

```python
if not name:
    print("Error: Student name cannot be empty.")
elif not name.replace(" ", "").isalpha():
    print("Error: Student name must contain only letters.")
else:
    return name

 Result After Fix

The application now correctly rejects:

- Empty names
- Numeric names
- Names containing numbers

Examples:

123

Rejected ✅

Stella123

Rejected ✅

Stella

Accepted ✅



Summary

Testing confirmed that:

- All required project features work correctly.
- Input validation prevents invalid data.
- Error handling prevents the application from crashing.
- Grade calculation produces correct results.
- Pass/Fail determination works correctly.
- The identified bug was successfully resolved before the final version.

 Conclusion

The Student Grade Calculator successfully passed all planned tests and satisfies the functional requirements of the project.

The application is considered stable, reliable, and ready for demonstration.
````
