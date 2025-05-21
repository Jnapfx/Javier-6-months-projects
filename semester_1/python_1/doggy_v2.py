import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk, ImageDraw

# Globals for photo handling
dog_photo_path = None
dog_photo_imgtk = None

# 🐶 Recommendation logic
def get_recommendations():
    if len(answers) < len(questions):
        show_message("Please answer all questions first.", error=True)
        return

    energy = answers.get("Energy Level")
    size = answers.get("Dog Size")
    fetch = answers.get("Likes Fetch?")
    swimming = answers.get("Likes Swimming?")
    mental = answers.get("Enjoys Mental Challenges?")

    recommendations = []

    if energy == "High" and fetch == "Yes":
        recommendations.append("Fetch")
        recommendations.append("Flyball")

    if energy == "High" and water == "Yes":
        recommendations.append("Swimming")
        recommendations.append("Dock Diving")

    if energy == "Medium" and mental == "Yes":
        recommendations.append("Agility")
        recommendations.append("Obedience")
        recommendations.append("Nosework")

    if energy == "Low":
        recommendations.append("Gentle Walks")
        recommendations.append("Puzzle Toys")

    if size == "Small" and energy == "High":
        recommendations.append("⚠️ Note: Choose low-impact activities for small, high-energy dogs.")

    dog_name = answers.get("Dog's Name", "your dog")
    result = f"Recommended activities for {dog_name}:\n\n" + "\n".join("• " + act for act in recommendations) if recommendations else "No suitable activities found based on the inputs."

    show_recommendations_only(result)

# Show only recommendations and a Start Over button below
def show_recommendations_only(recommendations_text):
    question_frame.pack_forget()
    progress_label.config(text="")
    welcome_frame.pack_forget()

    result_frame.pack(pady=10)
    for widget in result_frame.winfo_children():
        widget.destroy()

    # Show dog photo if uploaded
    global dog_photo_imgtk
    if dog_photo_imgtk:
        photo_label = tk.Label(result_frame, image=dog_photo_imgtk, bg="#f7f7f7")
        photo_label.pack(pady=5)

    rec_label = tk.Label(result_frame, text=recommendations_text, font=("Helvetica", 12), bg="#f7f7f7", justify="left")
    rec_label.pack(pady=10)

    btn_frame = tk.Frame(result_frame, bg="#f7f7f7")
    btn_frame.pack(pady=5)
    tk.Button(btn_frame, text="Start Over", command=restart, width=15, bg="#f58a8a").pack(side="left", padx=5)
    tk.Button(btn_frame, text="Back to Summary", command=show_summary, width=15, bg="#6fa8dc").pack(side="left", padx=5)

# Function to show error messages inside result_frame (used if user tries to get recommendations before answering all questions)
def show_message(message, error=False):
    # Clear any previous message
    for widget in message_frame.winfo_children():
        widget.destroy()
    if message:
        fg_color = "red" if error else "black"
        label = tk.Label(message_frame, text=message, font=("Helvetica", 12), bg="#f7f7f7", fg=fg_color, justify="left")
        label.pack()

# Select photo dialog and crop to circle
def select_photo():
    global dog_photo_path, dog_photo_imgtk
    path = filedialog.askopenfilename(
        title="Select Dog Photo",
        filetypes=[("Image Files", "*.png *.jpg *.jpeg *.bmp *.gif")]
    )
    if path:
        dog_photo_path = path
        img = Image.open(dog_photo_path).convert("RGBA")
        img = img.resize((150, 150), Image.LANCZOS)
        # Create circular mask
        mask = Image.new('L', (150, 150), 0)
        draw = ImageDraw.Draw(mask)
        draw.ellipse((0, 0, 150, 150), fill=255)
        img.putalpha(mask)

        dog_photo_imgtk = ImageTk.PhotoImage(img)
        photo_preview_label.config(image=dog_photo_imgtk)
        photo_preview_label.image = dog_photo_imgtk

# 🛠 GUI Setup
root = tk.Tk()
root.title("Dog Activity Recommender")
root.geometry("480x400")
root.configure(bg="#f7f7f7")

# 🐾 Title
tk.Label(root, text="🐶 Dog Activity Recommender", font=("Helvetica", 16, "bold"), bg="#f7f7f7").pack(pady=10)

# 🧭 Progress Label
progress_label = tk.Label(root, text="", font=("Helvetica", 11), bg="#f7f7f7")
progress_label.pack()

# Message Frame (for error/info messages)
message_frame = tk.Frame(root, bg="#f7f7f7")
message_frame.pack()

# 🌟 Welcome Screen
welcome_frame = tk.Frame(root, bg="#f7f7f7")
welcome_frame.pack(pady=30)

tk.Label(
    welcome_frame,
    text="Welcome to the Dog Activity Recommender!",
    font=("Helvetica", 14),
    bg="#f7f7f7"
).pack(pady=10)

tk.Label(
    welcome_frame,
    text="Answer a few quick questions about your dog, and we'll suggest\nfun and suitable activities for them to enjoy!",
    font=("Helvetica", 11),
    bg="#f7f7f7",
    justify="center"
).pack(pady=10)

