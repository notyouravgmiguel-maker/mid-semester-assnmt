# COS201 Programming I: Mid-Semester Lab Assessment Project
## Student Course Management (Mini-System)
**Institution:** MIVA Open University  
**Course:** COS201 - Programming I  

---

## Project Overview
The **Student Course Management System** allows students to register, display, search, compute credit units, and persist semester courses to disk.

The solution provides **both**:
1. **Interactive Console Menu Interface** (`main.py`)
2. **Graphical User Interface (GUI)** (`gui.py`)

Both interfaces share the exact same clean Object-Oriented backend (`course.py` and `course_manager.py`).

---

## Project Architecture

| File | Purpose | Key Concepts |
|---|---|---|
| [`course.py`](course.py) | Blueprint for an individual Course | Classes, Objects, Constructors (`__init__`), String Processing (`.strip()`, `.upper()`, `.title()`), Validation |
| [`course_manager.py`](course_manager.py) | Manages collection of courses | Lists, Iteration (`for`/`enumerate`), **Recursion** (`_search_recursive`, `calculate_total_units_recursive`), File I/O (`open()`, `with`), Exception Handling |
| [`main.py`](main.py) | Text-based interactive menu | Loops (`while True`), Decision logic (`if/elif/else`), Input validation (`try/except ValueError`) |
| [`gui.py`](gui.py) | Graphical interface | Event-driven programming, `tkinter` & `ttk`, Treeview tables, File Dialogs |
| `courses.txt` | Persistent storage file | CSV-formatted file storage (`CODE,TITLE,UNITS`) |

---

## How to Run the Application

Open your terminal / command prompt in this directory (`c:\wamp\www\miv`) and run either:

### Option A: Run the Console Version
```bash
python main.py
```

### Option B: Run the Graphical User Interface (GUI)
```bash
python gui.py
```

---

## Verification of Project Requirements

| Requirement | Implementation in Code |
|---|---|
| **1. Classes & Objects** | `Course` class in `course.py`, `CourseManager` class in `course_manager.py` |
| **2. Add Course** | `manager.add_course()` with duplicate prevention |
| **3. Display All Courses** | `manager.display_courses()` formatting a table |
| **4. Search Course** | `manager.find_course()` utilizing recursive binary/linear scan |
| **5. Compute Credit Units** | `manager.calculate_total_units_recursive()` |
| **6. File Saving & Loading** | `save_to_file()` and `load_from_file()` with exception protection |
| **7. Iteration (Loops)** | `while True` in menu; `for` loop in displaying courses and loading lines |
| **8. Recursion** | `_search_recursive(code, index)` and `calculate_total_units_recursive(index)` |
| **9. Exception Handling** | `try...except ValueError` on inputs; `try...except Exception` on file reading/writing |
| **10. String Processing** | `.strip()` removes leading/trailing spaces; `.upper()` normalizes course codes; `.title()` formats course titles |

---

## Lab Defense / Oral Q&A Cheat Sheet (For Your Presentation)

If your lecturer asks you about your code during grading, here are simple answers:

1. **"What is the difference between a class and an object in your code?"**
   > *"The class is the template (e.g. `Course` in `course.py`), while an object is an actual instance created from it, such as `Course('COS201', 'Programming I', 3)`."*

2. **"Where and why did you use recursion?"**
   > *"I used recursion in `course_manager.py` for searching a course (`_search_recursive`) and calculating total units (`calculate_total_units_recursive`). Instead of a standard loop, the function processes the current item and calls itself with `index + 1` until it reaches the base case (`index >= len(self.courses)`)."*

3. **"How does your program prevent crashes from bad user input?"**
   > *"In `main.py`, the `prompt_positive_int()` function wraps input conversion in a `try...except ValueError` block. If a user enters letters instead of numbers for credit units, the exception is caught, a friendly warning is printed, and the program prompts again instead of crashing."*

4. **"How is file persistence implemented?"**
   > *"Courses are written to `courses.txt` in comma-separated format (`CODE,TITLE,UNITS`). The `load_from_file()` method reads each line, splits by comma, constructs new `Course` objects, and repopulates the manager."*

