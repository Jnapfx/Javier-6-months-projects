import tkinter as tk
from tkinter import ttk, filedialog
from PIL import Image, ImageTk, ImageDraw

# Globals for photo handling
dog_photo_path = None
dog_photo_imgtk = None

# Questions with options (including new question for preferred activity location)
questions = [
    ("Dog's Name", None),  # special handling
    ("Dog Size", ["Small", "Medium", "Large"]),
    ("Energy Level", ["Low", "Medium", "High"]),
    ("Likes Fetch?", ["Yes", "No"]),
    ("Likes Water?", ["Yes", "No"]),
    ("Enjoys Mental Challenges?", ["Yes", "No"]),
    ("Age Group", ["Puppy", "Adult", "Senior"]),
    ("Temperament", ["Calm", "Excitable", "Nervous", "Aggressive"]),
    ("Sociability", ["Friendly with dogs", "Friendly with people", "Prefers being alone"]),
    ("Health or Mobility Issues", ["None", "Joint Issues", "Blind", "Deaf"]),
    ("Preferred Activity Location", ["Inside", "Outside"]),  # New question
]

answers = {}
current_question_index = 0

def show_message(message, error=False):
    for widget in message_frame.winfo_children():
        widget.destroy()
    if message:
        fg_color = "red" if error else "black"
        label = tk.Label(message_frame, text=message, font=("Helvetica", 12), bg="#f7f7f7", fg=fg_color, justify="left")
        label.pack()

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

def get_recommendations():
    if len(answers) < len(questions):
        show_message("Please answer all questions first.", error=True)
        return

    energy = answers.get("Energy Level")
    size = answers.get("Dog Size")
    fetch = answers.get("Likes Fetch?")
    water = answers.get("Likes Water?")
    mental = answers.get("Enjoys Mental Challenges?")
    age = answers.get("Age Group")
    temperament = answers.get("Temperament")
    sociability = answers.get("Sociability")
    health = answers.get("Health or Mobility Issues")
    location = answers.get("Preferred Activity Location")

    recommendations = []

    # Health-based suggestions override others if critical
    if health == "Joint Issues":
        recommendations.append("Gentle slow walks and indoor snuffle mats")
    elif health == "Blind":
        recommendations.append("Scent-based games and sound toys")
    elif health == "Deaf":
        recommendations.append("Visual signals and quiet fetch in fenced areas")
    else:
        # Age-based suggestions
        if age == "Senior":
            if energy == "Low":
                recommendations.append("Slow walks and indoor scent games")
            else:
                recommendations.append("Short play sessions with soft toys or puzzles")
        elif energy == "High":
            if fetch == "Yes" and temperament != "Nervous":
                recommendations.append("High-energy fetch and agility training")
            if water == "Yes":
                recommendations.append("Swimming and dock diving")
            if not (fetch == "Yes" or water == "Yes"):
                recommendations.append("Long hikes and tug-of-war")
        elif energy == "Medium" and mental == "Yes":
            recommendations.append("Agility, obedience, and nosework")
        elif energy == "Low":
            recommendations.append("Gentle walks and puzzle toys")

        # Temperament-based
        if temperament == "Nervous":
            recommendations.append("Calm enrichment toys and quiet indoor games")

        # Sociability-based
        if sociability == "Friendly with dogs":
            recommendations.append("Playdates or dog park visits")
        elif sociability == "Friendly with people":
            recommendations.append("Visits to pet-friendly cafes and social walks")

        # Size & energy caution
        if size == "Small" and energy == "High":
            recommendations.append("⚠️ Note: Choose low-impact activities for small, high-energy dogs.")

    # Filter recommendations based on preferred location
    if location == "Inside":
        recommendations = [rec for rec in recommendations if not any(x in rec.lower() for x in ["walk", "hike", "swimming", "dock", "fetch", "tug-of-war", "playdates", "dog park"])]
        # Add some indoor-specific recommendations if none left
        if not recommendations:
            recommendations.extend([
                "Puzzle toys and scent games",
                "Indoor fetch with soft toys",
                "Training sessions and obedience practice",
                "Interactive treat dispensers"
            ])
    elif location == "Outside":
        recommendations = [rec for rec in recommendations if any(x in rec.lower() for x in ["walk", "hike", "swimming", "dock", "fetch", "tug-of-war", "playdates", "dog park"])]
        # Add outdoor-specific if none left
        if not recommendations:
            recommendations.extend([
                "Leashed walks and exploring new parks",
                "Playing fetch in open areas",
                "Socializing with other dogs outdoors",
                "Water play and splash sessions"
            ])

    dog_name = answers.get("Dog's Name", "your dog")
    if recommendations:
        result = f"Recommended activities for {dog_name} ({location.lower()}):\n\n" + "\n".join("• " + act for act in recommendations)
    else:
        result = "No suitable activities found based on the inputs."

    show_recommendations_only(result)

