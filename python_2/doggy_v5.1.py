import tkinter as tk
from tkinter import ttk, filedialog, messagebox # Added messagebox
from PIL import Image, ImageTk, ImageDraw

class DogActivityApp:
    def __init__(self, root_window):
        self.root = root_window
        self.root.title("🐶 Dog Activity Recommender")
        self.root.geometry("520x670") # Slightly increased height for messages
        self.root.configure(bg="#f7f7f7")

        # --- Initialize App State ---
        self.dog_photo_path = None
        self.dog_photo_imgtk = None
        self.answers = {}
        self.current_question_index = 0

        # --- Questions ---
        """
Initializes a list of questions to gather information about a dog.

Each item in the list is a tuple where:
- The first element is the question prompt (str).
- The second element is a list of options (list of str) or None if the question expects free text input.

Questions cover various attributes such as the dog’s name, age group, size, energy level, play preferences,
temperament, sociability, health or mobility issues, and preferred activity location.
"""

        self.questions = [
            ("Dog's Name", None),
            ("Age Group", ["Puppy", "Adult", "Senior"]),
            ("Dog Size", ["Small", "Medium", "Large"]),
            ("Energy Level", ["Low", "Medium", "High"]),
            ("Likes Fetch?", ["Yes", "No"]),
            ("Likes Swimming?", ["Yes", "No"]),
            ("Enjoys Mental Challenges?", ["Yes", "No"]),
            ("Temperament", ["Calm", "Excitable", "Nervous", "Aggressive"]),
            ("Sociability", ["Friendly with dogs", "Friendly with people", "Prefers being alone"]),
            ("Health or Mobility Issues", ["None", "Joint Issues", "Blind", "Deaf"]),
            ("Preferred Activity Location", ["Inside", "Outside"]),
        ]
        self.name_entry_widget = None # For focusing on the name entry
        self.name_entry_var = tk.StringVar() # For the dog's name Entry widget
        self.next_button_name = None # To manage the state of the "Next" button for dog's name
        self._name_trace_id = None # To store the trace ID for name_entry_var

        # --- UI Frames ---
        self.welcome_frame = tk.Frame(self.root, bg="#f7f7f7")
        self.message_frame = tk.Frame(self.root, bg="#f7f7f7") # Will be packed/unpacked as needed
        self.question_frame = tk.Frame(self.root, bg="#f7f7f7")
        self.progress_frame = tk.Frame(self.root, bg="#f7f7f7")
        self.result_frame = tk.Frame(self.root, bg="#f7f7f7")

        # Photo preview label (created once, configured and packed as needed)
        self.photo_preview_label = tk.Label(bg="#f7f7f7") # Parent will be set when packed

        # --- UI Elements ---
        self.progress_var = tk.IntVar()
        self.progress_bar = ttk.Progressbar(self.progress_frame, length=450, mode="determinate",
                                            maximum=len(self.questions), variable=self.progress_var)
        self.progress_bar.pack(fill="x", expand=True, padx=10, pady=5)

        # --- Initialize UI ---
        self._setup_welcome_screen()
        self.root.bind("<Configure>", self._adjust_wraplength)

        # ---- ADD THIS LINE TO HANDLE WINDOW CLOSE ----
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)

