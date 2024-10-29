import tkinter as tk
from tkinter import messagebox
import sqlite3
import time
from threading import Timer


# Function to open the exam window
def open_exam_window(student_data):
	# Create the exam window
	exam_window = tk.Toplevel()
	exam_window.title("Exam Window")
	exam_window.geometry("800x500")
	exam_window.configure(bg="#ffffff")

	# Fonts
	title_font = ("Helvetica", 16, "bold")
	question_font = ("Helvetica", 12)
	option_font = ("Helvetica", 10)

	# Student Info (Top Left)
	student_info = f"Name: {student_data['Name']}    ID: {student_data['ID']}"
	tk.Label(exam_window, text=student_info, font=title_font, bg="#ffffff").place(x=20, y=20)

	# Timer (Top Right)
	timer_label = tk.Label(exam_window, text="10:00", font=title_font, bg="#ffffff")
	timer_label.place(x=700, y=20)

	# Timer countdown function
	def countdown(time_left):
		mins, secs = divmod(time_left, 60)
		timer_label.config(text=f"{mins:02d}:{secs:02d}")
		if time_left > 0:
			exam_window.after(1000, countdown, time_left - 1)
		else:
			messagebox.showinfo("Time's Up", "The exam time has finished!")
			exam_window.destroy()

	# Start the countdown
	countdown(600)  # 10 minutes in seconds

	# Questions and options
	questions = [
		"1. What is the main component of a computer that performs calculations and processes instructions?",
		"2. What is the main component of a computer that performs calculations and processes instructions?"
	]
	options = [
		["A) RAM", "B) Hard Drive", "C) CPU", "D) Power Supply"],
		["A) RAM", "B) Hard Drive", "C) CPU", "D) Power Supply"]
	]

	# Create a variable to store selected answers
	selected_answers = [tk.StringVar() for _ in questions]

	# Display questions and options
	for i, question in enumerate(questions):
		tk.Label(exam_window, text=question, font=question_font, bg="#ffffff").place(x=20, y=80 + (i * 100))

		for j, option in enumerate(options[i]):
			tk.Radiobutton(exam_window, text=option, variable=selected_answers[i], value=option, font=option_font,
			               bg="#ffffff").place(x=40 + j * 150, y=110 + (i * 100))

	# Submit Button
	submit_button = tk.Button(exam_window, text="Submit", font=("Helvetica", 12, "bold"), bg="#74b9ff", fg="#ffffff",
	                          command=lambda: submit_exam(selected_answers, exam_window))
	submit_button.place(x=350, y=400)


# Function to handle exam submission
def submit_exam(selected_answers, exam_window):
	answers = [answer.get() for answer in selected_answers]
	messagebox.showinfo("Exam Submission", f"Your answers: {answers}")
	exam_window.destroy()


# Example usage: Call this function with student data
if __name__ == "__main__":
	# Sample student data; replace with actual data from your database
	student_data = {
		'Name': 'Masum',
		'ID': '573'
	}
	open_exam_window(student_data)
	tk.mainloop()
