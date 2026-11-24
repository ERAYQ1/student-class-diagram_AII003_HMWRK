# Student Class Diagram

A simple object-oriented Python project implementing a UML Student Class Diagram with three classes: `Department`, `Course`, and `Student`.

**Author:** Eray Okuslug (20231882) — Near East University, Department of Computer Engineering

## Project Structure

- `department.py` – `Department` class
- `course.py` – `Course` class
- `student.py` – `Student` class
- `main.py` – Example usage script

## UML Class Diagram

```mermaid
classDiagram
    class Department {
        -str department_id
        -str department_name
        -list~Course~ courses
        +add_course(course: Course) bool
        +get_department_info() str
    }

    class Course {
        -str course_code
        -str course_name
        -int credits
        -list~Student~ enrolled_students
        +add_student(student: Student) bool
        +remove_student(student: Student) bool
        +get_course_info() str
    }

    class Student {
        -str student_id
        -str name
        -str email
        -float gpa
        -Department department
        -list~Course~ enrolled_courses
        +enroll_in_course(course: Course) bool
        +drop_course(course: Course) bool
        +update_gpa(new_gpa: float) None
        +get_student_info() str
    }

    Department "1" o-- "0..*" Course : offers
    Student "0..*" --> "1" Department : belongs to
    Student "0..*" -- "0..*" Course : enrolls in
```

## How to Run

```bash
python main.py
```
