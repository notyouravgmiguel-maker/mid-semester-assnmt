"""
course.py
Represents a single academic course.
Demonstrates:
- Object-Oriented Programming (Classes & Objects)
- Data validation and string processing (trimming, casing)
"""

class Course:
    def __init__(self, code: str, title: str, units: int):
        """
        Constructor (__init__):
        Runs automatically when a new Course object is created.
        """
        # String processing: clean up spaces and enforce consistent casing
        self.code = code.strip().upper()
        self.title = title.strip().title()
        
        # Validation: units must be a positive integer
        if units <= 0:
            raise ValueError("Credit units must be a positive integer (greater than 0).")
        self.units = int(units)

    def to_file_format(self) -> str:
        """Converts course data into a comma-separated format for saving to a file."""
        return f"{self.code},{self.title},{self.units}\n"

    def __str__(self) -> str:
        """
        Controls how the course looks when printed.
        Example: [COS201] Programming I - 3 Units
        """
        return f"[{self.code}] {self.title} ({self.units} units)"

