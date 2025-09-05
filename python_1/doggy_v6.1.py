# Dog Activity Recommender (Navigation Buttons Visible - with Scrollable Recommendations)
import tkinter as tk
from tkinter import ttk, filedialog, messagebox
from PIL import Image, ImageTk, ImageDraw
import darkdetect  # For detecting OS theme

class DogActivityApp:
    # --- Color Palettes ---
    LIGHT_THEME = {
        "app_bg": "#f7f7f7",
        "text_fg": "black",
        "entry_bg": "white",
        "entry_fg": "black",
        "entry_cursor": "black",
        "button_fg": "black",
        "button_relief": tk.FLAT,
        "button_start_bg": "#8dd694",
        "button_upload_bg": "#6fa8dc",
        "button_option_bg": "#8dd694",
        "button_nav_prev_bg": "#aec6cf",
        "button_nav_next_bg": "#5cb85c",
        "button_get_recs_bg": "#5cb85c",
        "button_back_to_q_bg": "#aec6cf",
        "button_start_over_bg": "#f58a8a",
        "button_copy_bg": "#AED6F1",
        "button_export_bg": "#FFD966",
        "button_summary_nav_bg": "#6fa8dc",
        "message_success_fg": "green",
        "message_error_fg": "red",
        "message_info_fg": "black",
        "progressbar_bg": "#8dd694",
        "progressbar_troughcolor": "#e0e0e0"
    }

    DARK_THEME = {
        "app_bg": "#2e2e2e",
        "text_fg": "#e0e0e0",
        "entry_bg": "#3c3c3c",
        "entry_fg": "#e0e0e0",
        "entry_cursor": "white",
        "button_fg": "#e0e0e0",
        "button_relief": tk.FLAT,
        "button_start_bg": "#38761d",
        "button_upload_bg": "#366092",
        "button_option_bg": "#38761d",
        "button_nav_prev_bg": "#4f636b",
        "button_nav_next_bg": "#2a5c2a",
        "button_get_recs_bg": "#2a5c2a",
        "button_back_to_q_bg": "#4f636b",
        "button_start_over_bg": "#a94442",
        "button_copy_bg": "#3670A3",
        "button_export_bg": "#B8860B",
        "button_summary_nav_bg": "#366092",
        "message_success_fg": "#77dd77",
        "message_error_fg": "#ff6961",
        "message_info_fg": "#e0e0e0",
        "progressbar_bg": "#38761d",
        "progressbar_troughcolor": "#3c3c3c"
    }

    # --- Constants ---
    INITIAL_WINDOW_GEOMETRY = "520x670"
    PROGRESS_BAR_LENGTH = 450
    FONT_HELVETICA = "Helvetica"
    FONT_SIZE_WELCOME = 16
    FONT_SIZE_HEADINGS_BOLD = 15
    FONT_SIZE_BUTTON_MAIN_BOLD = 15
    FONT_SIZE_OPTIONS_SUMMARY_RECOMMENDATIONS = 14
    PHOTO_PREVIEW_DIMENSIONS = (150, 150)

    # --- Questions (without Breed) ---
    QUESTIONS_CONFIG = [
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
        ("Current Weather", ["Hot", "Cold", "Rainy", "Mild"]),
    ]
    QUESTION_COUNT = len(QUESTIONS_CONFIG)
    DOG_NAME_QUESTION_KEY = "Dog's Name"

    def __init__(self, root_window):
        self.root = root_window

        try:
            current_os_theme = darkdetect.theme() or "Light"
        except Exception:
            current_os_theme = "Light"
        self.theme = DogActivityApp.DARK_THEME if current_os_theme == "Dark" else DogActivityApp.LIGHT_THEME

        self.root.title("🐶 Dog Activity Recommender")
        self.root.geometry(DogActivityApp.INITIAL_WINDOW_GEOMETRY)
        self.root.configure(bg=self.theme["app_bg"])
        self.root.grid_rowconfigure(0, weight=1) # Allow result_frame area to expand
        self.root.grid_columnconfigure(0, weight=1)


        self.dog_photo_path = None
        self.dog_photo_imgtk = None
        self.answers = {}
        self.current_question_index = 0

        self.name_entry_widget = None
        self.name_entry_var = tk.StringVar()
        self.next_button_name = None
        self._name_trace_id = None

        self.welcome_frame = tk.Frame(self.root, bg=self.theme["app_bg"])
        self.message_frame = tk.Frame(self.root, bg=self.theme["app_bg"])
        self.question_frame = tk.Frame(self.root, bg=self.theme["app_bg"])
        self.progress_frame = tk.Frame(self.root, bg=self.theme["app_bg"])
        self.result_frame = tk.Frame(self.root, bg=self.theme["app_bg"])
        # self.result_frame will be packed later. Configure its grid if using grid inside it.

        self.photo_preview_label = tk.Label(bg=self.theme["app_bg"])

        self.progress_var = tk.IntVar()
        style = ttk.Style()
        style.theme_use('default')
        style.configure(
            "themed.Horizontal.TProgressbar",
            background=self.theme["progressbar_bg"],
            troughcolor=self.theme["progressbar_troughcolor"],
            bordercolor=self.theme["app_bg"],
            lightcolor=self.theme["progressbar_bg"],
            darkcolor=self.theme["progressbar_bg"]
        )
        self.progress_bar = ttk.Progressbar(
            self.progress_frame,
            style="themed.Horizontal.TProgressbar",
            length=DogActivityApp.PROGRESS_BAR_LENGTH,
            mode="determinate",
            maximum=DogActivityApp.QUESTION_COUNT,
            variable=self.progress_var
        )
        self.progress_bar.pack(fill="x", expand=True, padx=10, pady=5)

        self._setup_welcome_screen()

        self.root.bind("<Configure>", self._adjust_wraplength)
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)

    def _setup_welcome_screen(self):
        self.message_frame.pack_forget()
        self.question_frame.pack_forget()
        self.progress_frame.pack_forget()
        self.result_frame.pack_forget()

        self.welcome_frame.pack(padx=10, pady=30, fill="both", expand=True)
        for widget in self.welcome_frame.winfo_children():
            widget.destroy()

        self.welcome_msg_label = tk.Label(
            self.welcome_frame,
            text=(
                "🐾 Welcome to your Personal Dog Activity Guide! 🐶\n\n"
                "Let's find the perfect games and exercises "
                "to keep your furry friend happy & healthy! 🎾🦴\n\n"
                "Click Start to begin!"
            ),
            font=(DogActivityApp.FONT_HELVETICA, DogActivityApp.FONT_SIZE_WELCOME, "italic"),
            bg=self.theme["app_bg"], fg=self.theme["text_fg"],
            justify="center", wraplength=460
        )
        self.welcome_msg_label.pack(pady=60, expand=True)

        start_button = tk.Button(
            self.welcome_frame,
            text="Start 🐕",
            font=(DogActivityApp.FONT_HELVETICA, DogActivityApp.FONT_SIZE_BUTTON_MAIN_BOLD, "bold"),
            width=15,
            relief=self.theme["button_relief"],
            bg=self.theme["button_start_bg"],
            fg=self.theme["button_fg"],
            command=self.start_quiz
        )
        start_button.pack(pady=10)

    def _adjust_wraplength(self, event=None):
        if hasattr(self, 'welcome_msg_label') and self.welcome_msg_label.winfo_ismapped():
            new_wrap = self.welcome_msg_label.master.winfo_width() - 40
            if new_wrap > 100: self.welcome_msg_label.config(wraplength=new_wrap)

        # For rec_display_label, wraplength will be based on its immediate master (inner_scrollable_frame)
        # which is controlled by the canvas width.
        if hasattr(self, 'rec_display_label') and self.rec_display_label.winfo_ismapped():
            # The canvas width is a better reference for wraplength here
            if hasattr(self, 'scrollable_canvas') and self.scrollable_canvas.winfo_ismapped():
                canvas_width = self.scrollable_canvas.winfo_width()
                # Subtract a bit for padding within the label or scrollbar width if it's overlaying
                new_wrap = canvas_width - 30 # Adjust this value as needed
                if new_wrap > 100:
                    self.rec_display_label.config(wraplength=new_wrap)
            else: # Fallback if canvas not ready
                 master_width = self.rec_display_label.master.winfo_width()
                 if master_width > 0 : # Ensure master width is available
                    new_wrap = master_width - 20 # Small padding
                    if new_wrap > 100: self.rec_display_label.config(wraplength=new_wrap)


        if hasattr(self, 'msg_display_label') and self.msg_display_label.winfo_ismapped():
            new_wrap = self.msg_display_label.master.winfo_width() - 40
            if new_wrap > 100: self.msg_display_label.config(wraplength=new_wrap)

    def show_message(self, message, error=False):
        for widget in self.message_frame.winfo_children():
            widget.destroy()

        if message:
            active_main_frame = None
            if self.result_frame.winfo_ismapped(): active_main_frame = self.result_frame
            elif self.question_frame.winfo_ismapped(): active_main_frame = self.question_frame
            elif self.welcome_frame.winfo_ismapped(): active_main_frame = self.welcome_frame # Message on welcome too
            # Progress frame usually sits above question frame, so message goes before question/result/welcome

            if not self.message_frame.winfo_ismapped():
                if active_main_frame:
                    self.message_frame.pack(fill="x", pady=(5,0), padx=10, before=active_main_frame)
                else: # Fallback if no main content frame is active yet (e.g. very early error)
                    self.message_frame.pack(fill="x", pady=(5,0), padx=10, side="top")


            fg_color = self.theme["message_error_fg"] if error else \
                       (self.theme["message_success_fg"] if "copied" in message.lower() or "saved" in message.lower() else
                        self.theme["message_info_fg"])
            
            wrap_len = self.root.winfo_width() - 40 if self.root.winfo_width() > 50 else 300
            self.msg_display_label = tk.Label(
                self.message_frame, text=message,
                font=(DogActivityApp.FONT_HELVETICA, DogActivityApp.FONT_SIZE_HEADINGS_BOLD -2), # Slightly smaller for messages
                bg=self.theme["app_bg"], fg=fg_color,
                justify="left", wraplength=max(100, wrap_len)
            )
            self.msg_display_label.pack(pady=(0,5), fill="x", expand=True)
            self._adjust_wraplength()
        elif self.message_frame.winfo_ismapped():
            self.message_frame.pack_forget()

    def select_photo(self):
        temp_name = ""
        if (self.current_question_index == 0 and
            DogActivityApp.QUESTIONS_CONFIG[self.current_question_index][0] == DogActivityApp.DOG_NAME_QUESTION_KEY):
            temp_name = self.name_entry_var.get()
        try:
            path = filedialog.askopenfilename(
                title="Select Dog Photo",
                filetypes=[("Image Files", "*.png *.jpg *.jpeg *.bmp *.gif")]
            )
        except Exception as e:
            self.show_message(f"Error opening file dialog: {e}", error=True); return
        if not path: self.show_message("No file selected.", error=True); return

        self.dog_photo_path = path
        try:
            img = Image.open(self.dog_photo_path).convert("RGBA")
            img = img.resize(DogActivityApp.PHOTO_PREVIEW_DIMENSIONS, Image.LANCZOS)
            mask = Image.new('L', DogActivityApp.PHOTO_PREVIEW_DIMENSIONS, 0)
            draw = ImageDraw.Draw(mask)
            draw.ellipse((0, 0) + DogActivityApp.PHOTO_PREVIEW_DIMENSIONS, fill=255)
            img.putalpha(mask)
            self.dog_photo_imgtk = ImageTk.PhotoImage(img)
            self.show_message("Image loaded successfully!")
        except FileNotFoundError:
            self.show_message("Error: Image file not found.", error=True); self.dog_photo_imgtk = None
        except Image.UnidentifiedImageError:
            self.show_message("Error: Cannot identify image. Use PNG/JPG.", error=True); self.dog_photo_imgtk = None
        except Exception as e:
            self.show_message(f"Error loading image: {e}", error=True); self.dog_photo_imgtk = None
        
        if self.dog_photo_imgtk is None and self.current_question_index == 0 : # Restore name if image load failed
            self.name_entry_var.set(temp_name)

        if (self.current_question_index == 0 and
            DogActivityApp.QUESTIONS_CONFIG[self.current_question_index][0] == DogActivityApp.DOG_NAME_QUESTION_KEY):
            self.show_question() # Refresh to show preview or lack thereof
            if temp_name and self.name_entry_var.get() == "": self.name_entry_var.set(temp_name)


    def start_quiz(self):
        self.welcome_frame.pack_forget()
        self.result_frame.pack_forget()
        self.message_frame.pack_forget()

        self.progress_frame.pack(fill="x", pady=5, padx=10, side="top") # Ensure progress is at top
        self.question_frame.pack(pady=10, fill="both", expand=True)
        
        self.progress_var.set(0)
        self.current_question_index = 0
        self.answers.clear()
        self.dog_photo_imgtk = None # Clear previous photo
        self.dog_photo_path = None
        self.show_question()

    def restart(self):
        self.answers.clear()
        self.dog_photo_imgtk = None
        self.dog_photo_path = None
        self.current_question_index = 0
        self.progress_var.set(0)
        self.name_entry_var.set("") # Clear name entry var

        self.result_frame.pack_forget()
        self.question_frame.pack_forget()
        self.progress_frame.pack_forget()
        self.message_frame.pack_forget()
        
        self._setup_welcome_screen()
        self._adjust_wraplength()

    def show_question(self):
        self.show_message("") 

        for widget in self.question_frame.winfo_children(): widget.destroy()
        self.photo_preview_label.pack_forget()

        question_key, options = DogActivityApp.QUESTIONS_CONFIG[self.current_question_index]
        tk.Label(
            self.question_frame, text=question_key,
            font=(DogActivityApp.FONT_HELVETICA, DogActivityApp.FONT_SIZE_HEADINGS_BOLD, "bold"),
            bg=self.theme["app_bg"], fg=self.theme["text_fg"]
        ).pack(pady=(15, 10))

        content_area = tk.Frame(self.question_frame, bg=self.theme["app_bg"])
        content_area.pack(pady=10, fill="both", expand=True)

        if question_key == DogActivityApp.DOG_NAME_QUESTION_KEY:
            current_name = self.answers.get(DogActivityApp.DOG_NAME_QUESTION_KEY, "")
            self.name_entry_var.set(current_name) # Set var, not just entry

            self.name_entry_widget = tk.Entry(
                content_area, font=(DogActivityApp.FONT_HELVETICA, DogActivityApp.FONT_SIZE_HEADINGS_BOLD),
                width=30, textvariable=self.name_entry_var,
                bg=self.theme["entry_bg"], fg=self.theme["entry_fg"],
                insertbackground=self.theme["entry_cursor"]
            )
            self.name_entry_widget.pack(pady=5)
            self.name_entry_widget.focus()

            if self.dog_photo_imgtk:
                self.photo_preview_label.config(image=self.dog_photo_imgtk, bg=self.theme["app_bg"])
                self.photo_preview_label.pack(in_=content_area, pady=10)

            tk.Button(
                content_area, text="Upload Dog Photo (Optional)", width=25,
                relief=self.theme["button_relief"], bg=self.theme["button_upload_bg"],
                fg=self.theme["button_fg"], command=self.select_photo
            ).pack(pady=10)
        else:
            option_buttons_frame = tk.Frame(content_area, bg=self.theme["app_bg"])
            option_buttons_frame.pack()
            for opt in options:
                btn_style = ttk.Style()
                btn_style_name = f"{opt.replace(' ','')}.TButton"
                # Basic styling for ttk buttons if needed, can be expanded
                btn_style.configure(btn_style_name, font=(DogActivityApp.FONT_HELVETICA, DogActivityApp.FONT_SIZE_OPTIONS_SUMMARY_RECOMMENDATIONS-1),
                                    background=self.theme.get("button_option_bg", "#FFFFFF"), # Fallback
                                    foreground=self.theme.get("button_fg", "#000000"))
                                    
                b = ttk.Button(
                    option_buttons_frame, text=opt, width=25, # Increased width
                    style=btn_style_name, # Apply custom style if defined
                    command=lambda o=opt: self.next_question(o)
                )
                b.pack(pady=4, ipady=3) # Increased internal padding

        nav_frame = tk.Frame(self.question_frame, bg=self.theme["app_bg"])
        nav_frame.pack(side="bottom", fill="x", pady=(10,15), padx=10)

        prev_button = ttk.Button(nav_frame, text="⬅ Previous", width=12, command=self.previous_question)
        prev_button.pack(side="left", padx=(0,5))
        prev_button.config(state="disabled" if self.current_question_index == 0 else "normal")

        if question_key == DogActivityApp.DOG_NAME_QUESTION_KEY:
            self.next_button_name = ttk.Button(nav_frame, text="Next ➡", width=12, command=self._submit_dog_name_and_proceed)
            self.next_button_name.pack(side="right", padx=(5,0))
            if self._name_trace_id: self.name_entry_var.trace_remove("write", self._name_trace_id)
            self._name_trace_id = self.name_entry_var.trace_add("write", self._update_next_button_state_for_name)
            self._update_next_button_state_for_name() # Initial state check

    def _update_next_button_state_for_name(self, *args):
        if self.next_button_name and self.next_button_name.winfo_exists():
            name_val = self.name_entry_var.get().strip()
            self.next_button_name.config(state="normal" if name_val else "disabled")
            if name_val: self.show_message("") 

    def _submit_dog_name_and_proceed(self):
        name_val = self.name_entry_var.get().strip()
        if not name_val:
            self.show_message("Please enter your dog's name.", error=True)
            if self.name_entry_widget and self.name_entry_widget.winfo_exists(): self.name_entry_widget.focus()
            return
        self.next_question(name_val)

    def next_question(self, selected_option):
        question_key, _ = DogActivityApp.QUESTIONS_CONFIG[self.current_question_index]
        self.answers[question_key] = selected_option
        self.current_question_index += 1
        self.progress_var.set(self.current_question_index)

        if self.current_question_index < DogActivityApp.QUESTION_COUNT:
            self.show_question()
        else:
            self.question_frame.pack_forget() # Hide question frame
            self.progress_frame.pack_forget() # Hide progress bar
            self.show_summary()

    def previous_question(self):
        # Called from questions, summary, or results page
        if self.result_frame.winfo_ismapped(): # Coming from results page
            self.result_frame.pack_forget()
            self.show_summary() # Go to summary from results
            return

        if self.current_question_index > 0:
            # If on summary (index == Q_COUNT), going back means to last question (index Q_COUNT-1)
            if self.current_question_index == DogActivityApp.QUESTION_COUNT: 
                 self.current_question_index -=1 # To last question index
            elif self.current_question_index > 0 : # Already on a question page
                 self.current_question_index -= 1
            
            self.progress_var.set(self.current_question_index)
            
            # Ensure frames are correctly displayed for question view
            self.message_frame.pack_forget() # Clear any messages
            if not self.progress_frame.winfo_ismapped():
                self.progress_frame.pack(fill="x", pady=5, padx=10, side="top", before=self.question_frame)
            if not self.question_frame.winfo_ismapped():
                self.question_frame.pack(pady=10, fill="both", expand=True)
            
            self.show_question()

    def show_summary(self):
        self.welcome_frame.pack_forget()
        self.result_frame.pack_forget() 
        self.message_frame.pack_forget()

        # Summary is shown in the question_frame area, but progress is full
        if not self.progress_frame.winfo_ismapped():
             self.progress_frame.pack(fill="x", pady=5, padx=10, side="top")
        self.progress_var.set(DogActivityApp.QUESTION_COUNT) # Progress is full

        if not self.question_frame.winfo_ismapped():
             self.question_frame.pack(pady=20, fill="both", expand=True)
        
        for widget in self.question_frame.winfo_children(): widget.destroy()

        tk.Label(self.question_frame, text="📋 Summary of Your Answers:",
                 font=(DogActivityApp.FONT_HELVETICA, DogActivityApp.FONT_SIZE_WELCOME, "bold"),
                 bg=self.theme["app_bg"], fg=self.theme["text_fg"]
        ).pack(pady=10)

        summary_text_frame = tk.Frame(self.question_frame, bg=self.theme["app_bg"])
        summary_text_frame.pack(pady=10, padx=20, fill="x")

        for i, (q_text, _) in enumerate(DogActivityApp.QUESTIONS_CONFIG):
            val = self.answers.get(q_text, "Not answered")
            tk.Label(summary_text_frame, text=f"{q_text}:",
                     font=(DogActivityApp.FONT_HELVETICA, DogActivityApp.FONT_SIZE_OPTIONS_SUMMARY_RECOMMENDATIONS, "bold"),
                     bg=self.theme["app_bg"], fg=self.theme["text_fg"], anchor="e" # Align question to right
            ).grid(row=i, column=0, sticky="ew", pady=2, padx=(0,5))
            tk.Label(summary_text_frame, text=f"{val}",
                     font=(DogActivityApp.FONT_HELVETICA, DogActivityApp.FONT_SIZE_OPTIONS_SUMMARY_RECOMMENDATIONS),
                     bg=self.theme["app_bg"], fg=self.theme["text_fg"], anchor="w", wraplength=300
            ).grid(row=i, column=1, sticky="ew", pady=2, padx=(5,0))
        summary_text_frame.columnconfigure(0, weight=1) # Question text column
        summary_text_frame.columnconfigure(1, weight=2) # Answer text column, more space


        btn_frame = tk.Frame(self.question_frame, bg=self.theme["app_bg"])
        btn_frame.pack(pady=20) 
        
        # Center buttons in btn_frame
        actual_btn_container = tk.Frame(btn_frame, bg=self.theme["app_bg"])
        actual_btn_container.pack()

        ttk.Button(actual_btn_container, text="Get Recommendations 💡", width=22, command=self.get_recommendations).pack(side="left", padx=5, ipady=2)
        ttk.Button(actual_btn_container, text="⬅ Back to Questions", width=18, command=self.previous_question).pack(side="left", padx=5, ipady=2)
        ttk.Button(actual_btn_container, text="🔁 Start Over", width=15, command=self.restart).pack(side="left", padx=5, ipady=2)
    
    def get_recommendations(self):
        if len(self.answers) < DogActivityApp.QUESTION_COUNT:
            self.show_message("Please answer all questions first.", error=True)
            self.show_summary(); return

        age = self.answers.get("Age Group")
        energy = self.answers.get("Energy Level")
        health = self.answers.get("Health or Mobility Issues")
        temperament = self.answers.get("Temperament")
        location = self.answers.get("Preferred Activity Location")
        weather = self.answers.get("Current Weather")
        dog_name = self.answers.get(DogActivityApp.DOG_NAME_QUESTION_KEY, "your dog")

        recs = []
        if health == "Joint Issues": recs.append("❤️‍🩹 Gentle walks, consider hydrotherapy. Avoid high impact exercises like jumping.")
        if temperament == "Aggressive":
            recs = ["⚠️ SAFETY FIRST: Work with a certified professional dog trainer or veterinary behaviorist IMMEDIATELY. Focus on management and safety to prevent bites.",
                    " muzzle train your dog for safety during necessary outings."] # Crucial advice first
        elif age == "Puppy":
            recs.append("🐾 Short, frequent play sessions focusing on positive socialization with various sights, sounds, and (safe) dogs/people.")
            recs.append("🚫 Avoid strenuous, long-duration, or repetitive high-impact exercise (like long runs or repeated jumping) until growth plates close (typically 12-18 months).")
        
        if temperament != "Aggressive":
            if energy == "High": recs.append(f"🏃‍♂️ High-energy? Try fetch, flirt pole, or controlled running games in a secure area.")
            elif energy == "Medium": recs.append("🎾 Medium energy? Tug-of-war, puzzle toys, or a brisk walk are great.")
            else: recs.append("🛋️ Low-energy? Gentle indoor nose games like 'find the treat' or short, sniffy walks.")

            if self.answers.get("Likes Swimming?") == "Yes": recs.append("💧 Likes swimming? If safe and supervised, a short swim is excellent low-impact exercise.")
            if self.answers.get("Likes Fetch?") == "Yes": recs.append("🎾 Loves fetch? Vary distances and try different toys (soft frisbees, balls).")
            if self.answers.get("Enjoys Mental Challenges?") == "Yes":
                recs.append("🧩 Enjoys mental challenges? Use food-dispensing puzzle toys, teach new tricks, or play scent games.")

        if weather == "Hot": recs.append("☀️ Hot weather: Prioritize early morning/late evening activities. Check pavement temperature. Ensure constant access to water. Consider indoor cooling activities.")
        elif weather == "Rainy": recs.append("🌧️ Rainy day? Indoor hide-and-seek with treats, puzzle toys, or a short training session.")
        elif weather == "Cold": recs.append("❄️ Cold weather? Short, brisk walks (consider a coat/booties for sensitive dogs). Indoor play and mental stimulation are key.")
        
        final_recs = []
        seen = set()
        for r in recs:
            if r not in seen: final_recs.append(r); seen.add(r)

        generic_activities = {
            "Inside": [
                "🧸 Indoor fetch with a soft toy in a safe, clear space.",
                "🎓 Teach a new trick (e.g., 'spin', 'touch', 'go to mat').",
                "👃 Scent game: Hide treats around a room for your dog to find.",
                "🏠 DIY indoor agility: Use pillows for tunnels, broomsticks for low jumps (ensure safety)."
            ],
            "Outside": [
                "🌳 Leashed neighborhood walk, varying the route for new smells.",
                "🎾 Classic fetch in a secure, fenced yard (if appropriate for dog).",
                "🐾 'Sniffari': Allow your dog to lead and sniff extensively on a loose leash in a safe area.",
                "💧 Water play: Supervised fun with a sprinkler or kiddy pool (if weather and dog permit)."
            ]
        }
        
        # Ensure at least a few recommendations, especially if not aggressive
        if temperament == "Aggressive" and len(final_recs) >=1: # Primary advice is key
            pass
        else:
            pool = generic_activities.get(location, generic_activities["Inside"]) # Default to inside if somehow no location
            idx = 0
            while len(final_recs) < 4 and idx < len(pool):
                if pool[idx] not in seen: final_recs.append(pool[idx]); seen.add(pool[idx])
                idx += 1
        
        if not final_recs: # Ultimate fallback
            final_recs.append(f"🥰 Spend some quality time with {dog_name}, perhaps some gentle petting or a favorite calm game.")

        result_text = f"📝 Recommended activities for {dog_name} ({location.lower()} location):\n\n" + \
                      "\n".join(f"• {rec}" for rec in final_recs)
        self._show_recommendations_page(result_text)


    def _copy_to_clipboard(self, text_to_copy):
        try:
            self.root.clipboard_clear()
            self.root.clipboard_append(text_to_copy)
            self.show_message("📋 Recommendations copied to clipboard!")
        except tk.TclError:
            self.show_message("Error: Could not access clipboard. Is xclip/xsel installed (Linux)?", error=True)
        except Exception as e:
            self.show_message(f"Error copying: {e}", error=True)

    def _export_to_file(self, text_to_export):
        try:
            file_path = filedialog.asksaveasfilename(
                defaultextension=".txt",
                filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")],
                title="Export Recommendations As..."
            )
        except Exception as e: self.show_message(f"Error opening save dialog: {e}", error=True); return
        if not file_path: return

        try:
            with open(file_path, "w", encoding="utf-8") as f: f.write(text_to_export)
            messagebox.showinfo("Export Successful", f"Recommendations saved to:\n{file_path}")
            self.show_message("") # Clear potential error messages
        except Exception as e:
            messagebox.showerror("Error Exporting", f"Could not save file: {e}")

    def _show_recommendations_page(self, recommendations_text):
        self.question_frame.pack_forget()
        self.progress_frame.pack_forget()
        self.welcome_frame.pack_forget()
        self.message_frame.pack_forget()

        for w in self.result_frame.winfo_children(): w.destroy()
        if not self.result_frame.winfo_ismapped():
            self.result_frame.pack(pady=10, fill="both", expand=True)
        
        self.result_frame.grid_rowconfigure(0, weight=1) # Canvas row
        self.result_frame.grid_columnconfigure(0, weight=1) # Canvas col
        self.result_frame.grid_columnconfigure(1, weight=0) # Scrollbar col

        # --- Button Frame (Fixed at Bottom) ---
        button_panel = tk.Frame(self.result_frame, bg=self.theme["app_bg"])
        button_panel.grid(row=1, column=0, columnspan=2, sticky="ew", pady=(5, 10), padx=10)
        
        actual_buttons_container = tk.Frame(button_panel, bg=self.theme["app_bg"])
        actual_buttons_container.pack(pady=5) # This frame will hold buttons and be centered by its parent's pack

        btn_font = (DogActivityApp.FONT_HELVETICA, 11) # Common font for these buttons

        copy_btn = ttk.Button(actual_buttons_container, text="📋 Copy", width=12, command=lambda: self._copy_to_clipboard(recommendations_text))
        copy_btn.pack(side="left", padx=5, ipady=2)

        export_btn = tk.Button(
            actual_buttons_container, text="💾 Export", width=12,
            relief=self.theme["button_relief"], bg=self.theme["button_export_bg"],
            fg=self.theme["button_fg"], font=btn_font,
            command=lambda: self._export_to_file(recommendations_text)
        )
        export_btn.pack(side="left", padx=5, ipady=1 if tk.TkVersion >= 8.6 else 0)

        back_btn = ttk.Button(actual_buttons_container, text="⬅ Back to Summary", width=18, command=self.previous_question) # Goes to summary
        back_btn.pack(side="left", padx=5, ipady=2)

        restart_btn = ttk.Button(actual_buttons_container, text="🔁 Start Over", width=15, command=self.restart)
        restart_btn.pack(side="left", padx=5, ipady=2)


        # --- Scrollable Area for Photo and Text (Above Buttons) ---
        self.scrollable_canvas = tk.Canvas(self.result_frame, bg=self.theme["app_bg"], highlightthickness=0)
        self.scrollable_canvas.grid(row=0, column=0, sticky="nsew")

        scrollbar = ttk.Scrollbar(self.result_frame, orient="vertical", command=self.scrollable_canvas.yview)
        scrollbar.grid(row=0, column=1, sticky="ns")
        self.scrollable_canvas.configure(yscrollcommand=scrollbar.set)

        inner_scrollable_frame = tk.Frame(self.scrollable_canvas, bg=self.theme["app_bg"])
        self.scrollable_canvas.create_window((0, 0), window=inner_scrollable_frame, anchor="nw", tags="inner_frame")

        def _configure_inner_frame(event):
            # Update the scroll Toplevel of the canvas to encompass the inner frame
            self.scrollable_canvas.config(scrollregion=self.scrollable_canvas.bbox("all"))
            # Update canvas window width to match canvas width for wraplength
            self.scrollable_canvas.itemconfig("inner_frame", width=event.width)
            self._adjust_wraplength() # Re-adjust wraplength for rec_display_label

        def _configure_canvas(event):
            # Update the inner_frame's width to match the canvas's width
            self.scrollable_canvas.itemconfig("inner_frame", width=event.width)
            self._adjust_wraplength()


        inner_scrollable_frame.bind("<Configure>", _configure_inner_frame)
        self.scrollable_canvas.bind("<Configure>", _configure_canvas)


        # Content inside the scrollable frame
        current_row = 0
        if self.dog_photo_imgtk:
            photo_label_scroll = tk.Label(inner_scrollable_frame, image=self.dog_photo_imgtk, bg=self.theme["app_bg"])
            photo_label_scroll.grid(row=current_row, column=0, pady=(10,5), padx=10)
            current_row += 1

        self.rec_display_label = tk.Label(
            inner_scrollable_frame, text=recommendations_text,
            font=(DogActivityApp.FONT_HELVETICA, DogActivityApp.FONT_SIZE_OPTIONS_SUMMARY_RECOMMENDATIONS),
            bg=self.theme["app_bg"], fg=self.theme["text_fg"], justify="left", anchor="nw"
        )
        self.rec_display_label.grid(row=current_row, column=0, sticky="ew", padx=10, pady=(5,10))
        inner_scrollable_frame.columnconfigure(0, weight=1) # Allow text label to expand width
        
        self.show_message("") # Clear any lingering messages
        self.root.update_idletasks() # Ensure everything is drawn
        self._adjust_wraplength() # Final adjustment
        self.scrollable_canvas.config(scrollregion=self.scrollable_canvas.bbox("all")) # Set initial scrollregion


    def on_closing(self):
        dog_name = self.answers.get(DogActivityApp.DOG_NAME_QUESTION_KEY, "your furry friend")
        goodbye_title = "Goodbye! 🐾"
        goodbye_message = (f"Thanks for using the Dog Activity Recommender!\n\n"
                           f"Hope you and {dog_name} have a fantastic time with your new activities! 👋")
        if not self.answers and self.current_question_index == 0 and self.welcome_frame.winfo_ismapped():
            goodbye_message = ("Thanks for checking out the Dog Activity Recommender!\n\n"
                               "Come back soon to find paw-some activities! 🐶")
        try:
            messagebox.showinfo(goodbye_title, goodbye_message)
        except Exception as e: print(f"Error displaying closing message: {e}")
        finally:
            print("Dog Activity Recommender is closing.")
            if self.root:
                try: self.root.destroy()
                except tk.TclError as e: print(f"Error destroying root window: {e}")


if __name__ == '__main__':
    root = tk.Tk()
    app = DogActivityApp(root)
    root.mainloop()