from datetime import datetime
from typing import Dict, List, Optional
class Student:
    def __init__(self, student_id: int, name: str, email: str):
        self.student_id = student_id
        self.name = name
        self.email = email
        self.courses: List[str] = []
        self.grades: Dict[str, float] = {}

    def add_course(self, course_name: str) -> None:
        """
        Add a course to the student's course list.
        Args:
            course_name: The name of the course to add
        """
        if course_name not in self.courses:
            self.courses.append(course_name)

    def remove_course(self, course_name: str) -> bool:
        """
        Remove a course from the student's course list.
        Args:
            course_name: The name of the course to remove
        Returns:
            bool: True if the course was removed, False if it wasn't found
        """
        if course_name in self.courses:
            self.courses.remove(course_name)
            return True
        return False

    def add_grade(self, course_name: str, grade: float) -> None:
        """
        Add a grade for a specific course.
        Args:
            course_name: The name of the course
            grade: The grade to add (0-100)
        Raises:
            ValueError: If the grade is not between 0 and 100
        """
        if not 0 <= grade <= 100:
            raise ValueError("Grade must be between 0 and 100")
        self.grades[course_name] = grade

    def calculate_gpa(self) -> float:
        """
        Calculate the student's GPA.
        Returns:
            float: The calculated GPA (0-4.0 scale)
        """
        if not self.grades:
            return 0.0
        
        total_points = 0
        for grade in self.grades.values():
            if grade >= 90:
                total_points += 4.0
            elif grade >= 80:
                total_points += 3.0
            elif grade >= 70:
                total_points += 2.0
            elif grade >= 60:
                total_points += 1.0
        
        return round(total_points / len(self.grades), 2)

    def get_course_load(self) -> int:
        """
        Get the number of courses the student is enrolled in.
        Returns:
            int: Number of courses
        """
        return len(self.courses)
    

    

class StudentRegistry:
    def __init__(self):
        self.students: Dict[int, Student] = {}

    def add_student(self, student: Student) -> None:
        """
        Add a student to the registry.
        Args:
            student: The student object to add
        """
        self.students[student.student_id] = student

    def get_student(self, student_id: int) -> Optional[Student]:
        """
        Retrieve a student from the registry by their ID.
        Args:
            student_id: The ID of the student to retrieve
        Returns:
            Optional[Student]: The student object if found, None otherwise
        """
        return self.students.get(student_id)

    def generate_report(self) -> str:
        """
        Generate a report of all students and their GPAs.
        Returns:
            str: A formatted report string
        """
        report = "Student Performance Report\n"
        report += f"Generated on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n"
        report += "-" * 50 + "\n"
        
        for student in self.students.values():
            report += f"Name: {student.name}\n"
            report += f"ID: {student.student_id}\n"
            report += f"Courses: {len(student.courses)}\n"
            report += f"GPA: {student.calculate_gpa()}\n"
            report += "-" * 25 + "\n"
        
        return report     


if __name__ == "__main__":

    
    # Create a registry
    registry = StudentRegistry()
    
    # Create some test students
    student1 = Student(1001, "John Doe", "john@example.com")
    student2 = Student(1002, "Jane Smith", "jane@example.com")
    student3 = Student(1003, "Bob Johnson", "bob@example.com")
    
    # Add courses and grades for student1
    student1.add_course("Math")
    student1.add_course("Physics")
    student1.add_grade("Math", 95)  # GPA: 4.0
    student1.add_grade("Physics", 88)  # GPA: 3.0
    # Expected GPA: 3.5
    
    # Add courses and grades for student2
    student2.add_course("Chemistry")
    student2.add_course("Biology")
    student2.add_course("English")
    student2.add_grade("Chemistry", 92)  # GPA: 4.0
    student2.add_grade("Biology", 85)  # GPA: 3.0
    student2.add_grade("English", 78)  # GPA: 2.0
    # Expected GPA: 3.0
    
    # Add courses and grades for student3
    student3.add_course("History")
    student3.add_course("Literature")
    student3.add_grade("History", 75)  # GPA: 2.0
    student3.add_grade("Literature", 82)  # GPA: 3.0
    # Expected GPA: 2.5
    
    # Add students to registry
    registry.add_student(student1)
    registry.add_student(student2)
    registry.add_student(student3)
        

    
    
