"""Demonstration script for the UML Student Class Diagram project."""

from course import Course
from department import Department
from student import Student


def print_section(title: str) -> None:
    """Print a formatted section header."""
    print(f"\n{'=' * 55}")
    print(f" {title}")
    print(f"{'=' * 55}")


def main() -> None:
    # 1. Create a Department
    com_dept = Department("COM", "Computer Engineering - Near East University")

    # 2. Create Courses and add them to the Department (Aggregation)
    ict_course = Course("AII003", "Information and Communication Technologies", 3)
    oop_course = Course("AII409", "Object-Oriented Programming II", 4)
    cyber_course = Course("AII435", "Cybersecurity", 3)

    com_dept.add_course(ict_course)
    com_dept.add_course(oop_course)
    com_dept.add_course(cyber_course)

    print_section("Department Information")
    print(com_dept.get_department_info())

    # 3. Create a Student associated with the Department
    student = Student(
        student_id="20231882",
        name="Eray Okuslug",
        email="20231882@std.neu.edu.tr",
        gpa=3.50,
        department=com_dept,
    )

    # 4. Enroll the Student in Courses (Bidirectional Association)
    print_section("Enrolling Student in Courses")
    for course in (ict_course, oop_course, cyber_course):
        enrolled = student.enroll_in_course(course)
        print(f"Enrolled in {course.course_code} ({course.course_name}): {enrolled}")

    print_section("Student Information (After Enrollment)")
    print(student.get_student_info())

    print_section("Course Information (After Enrollment)")
    for course in (ict_course, oop_course, cyber_course):
        print(course.get_course_info())
        print("-" * 40)

    # 5. Drop a Course
    print_section("Dropping a Course")
    dropped = student.drop_course(cyber_course)
    print(f"Dropped {cyber_course.course_code} ({cyber_course.course_name}): {dropped}")

    # 6. Update GPA
    print_section("Updating Student GPA")
    old_gpa = student.gpa
    student.update_gpa(3.75)
    print(f"GPA updated: {old_gpa:.2f} -> {student.gpa:.2f}")

    # 7. Final state summary
    print_section("Final Student Information")
    print(student.get_student_info())

    print_section("Updated Course Roster for Dropped Course")
    print(cyber_course.get_course_info())


if __name__ == "__main__":
    main()
