"""
gui.py
Graphical User Interface (GUI) for Student Course Management System
Built using Python's standard tkinter library.
Demonstrates:
- Event-driven programming
- Object-Oriented GUI design
- Reusing Course and CourseManager backend logic seamlessly
"""

import tkinter as tk
from tkinter import ttk, messagebox, filedialog
from course import Course
from course_manager import CourseManager

class CourseManagementGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("MIVA Open University - Student Course Management")
        self.root.geometry("750x550")
        self.root.minsize(700, 500)

        # Initialize Backend Manager
        self.manager = CourseManager()

        # Build UI Components
        self._setup_styles()
        self._create_header()
        self._create_input_form()
        self._create_table_view()
        self._create_bottom_bar()

        # Update initial total units
        self._refresh_table()

    def _setup_styles(self):
        style = ttk.Style()
        style.theme_use("clam")
        style.configure("Treeview.Heading", font=("Helvetica", 10, "bold"))
        style.configure("Treeview", rowheight=26, font=("Helvetica", 10))

    def _create_header(self):
        header_frame = tk.Frame(self.root, bg="#1a365d", pady=12)
        header_frame.pack(fill="x")

        title_label = tk.Label(
            header_frame,
            text="Student Course Management System",
            font=("Helvetica", 16, "bold"),
            fg="white",
            bg="#1a365d"
        )
        title_label.pack()

        subtitle_label = tk.Label(
            header_frame,
            text="COS201: Programming I - Mid-Semester Lab Assessment",
            font=("Helvetica", 10),
            fg="#cbd5e1",
            bg="#1a365d"
        )
        subtitle_label.pack()

    def _create_input_form(self):
        form_frame = ttk.LabelFrame(self.root, text=" Add / Search Course ", padding=10)
        form_frame.pack(fill="x", padx=15, pady=10)

        # Row 1: Inputs
        ttk.Label(form_frame, text="Course Code:").grid(row=0, column=0, sticky="w", padx=5, pady=5)
        self.code_entry = ttk.Entry(form_frame, width=14)
        self.code_entry.grid(row=0, column=1, padx=5, pady=5)

        ttk.Label(form_frame, text="Course Title:").grid(row=0, column=2, sticky="w", padx=5, pady=5)
        self.title_entry = ttk.Entry(form_frame, width=28)
        self.title_entry.grid(row=0, column=3, padx=5, pady=5)

        ttk.Label(form_frame, text="Units:").grid(row=0, column=4, sticky="w", padx=5, pady=5)
        self.units_entry = ttk.Entry(form_frame, width=6)
        self.units_entry.grid(row=0, column=5, padx=5, pady=5)

        # Row 2: Action Buttons
        btn_frame = ttk.Frame(form_frame)
        btn_frame.grid(row=1, column=0, columnspan=6, pady=8)

        ttk.Button(btn_frame, text="Add Course", command=self._on_add).pack(side="left", padx=5)
        ttk.Button(btn_frame, text="Search by Code", command=self._on_search).pack(side="left", padx=5)
        ttk.Button(btn_frame, text="Clear Fields", command=self._clear_fields).pack(side="left", padx=5)

    def _create_table_view(self):
        table_frame = ttk.Frame(self.root, padding=10)
        table_frame.pack(fill="both", expand=True, padx=15)

        columns = ("no", "code", "title", "units")
        self.tree = ttk.Treeview(table_frame, columns=columns, show="headings", selectmode="browse")

        self.tree.heading("no", text="#")
        self.tree.heading("code", text="Course Code")
        self.tree.heading("title", text="Course Title")
        self.tree.heading("units", text="Credit Units")

        self.tree.column("no", width=40, anchor="center")
        self.tree.column("code", width=120, anchor="center")
        self.tree.column("title", width=380, anchor="w")
        self.tree.column("units", width=90, anchor="center")

        scrollbar = ttk.Scrollbar(table_frame, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscrollcommand=scrollbar.set)

        self.tree.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

    def _create_bottom_bar(self):
        bottom_frame = ttk.Frame(self.root, padding=10)
        bottom_frame.pack(fill="x", padx=15, pady=5)

        # File actions
        ttk.Button(bottom_frame, text="Save to File", command=self._on_save).pack(side="left", padx=5)
        ttk.Button(bottom_frame, text="Load from File", command=self._on_load).pack(side="left", padx=5)

        # Summary label (total courses & units)
        self.summary_label = ttk.Label(
            bottom_frame,
            text="Total Courses: 0 | Total Units: 0",
            font=("Helvetica", 10, "bold")
        )
        self.summary_label.pack(side="right", padx=10)

    def _refresh_table(self):
        """Clears and re-populates the table from manager."""
        for row in self.tree.get_children():
            self.tree.delete(row)

        for i, course in enumerate(self.manager.get_all_courses(), start=1):
            self.tree.insert("", "end", values=(i, course.code, course.title, course.units))

        total_units = self.manager.calculate_total_units_recursive()
        count = len(self.manager.get_all_courses())
        self.summary_label.config(text=f"Total Courses: {count} | Total Units: {total_units}")

    def _clear_fields(self):
        self.code_entry.delete(0, tk.END)
        self.title_entry.delete(0, tk.END)
        self.units_entry.delete(0, tk.END)

    def _on_add(self):
        code = self.code_entry.get().strip()
        title = self.title_entry.get().strip()
        units_str = self.units_entry.get().strip()

        if not code or not title or not units_str:
            messagebox.showwarning("Input Error", "All fields (Code, Title, Units) are required!")
            return

        try:
            units = int(units_str)
            if units <= 0:
                messagebox.showwarning("Input Error", "Credit units must be greater than 0.")
                return
        except ValueError:
            messagebox.showwarning("Input Error", "Credit units must be a valid whole number.")
            return

        # Attempt to create Course object
        try:
            course = Course(code, title, units)
        except ValueError as e:
            messagebox.showerror("Error", str(e))
            return

        if not self.manager.add_course(course):
            messagebox.showwarning("Duplicate Course", f"Course with code '{course.code}' already exists!")
            return

        self._refresh_table()
        self._clear_fields()
        messagebox.showinfo("Success", f"Course '{course.code}' added successfully!")

    def _on_search(self):
        code = self.code_entry.get().strip()
        if not code:
            messagebox.showwarning("Search", "Please enter a course code in the Code field to search.")
            return

        course = self.manager.find_course(code)
        if course:
            # Highlight item in table if present
            for item in self.tree.get_children():
                row_vals = self.tree.item(item, "values")
                if row_vals[1] == course.code:
                    self.tree.selection_set(item)
                    self.tree.see(item)
                    break
            messagebox.showinfo("Course Found", f"Code: {course.code}\nTitle: {course.title}\nUnits: {course.units}")
        else:
            messagebox.showinfo("Not Found", f"No course found with code '{code.upper()}'.")

    def _on_save(self):
        filename = filedialog.asksaveasfilename(
            defaultextension=".txt",
            filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")],
            initialfile="courses.txt"
        )
        if filename:
            success, msg = self.manager.save_to_file(filename)
            if success:
                messagebox.showinfo("Saved", msg)
            else:
                messagebox.showerror("Save Error", msg)

    def _on_load(self):
        filename = filedialog.askopenfilename(
            filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
        )
        if filename:
            success, msg = self.manager.load_from_file(filename)
            if success:
                self._refresh_table()
                messagebox.showinfo("Loaded", msg)
            else:
                messagebox.showerror("Load Error", msg)

def main():
    root = tk.Tk()
    app = CourseManagementGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()