def show_recommendations_only(recommendations_text):
    question_frame.pack_forget()
    progress_frame.pack_forget()
    welcome_frame.pack_forget()
    message_frame.pack_forget()

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

def show_summary():
    question_frame.pack_forget()
    result_frame.pack_forget()
    progress_frame.pack(pady=5)
    progress_var.set(current_question_index)
    message_frame.pack_forget()
    welcome_frame.pack_forget()

    summary_text = ""
    for q, _ in questions:
        val = answers.get(q, "Not answered")
        summary_text += f"{q}: {val}\n"

    question_frame.pack(pady=20)
    for widget in question_frame.winfo_children():
        widget.destroy()

    tk.Label(question_frame, text="Summary:", font=("Helvetica", 14, "bold"), bg="#f7f7f7").pack(pady=10)
    tk.Label(question_frame, text=summary_text, font=("Helvetica", 12), bg="#f7f7f7", justify="left").pack(pady=10)

    btn_frame = tk.Frame(question_frame, bg="#f7f7f7")
    btn_frame.pack(pady=5)
    tk.Button(btn_frame, text="Get Recommendations", command=get_recommendations, width=20, bg="#8dd694").pack(side="left", padx=5)
    tk.Button(btn_frame, text="Start Over", command=restart, width=20, bg="#f58a8a").pack(side="left", padx=5)

def restart():
    global dog_photo_imgtk, dog_photo_path, current_question_index
    answers.clear()
    dog_photo_imgtk = None
    dog_photo_path = None
    current_question_index = 0
    result_frame.pack_forget()
    question_frame.pack_forget()
    progress_frame.pack_forget()
    progress_var.set(0)
    message_frame.pack()
    welcome_frame.pack(pady=30)

def next_question(selected_option):
    global current_question_index

    question_key, _ = questions[current_question_index]
    answers[question_key] = selected_option

    current_question_index += 1
    progress_var.set(current_question_index)

    if current_question_index < len(questions):
        show_question()
    else:
        question_frame.pack_forget()
        progress_frame.pack_forget()
        message_frame.pack_forget()
        show_summary()

def show_question():
    for widget in question_frame.winfo_children():
        widget.destroy()
    photo_preview_label.pack_forget()

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
            next_question(name)

        name_var.trace_add("write", on_name_change)
        next_btn.config(command=submit_name)
        next_btn.pack(pady=10)
    else:
        # Show options as buttons
        btn_frame = tk.Frame(question_frame, bg="#f7f7f7")
        btn_frame.pack()

        def on_option_click(opt):
            next_question(opt)

        for opt in options:
            b = tk.Button(btn_frame, text=opt, width=20, command=lambda o=opt: on_option_click(o), bg="#8dd694")
            b.pack(pady=3)

# GUI Setup
root = tk.Tk()
root.title("Dog Activity Recommender")
root.geometry("520x650")
root.configure(bg="#f7f7f7")

# Welcome Frame with improved message and start button
welcome_frame = tk.Frame(root, bg="#f7f7f7")
welcome_frame.pack(padx=10, pady)

welcome_msg = tk.Label(
    welcome_frame,
    text=(
        "🐾 Welcome to your Personal Dog Activity Guide! 🐶\n"
        "Let's find the perfect games and exercises\n"
        "to keep your furry friend happy & healthy! 🎾🦴\n"
        "Click Start to begin!"
    ),
    font=("Helvetica", 15, "italic"),
    bg="#f7f7f7",
    justify="center",
    wraplength=720,
)
welcome_msg.pack(pady=60)

start_button = tk.Button(welcome_frame, text="Start 🐕", font=("Helvetica", 14, "bold"), width=15, bg="#8dd694")
start_button.pack(pady=10)

def start_quiz():
    welcome_frame.pack_forget()
    message_frame.pack()
    question_frame.pack(pady=20)
    progress_frame.pack(pady=5)
    progress_var.set(0)
    show_question()

start_button.config(command=start_quiz)

# Message frame for errors or info
message_frame = tk.Frame(root, bg="#f7f7f7")

# Question frame
question_frame = tk.Frame(root, bg="#f7f7f7")

# Progress bar frame and bar (using ttk.Progressbar)
progress_frame = tk.Frame(root, bg="#f7f7f7")
progress_var = tk.IntVar()
progress_bar = ttk.Progressbar(progress_frame, length=450, mode="determinate", maximum=len(questions), variable=progress_var)
progress_bar.pack()

# Result frame
result_frame = tk.Frame(root, bg="#f7f7f7")

# Photo preview label (hidden initially)
photo_preview_label = tk.Label(root, bg="#f7f7f7")

# Dynamic wraplength adjustment for welcome message on resize
def adjust_wraplength(event):
    new_wraplength = event.width - 60
    if new_wraplength > 100:
        welcome_msg.config(wraplength=new_wraplength)

root.bind("<Configure>", adjust_wraplength)

root.mainloop()
