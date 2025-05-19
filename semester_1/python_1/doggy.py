import tkinter as tk

# 🐶 Recommendation logic
def get_recommendations():
    if len(answers) < len(questions):
        show_message("Please answer all questions first.", error=True)
        return

    energy = answers["Energy Level"]
    size = answers["Dog Size"]
    fetch = answers["Likes Fetch?"]
    water = answers["Likes Water?"]
    mental = answers["Enjoys Mental Challenges?"]

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

    if recommendations:
        result = "Recommended activities for your dog:\n\n" + "\n".join("• " + act for act in recommendations)
    else:
        result = "No suitable activities found based on the inputs."

    show_recommendations_only(result)

# Show only recommendations and a Start Over button below
def show_recommendations_only(recommendations_text):
    question_frame.pack_forget()
    progress_label.config(text="")
    welcome_frame.pack_forget()

    result_frame.pack(pady=10)
    for widget in result_frame.winfo_children():
        widget.destroy()

    rec_label = tk.Label(result_frame, text=recommendations_text, font=("Helvetica", 12), bg="#f7f7f7", justify="left")
    rec_label.pack(pady=10)

    tk.Button(result_frame, text="Start Over", command=restart, width=20, bg="#f58a8a").pack(pady=5)

# Function to show error messages inside result_frame (used if user tries to get recommendations before answering all questions)
def show_message(message, error=False):
    if hasattr(show_message, "message_label") and show_message.message_label.winfo_exists():
        show_message.message_label.destroy()

    fg_color = "red" if error else "black"
    show_message.message_label = tk.Label(result_frame, text=message, font=("Helvetica", 12), bg="#f7f7f7", fg=fg_color, justify="left")
    show_message.message_label.pack(pady=10)

# 🛠 GUI Setup
root = tk.Tk()
root.title("Dog Activity Recommender")
root.geometry("480x320")
root.configure(bg="#f7f7f7")

# 🐾 Title
tk.Label(root, text="🐶 Dog Activity Recommender", font=("Helvetica", 16, "bold"), bg="#f7f7f7").pack(pady=15)

# 🧭 Progress Label
progress_label = tk.Label(root, text="", font=("Helvetica", 11), bg="#f7f7f7")
progress_label.pack()

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

# 🟢 Result frame for summary or recommendations
result_frame = tk.Frame(root, bg="#f7f7f7")
result_frame.pack_forget()

# ▶️ Start questions
def start_questions():
    global current_question_index
    current_question_index = 0
    answers.clear()
    welcome_frame.pack_forget()
    result_frame.pack_forget()
    question_frame.pack(pady=20)
    show_question()

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

    progress_label.config(text=f"Question {current_question_index + 1} of {len(questions)}")

    question_text, options = questions[current_question_index]
    tk.Label(question_frame, text=question_text, font=("Helvetica", 13), bg="#f7f7f7").pack(pady=10)

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

    tk.Button(result_frame, text="Get Recommendations", command=get_recommendations, width=20, bg="#8dd694").pack(pady=5)
    tk.Button(result_frame, text="Start Over", command=restart, width=20, bg="#f58a8a").pack(pady=5)

# 🔄 Restart app
def restart():
    global current_question_index, answers
    current_question_index = 0
    answers = {}

    result_frame.pack_forget()
    question_frame.pack_forget()
    progress_label.config(text="")
    welcome_frame.pack(pady=30)

# 🚀 Run the app
root.mainloop()