tk.Button(
    welcome_frame,
    text="Start",
    width=20,
    bg="#8dd694",
    font=("Helvetica", 11, "bold"),
    command=lambda: start_questions()
).pack(pady=10)

# 🧠 Question logic
questions = [
    ("Dog's Name", None),  # special handling
    ("Energy Level", ["Low", "Medium", "High"]),
    ("Dog Size", ["Small", "Medium", "Large"]),
    ("Likes Fetch?", ["Yes", "No"]),
    ("Likes Water?", ["Yes", "No"]),
    ("Enjoys Mental Challenges?", ["Yes", "No"])
]

answers = {}
current_question_index = 0

# 🧩 Question container frame
question_frame = tk.Frame(root, bg="#f7f7f7")

# Photo preview label for name question
photo_preview_label = tk.Label(question_frame, bg="#f7f7f7")
photo_preview_label.pack_forget()

# 🟢 Result frame for summary or recommendations
result_frame = tk.Frame(root, bg="#f7f7f7")
result_frame.pack_forget()

# ▶️ Start questions
def start_questions():
    global current_question_index, dog_photo_imgtk, dog_photo_path
    current_question_index = 0
    answers.clear()
    dog_photo_imgtk = None
    dog_photo_path = None
    welcome_frame.pack_forget()
    result_frame.pack_forget()
    question_frame.pack(pady=20)
    show_question()
    show_message("")

# 🔘 Next Question
def next_question(selected_option):
    global current_question_index

    question_key, _ = questions[current_question_index]
    answers[question_key] = selected_option

    current_question_index += 1
    if current_question_index < len(questions):
        show_question()
    else:
        question_frame.pack_forget()
        progress_label.config(text="✅ All questions answered!")
        show_summary()

# 📋 Show a question
def show_question():
    for widget in question_frame.winfo_children():
        widget.destroy()
    photo_preview_label.pack_forget()

    progress_label.config(text=f"Question {current_question_index + 1} of {len(questions)}")

    question_text, options = questions[current_question_index]

    tk.Label(question_frame, text=question_text, font=("Helvetica", 13), bg="#f7f7f7").pack(pady=10)

    # Special handling for Dog's Name question
    if question_text == "Dog's Name":
        name_var = tk.StringVar()
        name_entry = tk.Entry(question_frame, font=("Helvetica", 12), width=30, textvariable=name_var)
        name_entry.pack(pady=5)

        # Show photo preview if photo selected
        if dog_photo_imgtk:
            photo_preview_label.pack(pady=5)

        # Upload photo button (optional)
        tk.Button(question_frame, text="Upload Dog Photo (Optional)", command=select_photo, width=25, bg="#6fa8dc").pack(pady=5)

        next_btn = tk.Button(question_frame, text="Next", state="disabled", width=20, bg="#8dd694")

        def on_name_change(*args):
            name = name_var.get().strip()
            if name:
                next_btn.config(state="normal")
                show_message("")
            else:
                next_btn.config(state="disabled")

        def submit_name():
            name = name_var.get().strip()
            if not name:
                show_message("Please enter your dog's name.", error=True)
                return
            answers[question_text] = name
            show_message("")
            next_question(name)

        name_var.trace_add("write", on_name_change)
        next_btn.config(command=submit_name)
        next_btn.pack(pady=10)

    else:
        for opt in options:
            tk.Button(question_frame, text=opt, width=20, bg="#d3eaf2",
                      command=lambda opt=opt: next_question(opt)).pack(pady=5)

# 📋 Show answers summary before recommendations
def show_summary():
    result_frame.pack(pady=10)
    for widget in result_frame.winfo_children():
        widget.destroy()

    summary_text = "You've answered:\n\n"
    for key, val in answers.items():
        summary_text += f"{key}: {val}\n"

    summary_label = tk.Label(result_frame, text=summary_text, font=("Helvetica", 12), bg="#f7f7f7", justify="left")
    summary_label.pack(pady=10)

    btn_frame = tk.Frame(result_frame, bg="#f7f7f7")
    btn_frame.pack(pady=5)

    tk.Button(btn_frame, text="Get Recommendations", command=get_recommendations, width=15, bg="#8dd694").pack(side="left", padx=5)
    tk.Button(btn_frame, text="Back to Questions", command=back_to_questions, width=15, bg="#6fa8dc").pack(side="left", padx=5)
    tk.Button(btn_frame, text="Start Over", command=restart, width=15, bg="#f58a8a").pack(side="left", padx=5)

# Go back from summary to last question
def back_to_questions():
    result_frame.pack_forget()
    global current_question_index
    current_question_index = len(answers) - 1
    question_frame.pack(pady=20)
    show_question()
    progress_label.config(text=f"Question {current_question_index + 1} of {len(questions)}")
    show_message("")

# 🔄 Restart app
def restart():
    global current_question_index, answers, dog_photo_imgtk, dog_photo_path
    current_question_index = 0
    answers = {}
    dog_photo_imgtk = None
    dog_photo_path = None
    result_frame.pack_forget()
    question_frame.pack_forget()
    progress_label.config(text="")
    welcome_frame.pack(pady=30)
    show_message("")

# 🚀 Run the app
root.mainloop()
