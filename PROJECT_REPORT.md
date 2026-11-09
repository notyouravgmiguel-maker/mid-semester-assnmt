# MIVA OPEN UNIVERSITY
## FACULTY OF COMPUTING AND APPLIED SCIENCES
### DEPARTMENT OF COMPUTER SCIENCE
**COURSE CODE:** COS201  
**COURSE TITLE:** Programming I  
**ASSESSMENT:** Mid-Semester Lab Assessment Project  
**PROJECT TOPIC:** Student Course Management System (Mini-System)  
**STUDENT NAME:** [Insert Your Name Here]  
**MATRICULATION NO:** [Insert Your Matric Number Here]  
**DATE:** November 2026  

---

## 1. Executive Summary & What the System Does

The **Student Course Management System** is a software application designed to assist university students in keeping track of their registered courses for an academic semester. 

Managing course registrations manually or with informal notes often leads to errors, such as enrolling in duplicate course codes, miscalculating total registered credit units, or losing registration records. 

To solve this problem, this system provides a structured, automated tool that allows students to:
1. Register courses with their official course code, descriptive title, and assigned credit units.
2. View all enrolled courses in a clean, organized tabular format.
3. Rapidly search for any specific course using its unique course code.
4. Automatically compute the total credit units accumulated for the semester.
5. Save records permanently to a file on disk (`courses.txt`) so data is never lost.
6. Reload previously saved course records whenever the application is reopened.

The system is developed in **Python** following strict **Object-Oriented Programming (OOP)** principles, accompanied by robust error handling, input validation, string processing, and algorithmic recursion. The project includes both an interactive console menu interface (`main.py`) and a Graphical User Interface (`gui.py`).

---

## 2. System Architecture & Program Design

The application is structured into modular layers adhering to the **Separation of Concerns (SoC)** software engineering principle:

```
┌────────────────────────────────────────────────────────┐
│                   PRESENTATION LAYER                   │
│   main.py (Console Menu)   |   gui.py (Desktop GUI)    │
└───────────────────────────┬────────────────────────────┘
                            │
┌───────────────────────────▼────────────────────────────┐
│                    BUSINESS LOGIC                      │
│                course_manager.py                       │
│     (List Storage, Recursion, File I/O, Validation)    │
└───────────────────────────┬────────────────────────────┘
                            │
┌───────────────────────────▼────────────────────────────┐
│                      DATA MODEL                        │
│                      course.py                         │
│       (Course Class: Code, Title, Credit Units)        │
└───────────────────────────┬────────────────────────────┘
                            │
┌───────────────────────────▼────────────────────────────┐
│                  PERSISTENCE STORAGE                   │
│                      courses.txt                       │
└────────────────────────────────────────────────────────┘
```

### Key Components:
- **`Course` Class (`course.py`):** Acts as the data model blueprint representing an individual course entity. It encapsulates the course code, title, and credit units, and enforces input cleaning and validation upon instantiation.
- **`CourseManager` Class (`course_manager.py`):** Acts as the controller and storage manager. It stores `Course` objects in a dynamic internal list and provides member methods for addition, recursive search, tabular display, recursive unit summation, and disk persistence.
- **Console Interface (`main.py`):** Implements an intuitive text menu loop with 7 distinct numbered options, structured branching, and defensive exception handling.
- **Graphical Interface (`gui.py`):** Implements an event-driven desktop window utilizing Python's built-in `tkinter` and `ttk` libraries, complete with a structured `Treeview` data grid and file dialog pickers.

---

## 3. How Each Major Feature Works

### Feature 1: Add Course
- **Operation:** Accepts the course code (e.g., `COS201`), course title (e.g., `Programming I`), and credit units (e.g., `3`).
- **How it Works:** 
  1. The user inputs are sanitized using `.strip()` to eliminate extraneous whitespace.
  2. The course code is forced to uppercase via `.upper()`, and the title is normalized to title case via `.title()`.
  3. The credit units input is verified through a `try...except ValueError` block to ensure it is a positive integer greater than zero.
  4. Before insertion, `manager.find_course(code)` is executed to guarantee that duplicate course codes cannot be registered.
  5. Upon passing validation, a new `Course` instance is appended to the internal `self.courses` list.