#  Sets up and displays the welcome screen, hiding all other frames and initializing the welcome message and Start button.
    def _setup_welcome_screen(self):
        self.message_frame.pack_forget()
        self.question_frame.pack_forget()
        self.progress_frame.pack_forget()
        self.result_frame.pack_forget()

        self.welcome_frame.pack(padx=10, pady=30, fill="both", expand=True)
        for widget in self.welcome_frame.winfo_children(): # Clear previous content if any
            widget.destroy()

        self.welcome_msg_label = tk.Label(
            self.welcome_frame,
            text=(
                "🐾 Welcome to your Personal Dog Activity Guide! 🐶\n\n"
                "Let's find the perfect games and exercises "
                "to keep your furry friend happy & healthy! 🎾🦴\n\n"
                "Click Start to begin!"
            ),
            font=("Helvetica", 16, "italic"),
            bg="#f7f7f7",
            justify="center",
            wraplength=460, # Initial wraplength
        )
        self.welcome_msg_label.pack(pady=60)

        start_button = tk.Button(self.welcome_frame, text="Start 🐕",
                                 font=("Helvetica", 15, "bold"), width=15,
                                 bg="#8dd694", command=self.start_quiz) # Default fg (black) should be fine here
        start_button.pack(pady=10)


    def _adjust_wraplength(self, event=None):
        
        if hasattr(self, 'welcome_msg_label') and self.welcome_msg_label.winfo_ismapped():
            new_wraplength = self.welcome_msg_label.master.winfo_width() - 40
            if new_wraplength > 100:
                self.welcome_msg_label.config(wraplength=new_wraplength)

        if hasattr(self, 'rec_display_label') and self.rec_display_label.winfo_ismapped():
            new_wraplength = self.rec_display_label.master.winfo_width() - 60 # Adjusted padding for this label
            if new_wraplength > 100:
                 self.rec_display_label.config(wraplength=new_wraplength)

        if hasattr(self, 'msg_display_label') and self.msg_display_label.winfo_ismapped():
            new_wraplength = self.msg_display_label.master.winfo_width() - 40
            if new_wraplength > 100:
                 self.msg_display_label.config(wraplength=new_wraplength)
    """
    Dynamically adjusts the wraplength of text labels based on the width 
    of their parent container (usually a frame or window). This ensures 
    that text inside the labels wraps properly when the window is resized.

    Parameters:
        event (optional): An event object passed automatically when this 
                          function is bound to a GUI event (like <Configure>). 
                          Defaults to None.

    Behavior:
        - Adjusts the 'wraplength' of 'welcome_msg_label', 'rec_display_label',
          and 'msg_display_label', if they exist and are currently visible.
        - Ensures wraplength is only updated if the new value exceeds 100 pixels.
    """

    def show_message(self, message, error=False):
        if message:
            if not self.message_frame.winfo_ismapped():
                # Determine where to pack message_frame strategically
                if self.question_frame.winfo_ismapped():
                    self.message_frame.pack(fill="x", pady=(5,0), padx=10, before=self.question_frame)
                elif self.progress_frame.winfo_ismapped():
                     self.message_frame.pack(fill="x", pady=(5,0), padx=10, before=self.progress_frame)
                else: # Fallback if neither is visible (e.g. on results page if error occurs)
                     self.message_frame.pack(fill="x", pady=(5,0), padx=10)

        elif self.message_frame.winfo_ismapped():
             self.message_frame.pack_forget()

        for widget in self.message_frame.winfo_children():
            widget.destroy()

        if message:
            fg_color = "red" if error else "black"
            wraplength = self.root.winfo_width() - 40 if self.root.winfo_width() > 50 else 300
            self.msg_display_label = tk.Label(self.message_frame, text=message, font=("Helvetica", 15),
                             bg="#f7f7f7", fg=fg_color, justify="left", wraplength=max(100, wraplength))
            self.msg_display_label.pack(pady=(0,5))
            self._adjust_wraplength() # Adjust immediately


    def select_photo(self):
        path = filedialog.askopenfilename(
            title="Select Dog Photo",
            filetypes=[("Image Files", "*.png *.jpg *.jpeg *.bmp *.gif")]
        )
        if path:
            self.dog_photo_path = path
            try:
                img = Image.open(self.dog_photo_path).convert("RGBA")
                img = img.resize((150, 150), Image.LANCZOS)
                mask = Image.new('L', (150, 150), 0)
                draw = ImageDraw.Draw(mask)
                draw.ellipse((0, 0, 150, 150), fill=255)
                img.putalpha(mask)
                self.dog_photo_imgtk = ImageTk.PhotoImage(img)
            except Exception as e:
                self.show_message(f"Error loading image: {e}", error=True)
                self.dog_photo_imgtk = None
                return

            if self.current_question_index == 0 and self.questions[self.current_question_index][0] == "Dog's Name":
                self.show_question()

                """
Prompts the user to select a dog photo from their file system and processes the image.

- Opens a file dialog for selecting image files (PNG, JPG, JPEG, BMP, GIF).
- If a valid image is selected:
    - Loads and resizes it to 150x150 pixels.
    - Applies a circular mask for rounded appearance.
    - Converts the image to a format compatible with Tkinter (ImageTk.PhotoImage).
- Sets `self.dog_photo_imgtk` to the processed image or None if an error occurs.
- Shows an error message if image loading fails.
"""


    def start_quiz(self):
        self.welcome_frame.pack_forget()
        self.question_frame.pack(pady=10, fill="both", expand=True)
        self.progress_frame.pack(fill="x", pady=5, padx=10, before=self.question_frame)
        self.progress_var.set(0)
        self.current_question_index = 0
        self.answers.clear()
        self.dog_photo_imgtk = None
        self.dog_photo_path = None
        self.show_question()

    def restart(self):
        self.answers.clear()
        self.dog_photo_imgtk = None
        self.dog_photo_path = None
        self.current_question_index = 0
        self.progress_var.set(0)

        self.result_frame.pack_forget()
        self.question_frame.pack_forget()
        self.progress_frame.pack_forget()
        self.message_frame.pack_forget()
        for widget in self.message_frame.winfo_children():
            widget.destroy()

        self._setup_welcome_screen()
        self._adjust_wraplength()

    def show_question(self):
        for widget in self.question_frame.winfo_children():
            widget.destroy()
        self.photo_preview_label.pack_forget()

        question_key, options = self.questions[self.current_question_index]
        tk.Label(self.question_frame, text=question_key, font=("Helvetica", 15, "bold"), bg="#f7f7f7").pack(pady=(15,10))

        content_area = tk.Frame(self.question_frame, bg="#f7f7f7")
        content_area.pack(pady=10, fill="both", expand=True)

        if question_key == "Dog's Name":
            self.name_entry_var.set(self.answers.get(question_key, ""))
            self.name_entry_widget = tk.Entry(content_area, font=("Helvetica", 15), width=30,
                                        textvariable=self.name_entry_var)
            self.name_entry_widget.pack(pady=5)
            self.name_entry_widget.focus()

            if self.dog_photo_imgtk:
                self.photo_preview_label.config(image=self.dog_photo_imgtk)
                self.photo_preview_label.pack(in_=content_area, pady=10)

            tk.Button(content_area, text="Upload Dog Photo (Optional)",
                      command=self.select_photo, width=25, bg="#6fa8dc", fg="black").pack(pady=10)
        else:
            option_buttons_frame = tk.Frame(content_area, bg="#f7f7f7")
            option_buttons_frame.pack()

            for opt in options:
                b = tk.Button(option_buttons_frame, text=opt, width=20,
                              command=lambda o=opt: self.next_question(o), bg="#8dd694",
                              fg="black", relief=tk.FLAT, font=("Helvetica", 14))
                b.pack(pady=4, ipady=2)

        nav_frame = tk.Frame(self.question_frame, bg="#f7f7f7")
        nav_frame.pack(side="bottom", fill="x", pady=(10,15), padx=10)

        prev_button = tk.Button(nav_frame, text="Previous", command=self.previous_question, width=12, bg="#aec6cf",
                                fg="black", relief=tk.FLAT)
        prev_button.pack(side="left", padx=(0, 5))
        prev_button.config(state="disabled" if self.current_question_index == 0 else "normal")

        if question_key == "Dog's Name":
            self.next_button_name = tk.Button(nav_frame, text="Next", width=12, bg="#5cb85c",
                                              fg="black", relief=tk.FLAT,
                                              command=self._submit_dog_name_and_proceed)
            self.next_button_name.pack(side="right", padx=(5, 0))
            if self._name_trace_id: # Remove previous trace if it exists
                self.name_entry_var.trace_remove("write", self._name_trace_id)
            self._name_trace_id = self.name_entry_var.trace_add("write", self._update_next_button_state_for_name)
            self._update_next_button_state_for_name()

        self.show_message("")

    def _update_next_button_state_for_name(self, *args):
        if self.next_button_name and self.next_button_name.winfo_exists():
            name_val = self.name_entry_var.get().strip()
            if name_val:
                self.next_button_name.config(state="normal")
                self.show_message("")
            else:
                self.next_button_name.config(state="disabled")

    def _submit_dog_name_and_proceed(self):
        name_val = self.name_entry_var.get().strip()
        if not name_val:
            self.show_message("Please enter your dog's name.", error=True)
            if self.name_entry_widget and self.name_entry_widget.winfo_exists():
                self.name_entry_widget.focus()
            return
        self.next_question(name_val)

    def next_question(self, selected_option):
        question_key, _ = self.questions[self.current_question_index]
        self.answers[question_key] = selected_option

        self.current_question_index += 1
        self.progress_var.set(self.current_question_index)

        if self.current_question_index < len(self.questions):
            self.show_question()
        else:
            self.question_frame.pack_forget()
            self.show_message("")
            self.show_summary()

    def previous_question(self):
        if self.current_question_index > 0:
            if self.current_question_index >= len(self.questions):
                self.current_question_index = len(self.questions) - 1
            else:
                self.current_question_index -= 1

            self.progress_var.set(self.current_question_index)
            self.result_frame.pack_forget()
            if not self.question_frame.winfo_ismapped():
                self.question_frame.pack(pady=10, fill="both", expand=True)
            if not self.progress_frame.winfo_ismapped():
                 self.progress_frame.pack(fill="x", pady=5, padx=10, before=self.question_frame)
            self.show_question()

    def show_summary(self):
        self.question_frame.pack_forget()
        self.result_frame.pack_forget()

        if not self.progress_frame.winfo_ismapped():
            self.progress_frame.pack(fill="x", pady=5, padx=10)
        self.progress_var.set(len(self.questions))

        self.show_message("")
        self.welcome_frame.pack_forget()

        self.question_frame.pack(pady=20, fill="both", expand=True)
        for widget in self.question_frame.winfo_children():
            widget.destroy()

        tk.Label(self.question_frame, text="Summary of Your Answers:", font=("Helvetica", 16, "bold"), bg="#f7f7f7").pack(pady=10)

        summary_text_frame = tk.Frame(self.question_frame, bg="#f7f7f7")
        summary_text_frame.pack(pady=10, padx=20, fill="x")

        for i, (q_text, _) in enumerate(self.questions):
            val = self.answers.get(q_text, "Not answered")
            tk.Label(summary_text_frame, text=f"{q_text}:", font=("Helvetica", 14, "bold"), bg="#f7f7f7", anchor="w").grid(row=i, column=0, sticky="w", pady=2)
            tk.Label(summary_text_frame, text=f" {val}", font=("Helvetica", 14), bg="#f7f7f7", anchor="w", wraplength=300).grid(row=i, column=1, sticky="w", pady=2)
        summary_text_frame.columnconfigure(1, weight=1)

        btn_frame = tk.Frame(self.question_frame, bg="#f7f7f7")
        btn_frame.pack(pady=20)
        tk.Button(btn_frame, text="Get Recommendations", command=self.get_recommendations, width=20, bg="#5cb85c",
                  fg="black", relief=tk.FLAT).pack(side="left", padx=5)
        tk.Button(btn_frame, text="Back to Questions", command=self.previous_question, width=18, bg="#aec6cf",
                  fg="black", relief=tk.FLAT).pack(side="left", padx=5)
        tk.Button(btn_frame, text="Start Over", command=self.restart, width=15, bg="#f58a8a",
                  fg="black", relief=tk.FLAT).pack(side="left", padx=5)




    def get_recommendations(self): # Generate activity recommendations based on the dog's profile and preferences

        if len(self.answers) < len(self.questions):
            self.show_message("Please answer all questions first.", error=True)
            self.show_summary()
            return

        age = self.answers.get("Age Group")
        energy = self.answers.get("Energy Level")
        size = self.answers.get("Dog Size")
        fetch = self.answers.get("Likes Fetch?")
        water = self.answers.get("Likes Swimming?")
        mental = self.answers.get("Enjoys Mental Challenges?")
        temperament = self.answers.get("Temperament")
        sociability = self.answers.get("Sociability")
        health = self.answers.get("Health or Mobility Issues")
        location = self.answers.get("Preferred Activity Location")

        recommendations_data = [] # Store as dicts with text and tags

        # Health-based suggestions override others if critical
        if health == "Joint Issues":
            recommendations_data.append({"text": "❤️‍🩹 Gentle slow walks and indoor snuffle mats", "tags": ["walk", "indoor", "gentle", "health_specific"]})
        elif health == "Blind":
            recommendations_data.append({"text": "👁️‍🗨️ Scent-based games and sound toys in a safe, familiar area", "tags": ["indoor", "outdoor", "sensory", "health_specific"]})
        elif health == "Deaf":
            recommendations_data.append({"text": "👂 Visual signal training and quiet fetch in securely fenced areas", "tags": ["outdoor", "fetch", "sensory", "training", "health_specific"]})

        if not any("health_specific" in r.get("tags", []) for r in recommendations_data):
            if age == "Senior":
                if energy == "Low":
                    recommendations_data.append({"text": "🚶‍♂️ Slow, short walks and indoor scent games", "tags": ["walk", "indoor", "gentle", "senior", "scent"]})
                else:
                    recommendations_data.append({"text": "🧸 Short, gentle play sessions with soft toys or simple puzzles", "tags": ["indoor", "outdoor", "gentle", "senior", "play", "puzzle"]})
            elif energy == "High":
                if fetch == "Yes" and temperament != "Nervous" and temperament != "Aggressive":
                    recommendations_data.append({"text": "🎾 High-energy fetch (e.g., with a Chuckit!) and consider agility training", "tags": ["outdoor", "fetch", "high-energy", "training", "agility"]})
                if water == "Yes":
                    recommendations_data.append({"text": "🏊 Swimming or dock diving (if appropriate and safe)", "tags": ["outdoor", "water", "high-energy"]})
                if (not (fetch == "Yes" or water == "Yes") or len(recommendations_data) < 1) and temperament != "Aggressive" :
                     recommendations_data.append({"text": "💨 Long hikes, running partner (breed permitting), or vigorous tug-of-war", "tags": ["outdoor", "hike", "tug", "high-energy", "run"]})
            elif energy == "Medium":
                if mental == "Yes":
                    recommendations_data.append({"text": "🧠 Obedience classes, nosework, or learning new tricks", "tags": ["outdoor", "indoor", "mental", "training", "nosework"]})
                else:
                    recommendations_data.append({"text": "🐕 Moderate walks, casual fetch, and puzzle toys", "tags": ["walk", "fetch", "indoor", "outdoor", "puzzle"]})
            elif energy == "Low":
                recommendations_data.append({"text": "🧩 Gentle leashed walks and interactive puzzle toys", "tags": ["walk", "indoor", "gentle", "puzzle"]})

            if temperament == "Nervous":
                recommendations_data.append({"text": "🥰 Focus on calm enrichment toys (e.g., LickiMat, Kong) and quiet, positive reinforcement games in a secure space", "tags": ["indoor", "calm", "nervous", "enrichment", "kong"]})
            elif temperament == "Aggressive":
                 recommendations_data.clear()
                 recommendations_data.append({"text": "⚠️ Work with a professional trainer/behaviorist. Solo enrichment activities are best. Avoid dog parks or uncontrolled social situations.", "tags": ["caution", "professional_help", "indoor", "solo", "aggressive_dog_protocol"]})

            if temperament != "Aggressive":
                if sociability == "Friendly with dogs":
                    recommendations_data.append({"text": "🐶🤝🐶 Supervised playdates with known, friendly dogs or well-managed dog park visits (use caution)", "tags": ["outdoor", "social_dog", "playdate"]})
                elif sociability == "Friendly with people":
                    recommendations_data.append({"text": "👋 Visits to pet-friendly cafes (if calm), social walks in public areas, or therapy dog work (if suitable temperament)", "tags": ["outdoor", "social_people", "walk", "cafe"]})

            if size == "Small" and energy == "High" and temperament != "Aggressive":
                recommendations_data.append({"text": "🤸‍♂️⚠️ For small, high-energy dogs, ensure activities are low-impact on joints (e.g., avoid excessive jumping on hard surfaces). Indoor agility or flirt pole can be great.", "tags": ["caution", "small_dog", "indoor", "outdoor", "low_impact", "agility"]})

        final_recommendations_text = []
        if any("aggressive_dog_protocol" in r.get("tags", []) for r in recommendations_data):
            final_recommendations_text = [r["text"] for r in recommendations_data if "aggressive_dog_protocol" in r.get("tags", [])]
        else:
            if location == "Inside":
                for rec in recommendations_data:
                    if "indoor" in rec["tags"] or "caution" in rec["tags"]:
                        final_recommendations_text.append(rec["text"])
                if not final_recommendations_text or (len(final_recommendations_text) == 1 and "caution" in recommendations_data[0]["tags"] and "indoor" not in recommendations_data[0].get("tags",[])):
                    final_recommendations_text.extend([
                        "🧩 Interactive puzzle toys and food-releasing toys.",
                        "🧸 Indoor fetch with soft toys in a safe space.",
                        "🎓 Short training sessions focusing on tricks or obedience.",
                        "👃 Scent games: hide treats around the house.",
                        "🏠 Build a simple indoor obstacle course with household items."
                    ])
            elif location == "Outside":
                for rec in recommendations_data:
                    if "outdoor" in rec["tags"] or "caution" in rec["tags"]:
                        final_recommendations_text.append(rec["text"])
                if not final_recommendations_text or (len(final_recommendations_text) == 1 and "caution" in recommendations_data[0]["tags"] and "outdoor" not in recommendations_data[0].get("tags",[])):
                    final_recommendations_text.extend([
                        "🌳 Leashed walks in varied environments (parks, trails).",
                        "🎾 Playing fetch in a securely fenced open area.",
                        "🐾 Exploring new sniffing spots on a long lead.",
                        "💧 If safe and appropriate, water play or splashing sessions.",
                        "👍 Outdoor training or practicing commands in a distracting environment."
                    ])
            else:
                final_recommendations_text = [rec["text"] for rec in recommendations_data]

        unique_recs = {}
        for rec_text in final_recommendations_text:
            unique_recs[rec_text] = rec_text

        sorted_recs = sorted(list(unique_recs.values()), key=lambda x: ("⚠️" not in x, "❤️‍🩹" not in x, "👁️‍🗨️" not in x, "👂" not in x)) # Prioritize cautions and health

        dog_name = self.answers.get("Dog's Name", "your dog")
        if sorted_recs:
            result = f"🐾 Recommended activities for {dog_name} ({location.lower()}):\n\n" + "\n".join("• " + act for act in sorted_recs)
        else:
            result = f"😥 No specific {location.lower()} activities found for {dog_name}. Consider general enrichment! 🦴"

        self._show_recommendations_page(result)


    def _show_recommendations_page(self, recommendations_text):
        self.question_frame.pack_forget()
        self.progress_frame.pack_forget()
        self.welcome_frame.pack_forget()
        self.show_message("")

        self.result_frame.pack(pady=10, fill="both", expand=True)
        for widget in self.result_frame.winfo_children():
            widget.destroy()

        if self.dog_photo_imgtk:
            result_photo_label = tk.Label(self.result_frame, image=self.dog_photo_imgtk, bg="#f7f7f7")
            result_photo_label.pack(pady=(10,5))

        rec_label_frame = tk.Frame(self.result_frame, bg="#f7f7f7")
        rec_label_frame.pack(pady=10, padx=20, fill="x")

        self.rec_display_label = tk.Label(rec_label_frame, text=recommendations_text, font=("Helvetica", 14),
                                 bg="#f7f7f7", justify="left",
                                 wraplength=max(100, self.root.winfo_width()-60))
        self.rec_display_label.pack()
        self._adjust_wraplength() # Adjust immediately

        btn_frame = tk.Frame(self.result_frame, bg="#f7f7f7")
        btn_frame.pack(pady=15)
        tk.Button(btn_frame, text="Start Over", command=self.restart, width=15, bg="#f58a8a",
                  fg="black", relief=tk.FLAT).pack(side="left", padx=5)
        tk.Button(btn_frame, text="Back to Summary", command=self.show_summary, width=18, bg="#6fa8dc",
                  fg="black", relief=tk.FLAT).pack(side="left", padx=5)

    # ---- NEW METHOD FOR HANDLING WINDOW CLOSE ----
    def on_closing(self):
        dog_name = self.answers.get("Dog's Name", "your furry friend") # Get dog's name if available
        
        goodbye_title = "Goodbye! 🐾"
        goodbye_message = f"Thanks for using the Dog Activity Recommender!\n\n" \
                          f"Hope you and {dog_name} have a fantastic time with your new activities! 👋"

        # If the app is closed from the welcome screen before any interaction or name entry
        if dog_name == "your furry friend" and self.current_question_index == 0 and not self.answers:
            goodbye_message = "Thanks for checking out the Dog Activity Recommender!\n\nCome back soon to find paw-some activities! 🐶"

        if messagebox.showinfo(goodbye_title, goodbye_message):
            self.root.destroy()
"""
Handles the application closing event by showing a personalized goodbye message.

- Retrieves the dog's name from the user's answers (defaults to "your furry friend").
- Displays a friendly farewell message based on whether the user interacted with the app.
- Closes the main application window after the message is acknowledged.
"""

if __name__ == '__main__':
    root = tk.Tk()
    app = DogActivityApp(root)
    root.mainloop()