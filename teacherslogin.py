import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk


def open_teacher_login():
    # Create a new window for the teacher login
    login_window = tk.Toplevel()
    login_window.title("Teacher Login")
    login_window.geometry("800x500")
    login_window.configure(bg="#d3d3d3")  # Matte grey background for the main window

    # Canvas for background effect with a light blue gradient color
    canvas = tk.Canvas(login_window, width=800, height=500, bg="#b0e0e6")  # Light blue shade
    canvas.pack(fill="both", expand=True)

    # Add gradient effect or background image
    gradient_img = Image.new("RGB", (800, 500), "#b0e0e6")  # Light blue background
    gradient_photo = ImageTk.PhotoImage(gradient_img)
    canvas.create_image(0, 0, anchor="nw", image=gradient_photo)
    login_window.gradient_photo = gradient_photo  # Keep reference to avoid garbage collection

    # Load back button icon
    back_icon_path = "left-arrow.png"  # Update with your actual icon path
    back_icon = Image.open(back_icon_path)
    back_icon = back_icon.resize((20, 20), Image.Resampling.LANCZOS)  # Resizing icon
    back_icon_photo = ImageTk.PhotoImage(back_icon)

    # Back Button
    back_button = tk.Button(
        login_window, image=back_icon_photo, command=login_window.destroy,
        bg="#b0e0e6", relief="flat", cursor="hand2", borderwidth=0
    )
    back_button.image = back_icon_photo  # Keep reference to avoid garbage collection
    back_button.place(x=10, y=10)  # Position the button at the top-left corner

    # Frame for login form
    frame = tk.Frame(login_window, bg="white", width=300, height=250)
    frame.place(relx=0.5, rely=0.5, anchor="center")

    # Title Label
    title_label = tk.Label(frame, text="Teacher Login", font=("Helvetica", 16, "bold"), bg="white", fg="#2c3e50")
    title_label.place(x=100, y=20)

    # User Label and Entry
    user_label = tk.Label(frame, text="User", font=("Helvetica", 10), bg="white", fg="#333")
    user_label.place(x=20, y=60)
    user_entry = tk.Entry(frame, width=25, font=("Helvetica", 10), bg="#f0f2f5", bd=0)
    user_entry.place(x=100, y=60)

    # Password Label and Entry
    pass_label = tk.Label(frame, text="Password", font=("Helvetica", 10), bg="white", fg="#333")
    pass_label.place(x=20, y=100)
    pass_entry = tk.Entry(frame, width=25, font=("Helvetica", 10), show="*", bg="#f0f2f5", bd=0)
    pass_entry.place(x=100, y=100)

    # Login Button
    login_button = tk.Button(
        frame, text="Login", font=("Helvetica", 10, "bold"),
        bg="#a29bfe", fg="white", width=12, height=1, bd=0,
        activebackground="#6c5ce7", activeforeground="white",
        command=lambda: messagebox.showinfo("Login", "Login clicked")
    )
    login_button.place(x=100, y=160)

    login_window.mainloop()


def check_login(username, password, login_window):
    # Hardcoded credentials for admin login
    if username == "admin" and password == "admin":
        messagebox.showinfo("Login", "Login successful")
        login_window.destroy()  # Close the login window
    else:
        messagebox.showerror("Login Error", "Invalid username or password")
