# student_registration.py
import tkinter as tk
from tkinter import messagebox
import sqlite3
from student_info import display_student_info  # Import the function to show student info

# Function to connect to database and create a table for students if it doesn't exist
def initialize_database():
    conn = sqlite3.connect("students.db")
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            university TEXT,
            semester TEXT,
            year TEXT,
            intake TEXT,
            student_id TEXT,
            password TEXT
        )
    ''')
    conn.commit()
    conn.close()

# Function to open student login and registration window
def open_student_window(parent_root):
    student_window = tk.Toplevel(parent_root)
    student_window.title("Student Portal")
    student_window.geometry("500x400")
    student_window.configure(bg="#f0f2f5")

    # Fonts
    title_font = ("Helvetica", 20, "bold")
    label_font = ("Helvetica", 12)

    # Title Label
    title_label = tk.Label(
        student_window, text="Student Portal", fg="#2c3e50", font=title_font, bg="#eaf0f1"
    )
    title_label.pack(pady=20)

    # Login Section
    login_frame = tk.Frame(student_window, bg="#eaf0f1")
    login_frame.pack(pady=10)

    tk.Label(login_frame, text="Student ID:", font=label_font, bg="#eaf0f1").grid(row=0, column=0, pady=5, sticky="e")
    student_id_entry = tk.Entry(login_frame, width=25, font=("Helvetica", 10))
    student_id_entry.grid(row=0, column=1, pady=5)

    tk.Label(login_frame, text="Password:", font=label_font, bg="#eaf0f1").grid(row=1, column=0, pady=5, sticky="e")
    password_entry = tk.Entry(login_frame, width=25, font=("Helvetica", 10), show="*")
    password_entry.grid(row=1, column=1, pady=5)

    # Login Button
    login_button = tk.Button(
        login_frame, text="Login", font=("Helvetica", 12, "bold"),
        bg="#a29bfe", fg="#fff", relief="flat", width=10, height=1, cursor="hand2",
        activebackground="#6c5ce7", activeforeground="white",
        command=lambda: messagebox.showinfo("Login", "Login Successful")  # Placeholder functionality
    )
    login_button.grid(row=2, column=0, columnspan=2, pady=10)

    # Divider Line
    tk.Label(student_window, text="OR", font=("Helvetica", 12), bg="#eaf0f1").pack(pady=5)

    # Register Section
    register_button = tk.Button(
        student_window, text="Register as New Student", font=("Helvetica", 12, "bold"),
        bg="#55efc4", fg="#fff", relief="flat", width=20, height=2, cursor="hand2",
        activebackground="#00b894", activeforeground="white",
        command=lambda: open_registration_window(student_window)
    )
    register_button.pack(pady=10)

# Registration Window Function
def open_registration_window(parent):
    registration_window = tk.Toplevel(parent)
    registration_window.title("Student Registration")
    registration_window.geometry("500x500")
    registration_window.configure(bg="#eaf0f1")

    # Fonts
    title_font = ("Helvetica", 18, "bold")
    label_font = ("Helvetica", 12)

    # Title Label
    tk.Label(
        registration_window, text="New Student Registration", font=title_font,
        fg="#2c3e50", bg="#eaf0f1"
    ).pack(pady=20)

    # Registration Form
    form_frame = tk.Frame(registration_window, bg="#eaf0f1")
    form_frame.pack(pady=10)

    fields = ["Name", "University", "Semester", "Year", "Intake", "Student ID", "Password"]
    entries = {}

    for idx, field in enumerate(fields):
        tk.Label(form_frame, text=f"{field}:", font=label_font, bg="#eaf0f1").grid(row=idx, column=0, pady=5, sticky="e")
        entry = tk.Entry(form_frame, width=25, font=("Helvetica", 10), show="*" if field == "Password" else "")
        entry.grid(row=idx, column=1, pady=5)
        entries[field] = entry

    # Register Button
    register_button = tk.Button(
        registration_window, text="Register", font=("Helvetica", 12, "bold"),
        bg="#74b9ff", fg="#fff", relief="flat", width=15, height=2, cursor="hand2",
        activebackground="#0984e3", activeforeground="white",
        command=lambda: register_student(entries, registration_window)
    )
    register_button.pack(pady=20)

# Register the student and save data to the database
def register_student(entries, registration_window):
    # Retrieve data from entries
    student_data = {field: entry.get() for field, entry in entries.items()}

    # Insert data into database
    conn = sqlite3.connect("students.db")
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO students (name, university, semester, year, intake, student_id, password)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    ''', (student_data["Name"], student_data["University"], student_data["Semester"],
          student_data["Year"], student_data["Intake"], student_data["Student ID"],
          student_data["Password"]))
    conn.commit()
    conn.close()

    # Show success message and display student information window
    messagebox.showinfo("Registration", "Registration Successful")
    display_student_info(student_data)  # Call the function to open student info window
    registration_window.destroy()

# Main function to initialize the main window
def main():
    root = tk.Tk()
    root.title("Main Application")
    root.geometry("300x200")

    # Initialize the database
    initialize_database()

    # Open student portal
    student_button = tk.Button(root, text="Student Portal", command=lambda: open_student_window(root))
    student_button.pack(pady=50)

    root.mainloop()

if __name__ == "__main__":
    main()
