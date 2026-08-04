def get_student_name():
    while True:
        name = input("Enter student name: ").strip()

        if not name:
            print("Error: Student name cannot be empty.")
        elif not name.replace(" ", "").isalpha():
            print("Error: Student name must contain only letters.")
        else:
            return name


def main():
    print("=" * 35)
    print("     STUDENT GRADE CALCULATOR")
    print("=" * 35)

    student_name = get_student_name()

    print(f"\nStudent name: {student_name}")


if __name__ == "__main__":
    main()