### Feature 2: View All Courses
- **Operation:** Neatly displays all registered semester courses.
- **How it Works:**
  - If the list is empty, an informative notice (`[i] No courses recorded yet`) is displayed.
  - When records exist, the method iterates over `self.courses` using Python's `enumerate()` function. It outputs a formatted table complete with column headers (`No.`, `Course Code`, `Course Title`, `Units`), aligned spacing, and a summary footer showing the total courses and units count.

### Feature 3: Search Course by Code (Demonstrating Recursion)
- **Operation:** Locates a specific course by its code.
- **How it Works:**
  - Rather than relying on a basic loop, the system implements a recursive linear search algorithm (`_search_recursive`):
    - **Base Case 1:** If the current scan index reaches the length of the list (`index >= len(self.courses)`), the algorithm concludes that the course does not exist and returns `None`.
    - **Base Case 2:** If `self.courses[index].code == target_code`, a match is found and the corresponding `Course` object is returned immediately.
    - **Recursive Step:** If neither base case matches, the function calls itself with the next index (`index + 1`).
  - This satisfies academic recursion requirements and demonstrates functional call-stack decomposition.

### Feature 4: Compute Total Units (Demonstrating Recursion)
- **Operation:** Calculates the cumulative credit units for all registered courses.
- **How it Works:**
  - Computed using `calculate_total_units_recursive(index)`:
    - **Base Case:** When `index >= len(self.courses)`, it returns `0`.
    - **Recursive Step:** Returns `self.courses[index].units + calculate_total_units_recursive(index + 1)`.
  - The return value is presented clearly to the student to ensure they stay within academic credit load limits.

### Feature 5: Save to File
- **Operation:** Exports all active courses to permanent disk storage (`courses.txt`).
- **How it Works:**
  - Opens the target file using Python's context manager (`with open(filename, 'w', encoding='utf-8') as f:`).
  - Iterates through the list and invokes `course.to_file_format()`, writing records in clean comma-separated values (CSV) format:
    ```text
    COS201,Programming I,3
    GST101,Use Of English,2
    ```
  - The entire operation is wrapped in a `try...except Exception` block to catch OS or disk write permission errors.

### Feature 6: Load from File
- **Operation:** Reads previously saved course records into memory.
- **How it Works:**
  - Validates that the file exists using `os.path.exists()`.
  - Reads line-by-line, trims whitespace, skips blank rows, and splits each line by the comma delimiter into `[code, title, units]`.
  - Re-instantiates each record as a validated `Course` object and repopulates the manager's list.
  - Safely handles malformed lines without crashing.

### Feature 7: Exit Program
- **Operation:** Terminates the application gracefully.
- **How it Works:**
  - Displays a polite farewell message and exits cleanly via `sys.exit(0)`.

---

## 4. Technical Features & Best Practices Demonstrated

1. **Object-Oriented Programming (OOP):** Encapsulation of state and behaviors within dedicated classes (`Course` and `CourseManager`).
2. **Algorithmic Recursion:** Employed in searching and numerical summation to satisfy technical criteria.
3. **Defensive Programming & Exception Handling:** `try...except` blocks protect against non-numeric credit units (`ValueError`), missing files (`FileNotFoundError`), and disk I/O errors (`IOError`).
4. **Data Cleansing & String Manipulation:** Automated string methods (`.strip()`, `.upper()`, `.title()`) guarantee data consistency regardless of how casually a user types.
5. **Dual Interface Implementation:** Offers both an organized terminal CLI and a desktop GUI using `tkinter`.

---

## 5. Sample Program Run (Screenshots / Console Transcript)

```text
============================================================
   MIVA OPEN UNIVERSITY - STUDENT COURSE MANAGEMENT SYSTEM
               COS201: PROGRAMMING I LAB
============================================================

--- MAIN MENU ---
1. Add New Course
2. Display All Courses
3. Search for a Course by Code
4. Calculate Total Credit Units
5. Save Courses to File
6. Load Courses from File
7. Exit Program
------------------------------
Enter your choice (1-7): 2

-- [2] All Registered Courses --

=======================================================
No.  Course Code     Course Title              Units 
-------------------------------------------------------
1    COS201          Programming I             3     
2    GST101          Use Of English            2     
3    MTH201          Linear Algebra            3     
=======================================================
Total Courses: 3 | Total Units: 8
=======================================================
```

---

## 6. Conclusion
The Student Course Management System fulfills all functional, architectural, and technical guidelines specified for the COS201 Mid-Semester Lab Assessment. The application is modular, resilient to user error, memory-safe, and ready for deployment and academic evaluation.

