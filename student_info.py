# student_info.py
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk  # For handling custom icon images

def display_student_info(student_data):
    # Create a new window for student information
    info_window = tk.Toplevel()
    info_window.title("Student Information")
    info_window.geometry("500x400")
    info_window.configure(bg="#eaf0f1")

    title_font = ("Helvetica", 16, "bold")
    label_font = ("Helvetica", 12)

    # Display a custom student icon
    icon_frame = tk.Frame(info_window, bg="#eaf0f1")
    icon_frame.pack(pady=10)

    # Load a placeholder image for the student icon
    try:
        student_icon = Image.open("stu.png")  # Replace with your icon file path
        student_icon = student_icon.resize((80, 80), Image.Resampling.LANCZOS)
        student_photo = ImageTk.PhotoImage(student_icon)
        icon_label = tk.Label(icon_frame, image=student_photo, bg="#eaf0f1")
        icon_label.image = student_photo  # Keep a reference
        icon_label.pack()
    except FileNotFoundError:
        icon_label = tk.Label(icon_frame, text="👤", font=("Helvetica", 40), bg="#eaf0f1")
        icon_label.pack()

    # Title Label
    tk.Label(
        info_window, text="Student Information", font=title_font, fg="#2c3e50", bg="#eaf0f1"
    ).pack(pady=5)

    # Frame for displaying student info
    info_frame = tk.Frame(info_window, bg="#eaf0f1")
    info_frame.pack(pady=10, padx=20, anchor="w")

    # Display each piece of student data
    for idx, (field, value) in enumerate(student_data.items()):
        tk.Label(info_frame, text=f"{field}: {value}", font=label_font, bg="#eaf0f1").grid(row=idx, column=0, sticky="w")

    # "Take Exam" button at the bottom
    take_exam_button = tk.Button(
        info_window, text="Take Exam", font=("Helvetica", 12, "bold"),
        bg="#55efc4", fg="#fff", relief="flat", width=15, cursor="hand2",
        activebackground="#00b894", activeforeground="white",
        command=lambda: start_exam(student_data)  # Placeholder function
    )
    take_exam_button.pack(pady=20)

# Placeholder function for the "Take Exam" button
def start_exam(student_data):
    messagebox.showinfo("Take Exam", f"{student_data.get('Name', 'Student')} is starting the exam!")

