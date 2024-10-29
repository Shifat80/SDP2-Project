import tkinter as tk
from teacherslogin import open_teacher_login  # Import function for teacher login
from stu_log import open_student_window       # Import function for student login and registration

# Main Window Setup
root = tk.Tk()
root.title("Exam Management System")
root.geometry("800x500")
root.configure(bg="#f0f2f5")

# Fonts
heading_font = ("Helvetica", 28, "bold")
subheading_font = ("Helvetica", 12)

# Canvas for Background Effect
canvas = tk.Canvas(root, width=800, height=500)
canvas.pack(fill="both", expand=True)

# Background Image
gradient_image = tk.PhotoImage(file="bg.png")  # Replace 'bg.png' with the actual path
canvas.create_image(0, 0, anchor="nw", image=gradient_image)

# Heading
heading = tk.Label(root, text="Welcome to the", fg="#2c3e50", font=heading_font, bg="#f0f2f5")
canvas.create_window(200, 100, anchor="w", window=heading)

# Title
title = tk.Label(root, text="Exam Management System", fg="#2c3e50", font=("Helvetica", 32, "bold"), bg="#f0f2f5")
canvas.create_window(200, 150, anchor="w", window=title)

# Description
description = tk.Label(root, text="This platform streamlines the entire examination process, from scheduling exams\n"
                                  "to managing student records, grading, and reporting",
                       fg="#5d6d7e", font=subheading_font, justify="left", bg="#f0f2f5")
canvas.create_window(200, 220, anchor="w", window=description)


# Button Styling Function
def create_button(text, command):
    button = tk.Button(
        root, text=text, command=command,
        bg="#a29bfe", fg="#fff", font=("Helvetica", 12, "bold"),
        relief="flat", width=12, height=2, cursor="hand2",
        activebackground="#6c5ce7", activeforeground="white"
    )
    return button


# Teacher and Student Buttons
teacher_button = create_button("Teacher", command=open_teacher_login)
canvas.create_window(200, 350, anchor="w", window=teacher_button)


student_button = create_button("Student", command=lambda: open_student_window(root))  # Pass root to stu_log.py
canvas.create_window(350, 350, anchor="w", window=student_button)

# Run the Main Loop
root.mainloop()
