# student_info.py
import tkinter as tk

def display_student_info(student_data):
    # Create a new window for student information
    info_window = tk.Toplevel()
    info_window.title("Student Information")
    info_window.geometry("400x300")
    info_window.configure(bg="#eaf0f1")

    title_font = ("Helvetica", 16, "bold")
    label_font = ("Helvetica", 12)

    tk.Label(
        info_window, text="Student Information", font=title_font, fg="#2c3e50", bg="#eaf0f1"
    ).pack(pady=10)

    info_frame = tk.Frame(info_window, bg="#eaf0f1")
    info_frame.pack(pady=10)

    # Display each piece of student data
    for idx, (field, value) in enumerate(student_data.items()):
        tk.Label(info_frame, text=f"{field}: {value}", font=label_font, bg="#eaf0f1").grid(row=idx, column=0, sticky="w")
