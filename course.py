"""Course module representing an academic course."""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from student import Student


class Course:
    """Represents a course that students can enroll in."""

    def __init__(self, course_code: str, course_name: str, credits: int) -> None:
        if not course_code.strip():
            raise ValueError("course_code cannot be empty.")
        if not course_name.strip():
            raise ValueError("course_name cannot be empty.")
        if credits <= 0:
            raise ValueError("credits must be a positive integer.")

        self.__course_code: str = course_code.strip()
        self.__course_name: str = course_name.strip()
        self.__credits: int = credits
        self.__enrolled_students: list[Student] = []

    @property
    def course_code(self) -> str:
        """Return the unique course code."""
        return self.__course_code

    @property
    def course_name(self) -> str:
        """Return the name of the course."""
        return self.__course_name

    @course_name.setter
    def course_name(self, value: str) -> None:
        if not value.strip():
            raise ValueError("course_name cannot be empty.")
        self.__course_name = value.strip()

    @property
    def credits(self) -> int:
        """Return the credit value of the course."""
        return self.__credits

    @credits.setter
    def credits(self, value: int) -> None:
        if value <= 0:
            raise ValueError("credits must be a positive integer.")
        self.__credits = value

    @property
    def enrolled_students(self) -> list[Student]:
        """Return a shallow copy of the students enrolled in this course."""
        return list(self.__enrolled_students)

    def add_student(self, student: Student) -> bool:
        """Enroll a student in this course and synchronize the student's record.

        Returns True if the student was added, False if already enrolled.
        """
        if student in self.__enrolled_students:
            return False
        self.__enrolled_students.append(student)
        if self not in student.enrolled_courses:
            student.enroll_in_course(self)
        return True

    def remove_student(self, student: Student) -> bool:
        """Remove a student from this course and synchronize the student's record.

        Returns True if the student was removed, False if not enrolled.
        """
        if student not in self.__enrolled_students:
            return False
        self.__enrolled_students.remove(student)
        if self in student.enrolled_courses:
            student.drop_course(self)
        return True

    def get_course_info(self) -> str:
        """Return a formatted summary of the course and its enrolled students."""
        student_list = (
            ", ".join(f"{s.name} ({s.student_id})" for s in self.__enrolled_students)
            if self.__enrolled_students
            else "None"
        )
        return (
            f"Course Code       : {self.__course_code}\n"
            f"Course Name       : {self.__course_name}\n"
            f"Credits           : {self.__credits}\n"
            f"Enrolled ({len(self.__enrolled_students)})      : {student_list}"
        )

    def __repr__(self) -> str:
        return (
            f"Course(course_code={self.__course_code!r}, "
            f"course_name={self.__course_name!r}, credits={self.__credits!r})"
        )
