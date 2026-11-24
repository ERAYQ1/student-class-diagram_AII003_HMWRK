"""Student module representing a university student."""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from course import Course
    from department import Department


class Student:
    """Represents a student belonging to a department and enrolled in courses."""

    def __init__(
        self,
        student_id: str,
        name: str,
        email: str,
        gpa: float,
        department: Department,
    ) -> None:
        if not student_id.strip():
            raise ValueError("student_id cannot be empty.")
        if not name.strip():
            raise ValueError("name cannot be empty.")
        if "@" not in email or not email.strip():
            raise ValueError("email must be a valid email address.")
        if not (0.0 <= gpa <= 4.0):
            raise ValueError("gpa must be between 0.0 and 4.0.")

        self.__student_id: str = student_id.strip()
        self.__name: str = name.strip()
        self.__email: str = email.strip()
        self.__gpa: float = float(gpa)
        self.__department: Department = department
        self.__enrolled_courses: list[Course] = []

    @property
    def student_id(self) -> str:
        """Return the student's unique identifier."""
        return self.__student_id

    @property
    def name(self) -> str:
        """Return the student's full name."""
        return self.__name

    @name.setter
    def name(self, value: str) -> None:
        if not value.strip():
            raise ValueError("name cannot be empty.")
        self.__name = value.strip()

    @property
    def email(self) -> str:
        """Return the student's email address."""
        return self.__email

    @email.setter
    def email(self, value: str) -> None:
        if "@" not in value or not value.strip():
            raise ValueError("email must be a valid email address.")
        self.__email = value.strip()

    @property
    def gpa(self) -> float:
        """Return the student's current GPA."""
        return self.__gpa

    @property
    def department(self) -> Department:
        """Return the department the student belongs to."""
        return self.__department

    @department.setter
    def department(self, value: Department) -> None:
        self.__department = value

    @property
    def enrolled_courses(self) -> list[Course]:
        """Return a shallow copy of the courses the student is enrolled in."""
        return list(self.__enrolled_courses)

    def enroll_in_course(self, course: Course) -> bool:
        """Enroll the student in a course and synchronize the course's roster.

        Returns True if enrolled successfully, False if already enrolled.
        """
        if course in self.__enrolled_courses:
            return False
        self.__enrolled_courses.append(course)
        if self not in course.enrolled_students:
            course.add_student(self)
        return True

    def drop_course(self, course: Course) -> bool:
        """Drop a course and synchronize the course's roster.

        Returns True if dropped successfully, False if not currently enrolled.
        """
        if course not in self.__enrolled_courses:
            return False
        self.__enrolled_courses.remove(course)
        if self in course.enrolled_students:
            course.remove_student(self)
        return True

    def update_gpa(self, new_gpa: float) -> None:
        """Update the student's GPA after validating the 0.0 - 4.0 range."""
        if not (0.0 <= new_gpa <= 4.0):
            raise ValueError("new_gpa must be between 0.0 and 4.0.")
        self.__gpa = float(new_gpa)

    def get_student_info(self) -> str:
        """Return a formatted summary of the student's profile and courses."""
        course_list = (
            ", ".join(f"{c.course_code} ({c.course_name})" for c in self.__enrolled_courses)
            if self.__enrolled_courses
            else "None"
        )
        return (
            f"Student ID        : {self.__student_id}\n"
            f"Name              : {self.__name}\n"
            f"Email             : {self.__email}\n"
            f"GPA               : {self.__gpa:.2f}\n"
            f"Department        : {self.__department.department_name} ({self.__department.department_id})\n"
            f"Enrolled Courses  : {course_list}"
        )

    def __repr__(self) -> str:
        return (
            f"Student(student_id={self.__student_id!r}, "
            f"name={self.__name!r}, gpa={self.__gpa!r})"
        )
