import tkinter as tk
from tkinter import ttk

# Define global variables
current_question_index = 0
answers = {}
question_history = []
current_theme = "light"

# Themes
light_theme = {
    "bg": "#f7f7f7",
    "fg": "black",
    "button_bg": "#8dd694",
    "button_fg": "black"
}

dark_theme = {
    "bg": "#2c2c2c",
    "fg": "white",
    "button_bg": "#4caf50",
    "button_fg": "white"
}

# Questions
questions = [
    ("size", ["Small", "Medium", "Large"]),
    ("energy", ["Low", "Moderate", "High"]),
    ("weather", ["Cold", "Mild", "Hot"]),
    ("temperament", ["Calm", "Playful", "Aggressive"]),
    ("age", ["Puppy", "Adult", "Senior"])
]

# Root window
root = tk.Tk()
root.title("Dog Activity Recommender")
root.geometry("400x500")

# Progress bar
progress_frame = tk.Frame(root)
progress_frame.pack(pady=10)
progress_var = tk.IntVar()
progress_bar = ttk.Progressbar(progress_frame, maximum=len(questions), variable=progress_var, length=300)
progress_bar.pack()

# Frames
welcome_frame = tk.Frame(root)
message_frame = tk.Frame(root)
question_frame = tk.Frame(root)
result_frame = tk.Frame(root)

# Welcome
tk.Label(welcome_frame, text="Welcome to the Dog Activity Recommender!", font=("Helvetica", 14)).pack(pady=20)
tk.Button(welcome_frame, text="Start", command=lambda: [welcome_frame.pack_forget(), message_frame.pack(), apply_theme()]).pack()

# Message
tk.Label(message_frame, text="Please answer a few questions about your dog.", font=("Helvetica", 12)).pack(pady=20)
tk.Button(message_frame, text="Continue", command=lambda: [message_frame.pack_forget(), progress_frame.pack(), show_question()]).pack()

# Show question
def show_question():
    global question_frame
    for widget in question_frame.winfo_children():
        widget.destroy()

    question_key, options = questions[current_question_index]
    tk.Label(question_frame, text=f"What is your dog's {question_key}?", font=("Helvetica", 12)).pack(pady=10)

    for option in options:
        tk.Button(question_frame, text=option, command=lambda opt=option: next_question(opt), width=20).pack(pady=2)

    nav_frame = tk.Frame(question_frame)
    nav_frame.pack(pady=10)

    if question_history:
        back_btn = tk.Button(nav_frame, text="⬅ Back", command=previous_question, width=15)
        back_btn.pack(side="left", padx=5)

    theme_btn = tk.Button(nav_frame, text="Toggle Theme", command=toggle_theme, width=15)
    theme_btn.pack(side="left", padx=5)

    question_frame.pack()
    apply_theme()

# Next question
def next_question(selected_option):
    global current_question_index

    question_key, _ = questions[current_question_index]
    answers[question_key] = selected_option
    question_history.append(current_question_index)

    current_question_index += 1
    progress_var.set(current_question_index)

    if current_question_index < len(questions):
        show_question()
    else:
        question_frame.pack_forget()
        progress_frame.pack_forget()
        message_frame.pack_forget()
        show_summary()

# Back button
def previous_question():
    global current_question_index

    if question_history:
        current_question_index = question_history.pop()
        show_question()

# Show summary
def show_summary():
    for widget in result_frame.winfo_children():
        widget.destroy()

    tk.Label(result_frame, text="Activity Recommendation", font=("Helvetica", 14)).pack(pady=10)

    recommendation = "Take your dog on a 30-minute walk!"  # Simple placeholder logic
    tk.Label(result_frame, text=recommendation).pack(pady=10)
    tk.Button(result_frame, text="Restart", command=restart_quiz).pack(pady=10)
    result_frame.pack()
    apply_theme()

# Restart
def restart_quiz():
    global current_question_index, answers, question_history
    current_question_index = 0
    answers = {}
    question_history = []
    result_frame.pack_forget()
    welcome_frame.pack()

# Theme application
def apply_theme():
    theme = light_theme if current_theme == "light" else dark_theme
    root.configure(bg=theme["bg"])

    for frame in [welcome_frame, message_frame, question_frame, result_frame, progress_frame]:
        frame.configure(bg=theme["bg"])
        for widget in frame.winfo_children():
            if isinstance(widget, (tk.Label, tk.Button, tk.Frame)):
                widget.configure(bg=theme["bg"], fg=theme["fg"])
                if isinstance(widget, tk.Button):
                    widget.configure(bg=theme["button_bg"], fg=theme["button_fg"])

# Toggle theme
def toggle_theme():
    global current_theme
    current_theme = "dark" if current_theme == "light" else "light"
    apply_theme()

# Start app
welcome_frame.pack()
apply_theme()
root.mainloop()
