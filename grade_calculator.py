def get_student_name():
    while True:
        name = input("Enter student name: ").strip()

        if not name:
            print("Error: Student name cannot be empty.")
        elif not name.replace(" ", "").isalpha():
            print("Error: Student name must contain only letters.")
        else:
            return name


def get_score(assessment_name):
    while True:
        try:
            score = float(input(f"Enter {assessment_name} score: "))

            if 0 <= score <= 100:
                return score
            else:
                print("Error: Score must be between 0 and 100.")

        except ValueError:
            print("Error: Please enter a valid number.")


def main():
    print("=" * 35)
    print("     STUDENT GRADE CALCULATOR")
    print("=" * 35)

    student_name = get_student_name()

    assignment_score = get_score("Assignment")
    test_score = get_score("Test")
    examination_score = get_score("Examination")

    print(f"\nStudent name: {student_name}")
    print(f"Assignment score: {assignment_score}")
    print(f"Test score: {test_score}")
    print(f"Examination score: {examination_score}")


if __name__ == "__main__":
    main()