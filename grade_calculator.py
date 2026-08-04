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


class StudentGradeCalculator:

    def __init__(self, name, assignment, test, examination):
        self.name = name
        self.assignment = assignment
        self.test = test
        self.examination = examination

    def calculate_total(self):
        return self.assignment + self.test + self.examination

    def calculate_average(self):
        return self.calculate_total() / 3

    def calculate_grade(self):
        average = self.calculate_average()

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

    def get_status(self):
        if self.calculate_average() >= 40:
            return "Pass"
        return "Fail"

    def display_result(self):
        print("\n" + "=" * 35)
        print("        STUDENT RESULT")
        print("=" * 35)
        print(f"Student Name : {self.name}")
        print(f"Assignment   : {self.assignment}")
        print(f"Test         : {self.test}")
        print(f"Examination  : {self.examination}")
        print(f"Total Score  : {self.calculate_total()}")
        print(f"Average      : {self.calculate_average():.2f}")
        print(f"Grade        : {self.calculate_grade()}")
        print(f"Status       : {self.get_status()}")


def main():

    print("=" * 35)
    print("     STUDENT GRADE CALCULATOR")
    print("=" * 35)

    student_name = get_student_name()

    assignment_score = get_score("Assignment")
    test_score = get_score("Test")
    examination_score = get_score("Examination")

    student = StudentGradeCalculator(
        student_name,
        assignment_score,
        test_score,
        examination_score
    )

    student.display_result()


if __name__ == "__main__":
    main()