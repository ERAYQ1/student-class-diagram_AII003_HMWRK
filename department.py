"""Department module representing an academic department."""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from course import Course


class Department:
    """Represents an academic department that aggregates courses."""

    def __init__(self, department_id: str, department_name: str) -> None:
        if not department_id.strip():
            raise ValueError("department_id cannot be empty.")
        if not department_name.strip():
            raise ValueError("department_name cannot be empty.")

        self.__department_id: str = department_id.strip()
        self.__department_name: str = department_name.strip()
        self.__courses: list[Course] = []

    @property
    def department_id(self) -> str:
        """Return the unique identifier of the department."""
        return self.__department_id

    @property
    def department_name(self) -> str:
        """Return the name of the department."""
        return self.__department_name

    @department_name.setter
    def department_name(self, value: str) -> None:
        if not value.strip():
            raise ValueError("department_name cannot be empty.")
        self.__department_name = value.strip()

    @property
    def courses(self) -> list[Course]:
        """Return a shallow copy of the courses offered by the department."""
        return list(self.__courses)

    def add_course(self, course: Course) -> bool:
        """Add a course to the department if it is not already listed.

        Returns True if the course was added, False if it was already present.
        """
        if course in self.__courses:
            return False
        self.__courses.append(course)
        return True

    def get_department_info(self) -> str:
        """Return a formatted summary of the department and its courses."""
        course_list = (
            ", ".join(f"{c.course_code} ({c.course_name})" for c in self.__courses)
            if self.__courses
            else "None"
        )
        return (
            f"Department ID   : {self.__department_id}\n"
            f"Department Name : {self.__department_name}\n"
            f"Courses ({len(self.__courses)})     : {course_list}"
        )

    def __repr__(self) -> str:
        return (
            f"Department(department_id={self.__department_id!r}, "
            f"department_name={self.__department_name!r})"
        )
