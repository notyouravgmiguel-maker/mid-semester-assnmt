"""
course_manager.py
Manages the collection of courses for a student.
Demonstrates:
- List operations (storing, adding, retrieving)
- Iteration (loops)
- Recursion (recursive search and recursive units calculation)
- File I/O (saving to and loading from disk)
- Exception handling
"""

import os
from course import Course

class CourseManager:
    def __init__(self):
        # Internal structure to hold Course objects
        self.courses = []

    def add_course(self, course: Course) -> bool:
        """
        Adds a new course.
        Returns True if successful, False if course code already exists.
        """
        # Check if course code already exists (case-insensitive)
        if self.find_course(course.code):
            return False
        self.courses.append(course)
        return True

    def get_all_courses(self) -> list:
        """Returns the list of all recorded courses."""
        return self.courses

    def display_courses(self) -> None:
        """Displays all courses in a clean tabular format using iteration."""
        if not self.courses:
            print("\n  [i] No courses recorded yet.")
            return

        print("\n" + "=" * 55)
        print(f"{'No.':<4} {'Course Code':<15} {'Course Title':<25} {'Units':<6}")
        print("-" * 55)
        for i, c in enumerate(self.courses, start=1):
            print(f"{i:<4} {c.code:<15} {c.title:<25} {c.units:<6}")
        print("=" * 55)
        print(f"Total Courses: {len(self.courses)} | Total Units: {self.calculate_total_units_recursive()}")
        print("=" * 55)

    def find_course(self, code: str) -> Course | None:
        """Helper that initiates the recursive search."""
        target_code = code.strip().upper()
        return self._search_recursive(target_code, index=0)

    def _search_recursive(self, code: str, index: int = 0) -> Course | None:
        """
        Recursively searches for a course by its code.
        - Base Case 1: End of list reached (not found).
        - Base Case 2: Matching course code found.
        - Recursive Step: Inspect the next index (index + 1).
        """
        # Base Case 1: Reached the end of the list without finding a match
        if index >= len(self.courses):
            return None

        # Base Case 2: Found the course
        if self.courses[index].code == code:
            return self.courses[index]

        # Recursive Step: Check the next course
        return self._search_recursive(code, index + 1)

    def calculate_total_units_recursive(self, index: int = 0) -> int:
        """
        Recursively calculates the sum of all course credit units.
        - Base Case: index >= len(self.courses) -> 0
        - Recursive Step: current units + total of remainder
        """
        if index >= len(self.courses):
            return 0
        return self.courses[index].units + self.calculate_total_units_recursive(index + 1)

    def save_to_file(self, filename: str = "courses.txt") -> tuple[bool, str]:
        """
        Saves all courses to a text file.
        Uses exception handling for safety.
        """
        try:
            with open(filename, "w", encoding="utf-8") as f:
                for c in self.courses:
                    f.write(c.to_file_format())
            return True, f"Successfully saved {len(self.courses)} course(s) to '{filename}'."
        except Exception as e:
            return False, f"Failed to save file: {e}"

    def load_from_file(self, filename: str = "courses.txt") -> tuple[bool, str]:
        """
        Loads courses from a text file, parsing each line back into a Course object.
        Uses exception handling for missing files and malformed lines.
        """
        if not os.path.exists(filename):
            return False, f"File '{filename}' does not exist yet. Save some courses first!"

        try:
            loaded_courses = []
            with open(filename, "r", encoding="utf-8") as f:
                for line_num, line in enumerate(f, start=1):
                    line = line.strip()
                    if not line:
                        continue  # Skip empty lines
                    parts = line.split(",")
                    if len(parts) != 3:
                        continue  # Skip corrupted lines
                    code, title, units = parts
                    course = Course(code, title, int(units))
                    loaded_courses.append(course)

            self.courses = loaded_courses
            return True, f"Successfully loaded {len(self.courses)} course(s) from '{filename}'."
        except Exception as e:
            return False, f"Error reading file: {e}"

