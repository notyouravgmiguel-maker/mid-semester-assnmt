"""
main.py
Interactive Student Course Management System (Console Interface)
COS201 Programming I Mid-Semester Lab Assessment Project
MIVA Open University
"""

import sys
from course import Course
from course_manager import CourseManager

def print_banner():
    """Displays the welcome banner."""
    print("=" * 60)
    print("   MIVA OPEN UNIVERSITY - STUDENT COURSE MANAGEMENT SYSTEM")
    print("               COS201: PROGRAMMING I LAB")
    print("=" * 60)

def print_menu():
    """Displays the main options menu."""
    print("\n--- MAIN MENU ---")
    print("1. Add New Course")
    print("2. Display All Courses")
    print("3. Search for a Course by Code")
    print("4. Calculate Total Credit Units")
    print("5. Save Courses to File")
    print("6. Load Courses from File")
    print("7. Exit Program")
    print("-" * 30)

def prompt_non_empty(prompt_text: str) -> str:
    """Repeatedly prompts until user enters non-empty text."""
    while True:
        value = input(prompt_text).strip()
        if value:
            return value
        print("  [!] Input cannot be blank. Please try again.")

def prompt_positive_int(prompt_text: str) -> int:
    """
    Prompts for a positive integer with exception handling.
    Demonstrates handling invalid input via try-except.
    """
    while True:
        val_str = input(prompt_text).strip()
        try:
            val = int(val_str)
            if val <= 0:
                print("  [!] Credit units must be greater than 0.")
                continue
            return val
        except ValueError:
            print("  [!] Invalid input: please enter a whole number (e.g., 2, 3).")

def handle_add_course(manager: CourseManager):
    """Handles adding a new course with input validation."""
    print("\n-- [1] Add New Course --")
    code = prompt_non_empty("Enter Course Code (e.g., COS201): ")
    
    # Check duplicate before asking for more info
    if manager.find_course(code):
        print(f"  [X] Course with code '{code.upper()}' is already registered!")
        return

    title = prompt_non_empty("Enter Course Title (e.g., Programming I): ")
    units = prompt_positive_int("Enter Credit Units (e.g., 3): ")

    try:
        new_course = Course(code, title, units)
        manager.add_course(new_course)
        print(f"  [SUCCESS] Added: {new_course}")
    except ValueError as e:
        print(f"  [ERROR] Error creating course: {e}")

def handle_search_course(manager: CourseManager):
    """Handles searching for a course using recursive lookup."""
    print("\n-- [3] Search Course by Code --")
    code = prompt_non_empty("Enter Course Code to search: ")
    course = manager.find_course(code)
    
    if course:
        print("\n  [SUCCESS] Course Found:")
        print(f"      Code:         {course.code}")
        print(f"      Title:        {course.title}")
        print(f"      Credit Units: {course.units}")
    else:
        print(f"  [NOT FOUND] Course with code '{code.upper()}' was not found.")

def handle_total_units(manager: CourseManager):
    """Displays total credit units calculated recursively."""
    print("\n-- [4] Total Credit Units --")
    total = manager.calculate_total_units_recursive()
    count = len(manager.get_all_courses())
    print(f"  Total Courses Registered: {count}")
    print(f"  Total Credit Units:       {total}")

def handle_save(manager: CourseManager):
    """Handles saving courses to a file."""
    print("\n-- [5] Save Courses to File --")
    filename = input("Enter filename [default: courses.txt]: ").strip()
    if not filename:
        filename = "courses.txt"
    success, message = manager.save_to_file(filename)
    prefix = "[SUCCESS]" if success else "[ERROR]"
    print(f"  {prefix} {message}")

def handle_load(manager: CourseManager):
    """Handles loading courses from a file."""
    print("\n-- [6] Load Courses from File --")
    filename = input("Enter filename [default: courses.txt]: ").strip()
    if not filename:
        filename = "courses.txt"
    success, message = manager.load_from_file(filename)
    prefix = "[SUCCESS]" if success else "[ERROR]"
    print(f"  {prefix} {message}")

def main():
    """Main program loop."""
    print_banner()
    manager = CourseManager()

    # Pre-populate with sample course for convenience (optional, can be empty)
    # The user can also load existing files.
    
    while True:
        print_menu()
        choice = input("Enter your choice (1-7): ").strip()

        if choice == "1":
            handle_add_course(manager)
        elif choice == "2":
            print("\n-- [2] All Registered Courses --")
            manager.display_courses()
        elif choice == "3":
            handle_search_course(manager)
        elif choice == "4":
            handle_total_units(manager)
        elif choice == "5":
            handle_save(manager)
        elif choice == "6":
            handle_load(manager)
        elif choice == "7":
            print("\nThank you for using the Student Course Management System. Goodbye!")
            sys.exit(0)
        else:
            print("  [!] Invalid choice. Please enter a number between 1 and 7.")

if __name__ == "__main__":
    main()

