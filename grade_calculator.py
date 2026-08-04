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


def calculate_total(scores):
    return sum(scores)


def calculate_average(total, number_of_scores):
    return total / number_of_scores


def calculate_grade(average):
    if average >= 70:
        return "A"
    elif average >= 60:
        return "B"
    elif average >= 50:
        return "C"
    elif average >= 45:
        return "D"
    elif average >= 40:
        return "E"
    else:
        return "F"


def get_status(average):
    if average >= 40:
        return "Pass"
    else:
        return "Fail"


def main():
    print("=" * 35)
    print("     STUDENT GRADE CALCULATOR")
    print("=" * 35)

    student_name = get_student_name()

    assignment_score = get_score("Assignment")
    test_score = get_score("Test")
    examination_score = get_score("Examination")

    scores = [assignment_score, test_score, examination_score]

    total_score = calculate_total(scores)
    average_score = calculate_average(total_score, len(scores))

    grade = calculate_grade(average_score)
    status = get_status(average_score)

    print(f"\nStudent name: {student_name}")
    print(f"Total score: {total_score}")
    print(f"Average score: {average_score:.2f}")
    print(f"Grade: {grade}")
    print(f"Status: {status}")


if __name__ == "__main__":
    main()