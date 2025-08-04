import tkinter as tk
from tkinter import ttk, filedialog, messagebox
from PIL import Image, ImageTk, ImageDraw
import darkdetect # For detecting OS theme

class DogActivityApp:
    # --- Define Color Palettes ---
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
        "button_summary_nav_bg": "#366092",
        "message_success_fg": "#77dd77",
        "message_error_fg": "#ff6961",
        "message_info_fg": "#e0e0e0",
        "progressbar_bg": "#38761d",
        "progressbar_troughcolor": "#3c3c3c"
    }

    # --- Original Constants ---
    INITIAL_WINDOW_GEOMETRY = "520x670"
    PROGRESS_BAR_LENGTH = 450
    FONT_HELVETICA = "Helvetica"
    FONT_SIZE_WELCOME = 16
    FONT_SIZE_HEADINGS_BOLD = 15
    FONT_SIZE_BUTTON_MAIN_BOLD = 15
    FONT_SIZE_OPTIONS_SUMMARY_RECOMMENDATIONS = 14
    PHOTO_PREVIEW_DIMENSIONS = (250, 250)
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
    ]
    QUESTION_COUNT = len(QUESTIONS_CONFIG)
    DOG_NAME_QUESTION_KEY = "Dog's Name"

    def __init__(self, root_window):
        """
        Initializes the Dog Activity Recommender application.

        This constructor sets up the main application window, detects the
        operating system's theme (light/dark mode) to apply appropriate colors,
        initializes application state variables (like current question, answers),
        and creates the main UI frames and the progress bar. It also binds
        event handlers for window resizing and closing.

        Args:
            root_window (tk.Tk): The main Tkinter window for the application.
        """
        self.root = root_window

        try:
            current_os_theme = darkdetect.theme()
            if current_os_theme is None:
                 current_os_theme = "Light" # Fallback if detection returns None
        except Exception: # General fallback if darkdetect library fails
            current_os_theme = "Light"
            print("Warning: Could not detect OS theme using darkdetect. Defaulting to Light theme.")

        if current_os_theme == "Dark":
            self.theme = DogActivityApp.DARK_THEME
        else:
            self.theme = DogActivityApp.LIGHT_THEME

        self.root.title("🐶 Dog Activity Recommender")
        self.root.geometry(DogActivityApp.INITIAL_WINDOW_GEOMETRY)
        self.root.configure(bg=self.theme["app_bg"])

        # --- Initialize App State ---
        self.dog_photo_path = None
        self.dog_photo_imgtk = None # To hold the PhotoImage object for Tkinter
        self.answers = {} # Stores user's answers to questions
        self.current_question_index = 0 # Tracks the current question

        # --- Name Entry specific ---
        self.name_entry_widget = None
        self.name_entry_var = tk.StringVar() # Variable for dog's name entry
        self.next_button_name = None # Holds the 'Next' button widget for the name question
        self._name_trace_id = None # To manage the trace on name_entry_var

        # --- UI Frames ---
        self.welcome_frame = tk.Frame(self.root, bg=self.theme["app_bg"])
        self.message_frame = tk.Frame(self.root, bg=self.theme["app_bg"]) # For displaying messages
        self.question_frame = tk.Frame(self.root, bg=self.theme["app_bg"]) # Main content for questions
        self.progress_frame = tk.Frame(self.root, bg=self.theme["app_bg"]) # Contains the progress bar
        self.result_frame = tk.Frame(self.root, bg=self.theme["app_bg"])   # For displaying recommendations

        # --- Photo Preview Label (reused) ---
        self.photo_preview_label = tk.Label(bg=self.theme["app_bg"])

        # --- Progress Bar ---
        self.progress_var = tk.IntVar()
        self.ttk_style = ttk.Style()
        self.ttk_style.theme_use('default')
        self.ttk_style.configure("themed.Horizontal.TProgressbar",
                                 background=self.theme["progressbar_bg"],
                                 troughcolor=self.theme["progressbar_troughcolor"],
                                 bordercolor=self.theme["app_bg"],
                                 lightcolor=self.theme["progressbar_bg"],
                                 darkcolor=self.theme["progressbar_bg"])
        self.progress_bar = ttk.Progressbar(self.progress_frame, style="themed.Horizontal.TProgressbar",
                                            length=DogActivityApp.PROGRESS_BAR_LENGTH,
                                            mode="determinate",
                                            maximum=DogActivityApp.QUESTION_COUNT,
                                            variable=self.progress_var)
        self.progress_bar.pack(fill="x", expand=True, padx=10, pady=5)

        self._setup_welcome_screen()
        self.root.bind("<Configure>", self._adjust_wraplength) # Handle window resize
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing) # Handle window close button

    def _setup_welcome_screen(self):
        """
        Sets up and displays the initial welcome screen of the application.

        This method clears any other active views (questions, results, etc.)
        and presents a welcome message and a "Start" button to begin the quiz.
        """
        self.message_frame.pack_forget()
        self.question_frame.pack_forget()
        self.progress_frame.pack_forget()
        self.result_frame.pack_forget()

        self.welcome_frame.pack(padx=10, pady=30, fill="both", expand=True)
        # Clear any previous widgets in the welcome frame before repopulating
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
            justify="center", wraplength=460,
        )
        self.welcome_msg_label.pack(pady=60)

        start_button = tk.Button(self.welcome_frame, text="Start 🐕",
                                 font=(DogActivityApp.FONT_HELVETICA, DogActivityApp.FONT_SIZE_BUTTON_MAIN_BOLD, "bold"),
                                 width=15, relief=self.theme["button_relief"],
                                 bg=self.theme["button_start_bg"], fg=self.theme["button_fg"],
                                 command=self.start_quiz)
        start_button.pack(pady=10)

    def _adjust_wraplength(self, event=None):
        """
        Adjusts the `wraplength` property of dynamic text labels when the window is resized.

        This ensures that text within the welcome message, displayed recommendations,
        and any informational messages reflows correctly to fit the new window width,
        preventing text from being cut off or poorly formatted.

        Args:
            event (tk.Event, optional): The event object passed by Tkinter when a
                                         <Configure> event occurs (e.g., window resize).
                                         Defaults to None.
        """
        if hasattr(self, 'welcome_msg_label') and self.welcome_msg_label.winfo_ismapped():
            new_wraplength = self.welcome_msg_label.master.winfo_width() - 40
            if new_wraplength > 100: self.welcome_msg_label.config(wraplength=new_wraplength)

        if hasattr(self, 'rec_display_label') and self.rec_display_label.winfo_ismapped():
            new_wraplength = self.rec_display_label.master.winfo_width() - 60
            if new_wraplength > 100: self.rec_display_label.config(wraplength=new_wraplength)

        if hasattr(self, 'msg_display_label') and self.msg_display_label.winfo_ismapped():
            new_wraplength = self.msg_display_label.master.winfo_width() - 40
            if new_wraplength > 100: self.msg_display_label.config(wraplength=new_wraplength)

    def show_message(self, message, error=False):
        """
        Displays a message to the user in a dedicated message area.

        The message area is typically shown at the top of the current view.
        It can display informational messages, success confirmations (e.g., "copied to clipboard"),
        or error messages, which are styled with different text colors based on the theme.
        If the `message` argument is empty, any existing message is cleared and the
        message area is hidden.

        Args:
            message (str): The text of the message to display.
            error (bool, optional): If True, the message is styled as an error.
                                   Defaults to False.
        """
        # Clear previous message content from the frame
        for widget in self.message_frame.winfo_children():
            widget.destroy()

        if message: # If there's a new message to display
            # Determine where to pack the message_frame (before the current active main frame)
            if not self.message_frame.winfo_ismapped():
                active_main_frame = None
                if self.result_frame.winfo_ismapped(): active_main_frame = self.result_frame
                elif self.question_frame.winfo_ismapped(): active_main_frame = self.question_frame
                elif self.progress_frame.winfo_ismapped(): active_main_frame = self.progress_frame
                # (Welcome frame doesn't usually have messages above it in this app design)

                if active_main_frame:
                    self.message_frame.pack(fill="x", pady=(5,0), padx=10, before=active_main_frame)
                else: # Fallback if no other main frame is active (should ideally not happen during quiz/results)
                     self.message_frame.pack(fill="x", pady=(5,0), padx=10)
            
            # Determine text color based on message type and theme
            fg_color = self.theme["message_error_fg"] if error else \
                       self.theme["message_success_fg"] if "copied" in message.lower() else \
                       self.theme["message_info_fg"]
            
            wraplength = self.root.winfo_width() - 40 if self.root.winfo_width() > 50 else 300
            self.msg_display_label = tk.Label(self.message_frame, text=message,
                                              font=(DogActivityApp.FONT_HELVETICA, DogActivityApp.FONT_SIZE_HEADINGS_BOLD),
                                              bg=self.theme["app_bg"], fg=fg_color,
                                              justify="left", wraplength=max(100, wraplength))
            self.msg_display_label.pack(pady=(0,5))
            self._adjust_wraplength() # Adjust wraplength after displaying
        elif self.message_frame.winfo_ismapped(): # If message is empty, hide the frame
             self.message_frame.pack_forget()


    def select_photo(self):
        """
        Opens a system file dialog for the user to select a dog photo.

        If a photo is selected, it is loaded using PIL, resized, and a circular
        mask is applied. The processed image is then stored as a PhotoImage
        object for display in Tkinter. Error messages are shown for issues like
        file not found or invalid image format. If successful on the name question,
        the question view is refreshed to show the photo.
        """
        temp_current_name = ""
        if self.current_question_index == 0 and DogActivityApp.QUESTIONS_CONFIG[self.current_question_index][0] == DogActivityApp.DOG_NAME_QUESTION_KEY:
            if self.name_entry_var: temp_current_name = self.name_entry_var.get()

        path = None
        try:
            path = filedialog.askopenfilename(
                title="Select Dog Photo",
                filetypes=[("Image Files", "*.png *.jpg *.jpeg *.bmp *.gif")]
            )
        except Exception as e:
            self.show_message(f"Error opening file dialog: {e}", error=True)
            return
        else:
            if not path:
                self.show_message("No file selected.", error=True)
                return
        finally:
            pass

        if path: # Proceed only if a path was selected
            self.dog_photo_path = path
            try:
                img = Image.open(self.dog_photo_path).convert("RGBA")
                img = img.resize(DogActivityApp.PHOTO_PREVIEW_DIMENSIONS, Image.LANCZOS)
                mask = Image.new('L', DogActivityApp.PHOTO_PREVIEW_DIMENSIONS, 0)
                draw = ImageDraw.Draw(mask)
                draw.ellipse((0, 0, DogActivityApp.PHOTO_PREVIEW_DIMENSIONS[0], DogActivityApp.PHOTO_PREVIEW_DIMENSIONS[1]), fill=255)
                img.putalpha(mask)
                self.dog_photo_imgtk = ImageTk.PhotoImage(img)

            except FileNotFoundError:
                self.show_message(f"Error: The image file was not found at the selected path.", error=True)
                self.dog_photo_imgtk = None
                if self.current_question_index == 0 and DogActivityApp.QUESTIONS_CONFIG[self.current_question_index][0] == DogActivityApp.DOG_NAME_QUESTION_KEY and self.name_entry_var:
                    self.name_entry_var.set(temp_current_name) # Restore name if photo load fails
                return
            except Image.UnidentifiedImageError:
                self.show_message("Error: Cannot identify image file. Please select a valid image format (e.g., PNG, JPG).", error=True)
                self.dog_photo_imgtk = None
                if self.current_question_index == 0 and DogActivityApp.QUESTIONS_CONFIG[self.current_question_index][0] == DogActivityApp.DOG_NAME_QUESTION_KEY and self.name_entry_var:
                    self.name_entry_var.set(temp_current_name)
                return
            except Exception as e:
                self.show_message(f"Error loading image: {e}", error=True)
                self.show_message(f"Error loading image: {e}", error=True)
                self.dog_photo_imgtk = None
                if self.current_question_index == 0 and DogActivityApp.QUESTIONS_CONFIG[self.current_question_index][0] == DogActivityApp.DOG_NAME_QUESTION_KEY and self.name_entry_var:
                    self.name_entry_var.set(temp_current_name)
                return
            else:
                self.show_message("Image loaded successfully!", error=False)
            finally:
                pass

            # If successful and on the first question, refresh the question display to show the photo
            if self.current_question_index == 0 and DogActivityApp.QUESTIONS_CONFIG[self.current_question_index][0] == DogActivityApp.DOG_NAME_QUESTION_KEY:
                self.show_question() # Refresh to show the image preview
                if self.name_entry_var: # Keep existing name if any
                    self.name_entry_var.set(temp_current_name)


    def start_quiz(self):
        """
        Starts or restarts the quiz from the beginning.

        This method resets all application state variables related to the quiz
        (answers, current question index, dog photo, progress bar). It then
        hides any active views (welcome, results) and displays the first question.
        """
        self.welcome_frame.pack_forget()
        self.result_frame.pack_forget() 
        self.message_frame.pack_forget() 
        
        self.question_frame.pack(pady=10, fill="both", expand=True)
        self.progress_frame.pack(fill="x", pady=5, padx=10, before=self.question_frame)
        
        self.progress_var.set(0)
        self.current_question_index = 0
        self.answers.clear()
        self.dog_photo_imgtk = None
        self.dog_photo_path = None
        self.show_question()

    def restart(self):
        """
        Resets the entire application to its initial state (welcome screen).

        This clears all stored answers, the dog photo, resets the quiz progress,
        and hides all active quiz/result views, then displays the welcome screen.
        """
        self.answers.clear()
        self.dog_photo_imgtk = None
        self.dog_photo_path = None
        self.current_question_index = 0
        self.progress_var.set(0)
        
        self.result_frame.pack_forget()
        self.question_frame.pack_forget()
        self.progress_frame.pack_forget()
        self.message_frame.pack_forget()
        
        self._setup_welcome_screen()
        self._adjust_wraplength()

    def show_question(self):
        """
        Displays the current question based on `self.current_question_index`.

        This method is responsible for dynamically building the UI for the current
        question. It clears any previous question from the `question_frame`.
        If the question is for the "Dog's Name", it shows an entry field and an
        option to upload a photo. For other questions, it displays a set of
        option buttons (now `ttk.Button`). It also sets up "Previous" and "Next"
        navigation `ttk.Button`s and updates their state.
        """
        self.show_message("") # Clear any previous messages (e.g., "Copied!")
        
        # Clear previous question content from the frame
        for widget in self.question_frame.winfo_children():
            widget.destroy()
        self.photo_preview_label.pack_forget() # Ensure reused label is hidden initially

        question_key, options = DogActivityApp.QUESTIONS_CONFIG[self.current_question_index]
        
        # Display question title
        tk.Label(self.question_frame, text=question_key,
                 font=(DogActivityApp.FONT_HELVETICA, DogActivityApp.FONT_SIZE_HEADINGS_BOLD, "bold"),
                 bg=self.theme["app_bg"], fg=self.theme["text_fg"]).pack(pady=(15,10))
        
        # Frame for question-specific content (entry or options)
        content_area = tk.Frame(self.question_frame, bg=self.theme["app_bg"])
        content_area.pack(pady=10, fill="both", expand=True)

        if question_key == DogActivityApp.DOG_NAME_QUESTION_KEY:
            # Restore name from answers if navigating back, or keep current entry text
            current_name_in_entry = self.name_entry_var.get()
            if not current_name_in_entry and DogActivityApp.DOG_NAME_QUESTION_KEY in self.answers:
                 self.name_entry_var.set(self.answers.get(DogActivityApp.DOG_NAME_QUESTION_KEY, ""))
            elif not current_name_in_entry: # Ensure it's empty if no answer and no current entry
                 self.name_entry_var.set("")

            self.name_entry_widget = tk.Entry(content_area,
                                              font=(DogActivityApp.FONT_HELVETICA, DogActivityApp.FONT_SIZE_HEADINGS_BOLD),
                                              width=30, textvariable=self.name_entry_var,
                                              bg=self.theme["entry_bg"], fg=self.theme["entry_fg"],
                                              insertbackground=self.theme["entry_cursor"])
            self.name_entry_widget.pack(pady=5)
            self.name_entry_widget.focus()

            if self.dog_photo_imgtk: # If a photo has been loaded
                self.photo_preview_label.config(image=self.dog_photo_imgtk, bg=self.theme["app_bg"])
                self.photo_preview_label.pack(in_=content_area, pady=10)

            # Upload photo button (can remain tk.Button if specific styling is preferred and works)
            tk.Button(content_area, text="Upload Dog Photo (Optional)", width=25,
                      relief=self.theme["button_relief"],
                      bg=self.theme["button_upload_bg"], fg=self.theme["button_fg"],
                      command=self.select_photo).pack(pady=10)
        else: # Multiple choice question
            option_buttons_frame = tk.Frame(content_area, bg=self.theme["app_bg"])
            option_buttons_frame.pack()
            for opt in options:
                # Switched to ttk.Button for better theme adaptability
                b = ttk.Button(option_buttons_frame, text=opt, width=20,
                               command=lambda o=opt: self.next_question(o))
                b.pack(pady=4, ipady=2) # Note: ipady might not have the same effect on ttk.Button

        # Navigation buttons frame
        nav_frame = tk.Frame(self.question_frame, bg=self.theme["app_bg"])
        nav_frame.pack(side="bottom", fill="x", pady=(10,15), padx=10)

        prev_button = ttk.Button(nav_frame, text="Previous", width=12, # Switched to ttk.Button
                                 command=self.previous_question)
        prev_button.pack(side="left", padx=(0, 5))
        # ttk.Button state is also set via .config(state=...) or directly in constructor
        prev_button.config(state="disabled" if self.current_question_index == 0 else "normal")

        if question_key == DogActivityApp.DOG_NAME_QUESTION_KEY:
            self.next_button_name = ttk.Button(nav_frame, text="Next", width=12, # Switched to ttk.Button
                                               command=self._submit_dog_name_and_proceed)
            self.next_button_name.pack(side="right", padx=(5, 0))
            # Manage trace for enabling/disabling Next button based on name entry
            if self._name_trace_id: self.name_entry_var.trace_remove("write", self._name_trace_id)
            self._name_trace_id = self.name_entry_var.trace_add("write", self._update_next_button_state_for_name)
            self._update_next_button_state_for_name() # Initial check

    def _update_next_button_state_for_name(self, *args):
        """
        Updates the state (enabled/disabled) of the 'Next' button for the dog's name question.

        The button is enabled only if the name entry field is not empty.
        This method is typically triggered by changes to the `name_entry_var`
        (the `StringVar` linked to the name entry field).

        Args:
            *args: Variable arguments passed by the trace event (not used directly).
        """
        if self.next_button_name and self.next_button_name.winfo_exists():
            name_val = self.name_entry_var.get().strip()
            self.next_button_name.config(state="normal" if name_val else "disabled")
            if name_val: self.show_message("") # Clear "name required" message if it was shown

    def _submit_dog_name_and_proceed(self):
        """
        Validates the dog's name entered by the user and proceeds to the next question.

        If the name field is empty, an error message is displayed, and the focus
        is returned to the name entry field. Otherwise, it calls `next_question`
        with the entered name.
        """
        name_val = self.name_entry_var.get().strip()
        if not name_val:
            self.show_message("Please enter your dog's name.", error=True)
            if self.name_entry_widget and self.name_entry_widget.winfo_exists():
                self.name_entry_widget.focus()
            return
        self.next_question(name_val)

    def next_question(self, selected_option):
        """
        Saves the user's answer for the current question and moves to the next question.

        It updates the `self.answers` dictionary, increments the
        `current_question_index`, updates the progress bar, and then either calls
        `show_question` to display the next question or `show_summary` if all
        questions have been answered.

        Args:
            selected_option (str): The option selected or value entered by the user
                                   for the current question.
        """
        question_key, _ = DogActivityApp.QUESTIONS_CONFIG[self.current_question_index]
        self.answers[question_key] = selected_option
        self.current_question_index += 1
        self.progress_var.set(self.current_question_index)

        if self.current_question_index < DogActivityApp.QUESTION_COUNT:
            self.show_question()
        else:
            self.question_frame.pack_forget() # Hide question frame before showing summary
            # self.show_message("") # Not strictly needed, show_summary will clear it
            self.show_summary()

    def previous_question(self):
        """
        Navigates to the previous question in the quiz.

        Decrements the `current_question_index`, updates the progress bar,
        hides the results frame (if visible), and then calls `show_question`
        to display the content of the previous question.
        """
        if self.current_question_index > 0:
            # If on summary/results page, current_question_index might be QUESTION_COUNT
            if self.current_question_index >= DogActivityApp.QUESTION_COUNT:
                self.current_question_index = DogActivityApp.QUESTION_COUNT - 1 # Go to last actual question
            else:
                self.current_question_index -= 1

            self.progress_var.set(self.current_question_index)
            self.result_frame.pack_forget()
            self.message_frame.pack_forget() # Ensure message frame is hidden when navigating back
            
            # Ensure question_frame is visible before trying to pack progress_frame before it
            self.question_frame.pack(pady=10, fill="both", expand=True)
            if not self.progress_frame.winfo_ismapped():
                 self.progress_frame.pack(fill="x", pady=5, padx=10, before=self.question_frame)
            self.show_question() # This will also call show_message("") internally

    def show_summary(self):
        """
        Displays a summary of all the answers provided by the user.

        This view lists each question and the corresponding answer. It also
        provides buttons to "Get Recommendations", go "Back to Questions" (to the
        last question answered), or "Start Over".
        """
        self.result_frame.pack_forget()
        self.message_frame.pack_forget() # Ensure message frame is hidden
        self.welcome_frame.pack_forget()
        
        # Ensure question_frame is packed before progress_frame for correct 'before' behavior
        self.question_frame.pack(pady=20, fill="both", expand=True)
        if not self.progress_frame.winfo_ismapped():
            self.progress_frame.pack(fill="x", pady=5, padx=10, before=self.question_frame)
        self.progress_var.set(DogActivityApp.QUESTION_COUNT) # Set progress to max

        # Clear previous content (if any) from question_frame now used for summary
        for widget in self.question_frame.winfo_children():
            widget.destroy()

        tk.Label(self.question_frame, text="Summary of Your Answers:",
                 font=(DogActivityApp.FONT_HELVETICA, DogActivityApp.FONT_SIZE_WELCOME, "bold"),
                 bg=self.theme["app_bg"], fg=self.theme["text_fg"]).pack(pady=10)

        summary_text_frame = tk.Frame(self.question_frame, bg=self.theme["app_bg"])
        summary_text_frame.pack(pady=10, padx=20, fill="x")

        for i, (q_text, _) in enumerate(DogActivityApp.QUESTIONS_CONFIG):
            val = self.answers.get(q_text, "Not answered")
            tk.Label(summary_text_frame, text=f"{q_text}:",
                     font=(DogActivityApp.FONT_HELVETICA, DogActivityApp.FONT_SIZE_OPTIONS_SUMMARY_RECOMMENDATIONS, "bold"),
                     bg=self.theme["app_bg"], fg=self.theme["text_fg"], anchor="w").grid(row=i, column=0, sticky="w", pady=2)
            tk.Label(summary_text_frame, text=f" {val}",
                     font=(DogActivityApp.FONT_HELVETICA, DogActivityApp.FONT_SIZE_OPTIONS_SUMMARY_RECOMMENDATIONS),
                     bg=self.theme["app_bg"], fg=self.theme["text_fg"], anchor="w", wraplength=300).grid(row=i, column=1, sticky="w", pady=2)
        summary_text_frame.columnconfigure(1, weight=1) # Allow answer column to expand

        btn_frame = tk.Frame(self.question_frame, bg=self.theme["app_bg"])
        btn_frame.pack(pady=20)
        # Using ttk.Button for better theme integration
        ttk.Button(btn_frame, text="Get Recommendations", width=20, # width in characters
                   command=self.get_recommendations).pack(side="left", padx=5)
        ttk.Button(btn_frame, text="Back to Questions", width=18,
                   command=self.previous_question).pack(side="left", padx=5)
        ttk.Button(btn_frame, text="Start Over", width=15,
                   command=self.restart).pack(side="left", padx=5)


    def get_recommendations(self):
        """
        Generates activity recommendations based on the collected answers.

        This method retrieves all answers, applies a predefined set of rules
        (your recommendation engine logic) to determine suitable activities.
        It handles specific cases like health issues or temperament. The generated
        recommendations are then formatted and passed to `_show_recommendations_page`
        for display.
        """
        if len(self.answers) < DogActivityApp.QUESTION_COUNT:
            self.show_message("Please answer all questions first.", error=True)
            self.show_summary()
            return

        # --- Retrieve answers (as before) ---
        age = self.answers.get("Age Group")
        energy = self.answers.get("Energy Level")
        # ... (retrieve all other answers) ...
        health = self.answers.get("Health or Mobility Issues")
        temperament = self.answers.get("Temperament")
        location = self.answers.get("Preferred Activity Location")
        dog_name_for_rec = self.answers.get(DogActivityApp.DOG_NAME_QUESTION_KEY, "your dog")

        # --- Recommendation Logic (Full logic from previous versions should be here) ---
        # This is a simplified placeholder for the actual recommendation engine.
        # Replace this with your comprehensive recommendation generation.
        recommendations_data = []
        if health == "Joint Issues":
            recommendations_data.append({"text": "❤️‍🩹 Gentle walks, consider hydrotherapy. Avoid high impact.", "tags": ["gentle", "indoor", "outdoor", "health_specific", "joint_issues"]})
        if temperament == "Aggressive":
            recommendations_data = [{"text": "⚠️ Crucial to work with a certified professional trainer or behaviorist IMMEDIATELY. Focus on safety and management.", "tags": ["professional_help", "aggressive_dog_protocol", "caution"]}]
        elif age == "Puppy":
            recommendations_data.append({"text": "🐾 Short, frequent play sessions. Focus on positive socialization.", "tags": ["puppy", "play", "social", "indoor", "outdoor"]})
            recommendations_data.append({"text": "🚫 Avoid strenuous, repetitive exercise until growth plates close.", "tags": ["caution", "puppy"]})
        
        # Fallback generic recommendation if list is empty and not aggressive
        if not recommendations_data and temperament != "Aggressive":
            recommendations_data.append({"text": "🎾 A good game of fetch (if liked) or a mentally stimulating puzzle toy can be great options!", "tags": ["general", "play", "puzzle", "indoor", "outdoor"]})
        # --- End of simplified placeholder logic ---

        # --- Filtering and Formatting (as before) ---
        final_recommendations_text_list = []
        if any("aggressive_dog_protocol" in r.get("tags", []) for r in recommendations_data):
            final_recommendations_text_list = [r["text"] for r in recommendations_data if "aggressive_dog_protocol" in r.get("tags", [])]
        else:
            temp_recs_for_location = []
            location_tag = "indoor" if location == "Inside" else "outdoor"
            idx = 0
            while idx < len(recommendations_data):
                rec = recommendations_data[idx]
                if location_tag in rec.get("tags", []) or \
                   any(t in rec.get("tags", []) for t in ["caution", "health_specific", "senior_specific_consideration", "general"]): # Include general if it fits
                    temp_recs_for_location.append(rec["text"])
                idx += 1
            
            # Add generic location-based suggestions if no specific ones found
            if not temp_recs_for_location or \
               (len(temp_recs_for_location) == 1 and any(t in recommendations_data[0].get("tags",[]) for t in ["caution", "health_specific", "senior_specific_consideration"]) and location_tag not in recommendations_data[0].get("tags",[])):
                generic_recs_inside = ["🧩 Interactive puzzle toys and food-releasing toys are great indoors.","🧸 Indoor fetch with soft toys in a safe, spacious area can be fun.","🎓 Short, fun training sessions focusing on tricks or obedience help stimulate the mind.","👃 Scent games: hide treats around the house for your dog to find using their nose.","🏠 Build a simple indoor obstacle course with household items to explore."]
                generic_recs_outside = ["🌳 Leashed walks in varied environments offer great sniffing opportunities.","🎾 Playing fetch in a securely fenced open area is a classic (if enjoyed and safe).","🐾 Exploring new sniffing spots on a long lead ('decompression walks') can be very enriching.","💧 If safe and enjoyed: water play or splashing sessions in clean water.","👍 Outdoor training in a (mildly) distracting environment helps generalize behaviors."]
                temp_recs_for_location.extend(generic_recs_inside if location == "Inside" else generic_recs_outside)

            final_recommendations_text_list.extend(temp_recs_for_location)
            if not final_recommendations_text_list: # Ultimate fallback
                 final_recommendations_text_list = [rec["text"] for rec in recommendations_data if "aggressive_dog_protocol" not in r.get("tags",[])]

        # Deduplication
        final_recommendations_text_deduped = []
        processed_texts = set()
        idx = 0
        while idx < len(final_recommendations_text_list): # Iterate over the list that was extended
            rec_text = final_recommendations_text_list[idx]
            if rec_text not in processed_texts:
                final_recommendations_text_deduped.append(rec_text)
                processed_texts.add(rec_text)
            idx +=1
        
        # Sorting
        sorted_recs = sorted(final_recommendations_text_deduped, key=lambda x: (
            "⚠️" not in x, "❤️‍🩹" not in x, "👁️‍🗨️" not in x, "👂" not in x,
            "🚫" not in x, "👴👵" not in x, "🐾" not in x and "🐶" not in x,
        ))

        if sorted_recs:
            result_text = f"📝 Recommended activities for {dog_name_for_rec} ({location.lower()} location):\n\n" + "\n".join("• " + act for act in sorted_recs)
        else:
            result_text = f"😥 No specific {location.lower()} location activities found for {dog_name_for_rec} based on the selections. Consider general enrichment like a food puzzle or a gentle walk! 🦴"

        self._show_recommendations_page(result_text)

    def _copy_to_clipboard(self, text_to_copy):
        """
        Copies the provided text to the system clipboard.

        Shows a confirmation message using `show_message` on success, or an
        error message if the clipboard operation fails.

        Args:
            text_to_copy (str): The text string to be copied to the clipboard.
        """
        try:
            self.root.clipboard_clear()
            self.root.clipboard_append(text_to_copy)
            self.show_message("Recommendations copied to clipboard!") # Success message
        except tk.TclError: # Specific error if clipboard access fails
            self.show_message("Error: Could not access the clipboard.", error=True)
        except Exception as e: # Other potential errors
            self.show_message(f"Error copying: {e}", error=True)


    def _show_recommendations_page(self, recommendations_text):
        """
        Displays the generated recommendations on a dedicated page.

        This method handles the setup of the results view, including displaying
        the dog's photo (if uploaded), the list of recommendations, and
        action buttons ("Copy", "Start Over", "Summary"). It ensures proper
        frame management for a clean UI transition.

        Args:
            recommendations_text (str): The formatted string of recommendations
                                        to display.
        """
        # 1. Hide all other primary view frames and the frames we are about to rebuild/manage.
        self.question_frame.pack_forget()
        self.progress_frame.pack_forget()
        self.welcome_frame.pack_forget()
        self.result_frame.pack_forget()   # Explicitly hide result_frame first
        self.message_frame.pack_forget()  # Explicitly hide message_frame as well

        # Force Tkinter to process the pack_forget operations immediately.
        self.root.update_idletasks()

        # 2. Clear previous content from result_frame and message_frame (now that they are hidden)
        for widget in self.result_frame.winfo_children():
            widget.destroy()
        for widget in self.message_frame.winfo_children(): # Though show_message will also do this
            widget.destroy()

        # 3. Call show_message("") to ensure message_frame is definitely in a hidden state
        #    according to its internal logic.
        self.show_message("")

        # 4. Now, pack the result_frame. It's empty, and message_frame is confirmed hidden.
        self.result_frame.pack(pady=10, fill="both", expand=True)

        # 5. Populate result_frame with new content
        if self.dog_photo_imgtk:
            result_photo_label = tk.Label(self.result_frame, image=self.dog_photo_imgtk, bg=self.theme["app_bg"])
            result_photo_label.pack(pady=(10,5))

        rec_label_frame = tk.Frame(self.result_frame, bg=self.theme["app_bg"])
        rec_label_frame.pack(pady=10, padx=20, fill="x")

        self.rec_display_label = tk.Label(rec_label_frame, text=recommendations_text,
                                 font=(DogActivityApp.FONT_HELVETICA, DogActivityApp.FONT_SIZE_OPTIONS_SUMMARY_RECOMMENDATIONS),
                                 bg=self.theme["app_bg"], fg=self.theme["text_fg"], justify="left",
                                 wraplength=max(100, self.root.winfo_width()-60))
        self.rec_display_label.pack(fill="x", expand=True)
        self._adjust_wraplength()

        btn_frame = tk.Frame(self.result_frame, bg=self.theme["app_bg"])
        btn_frame.pack(pady=5, fill="x", side="bottom") # Pack buttons at the bottom

        # Sub-frame to center the buttons if btn_frame fills 'x'
        button_sub_frame = tk.Frame(btn_frame, bg=self.theme["app_bg"])
        button_sub_frame.pack() # Default pack will center it within btn_frame

        # Using ttk.Button for better theme integration
        ttk.Button(button_sub_frame, text="Copy", width=12,
                   command=lambda: self._copy_to_clipboard(recommendations_text)).pack(side="left", padx=5)
        ttk.Button(button_sub_frame, text="Start Over", width=15,
                   command=self.restart).pack(side="left", padx=5)
        ttk.Button(button_sub_frame, text="Summary", width=12,
                   command=self.show_summary).pack(side="left", padx=5)


    def on_closing(self):
        """
        Handles the application window closing event (e.g., clicking the 'X' button).

        Displays a confirmation/goodbye message box to the user. If the user
        acknowledges (clicks OK), the application window is destroyed,
        terminating the program.
        """
        dog_name = self.answers.get(DogActivityApp.DOG_NAME_QUESTION_KEY, "your furry friend")
        goodbye_title = "Goodbye! 🐾"
        goodbye_message = f"Thanks for using the Dog Activity Recommender!\n\n" \
                          f"Hope you and {dog_name} have a fantastic time with your new activities! 👋"
        if dog_name == "your furry friend" and self.current_question_index == 0 and not self.answers:
            goodbye_message = "Thanks for checking out the Dog Activity Recommender!\n\nCome back soon to find paw-some activities! 🐶"

        try:
            # messagebox.showinfo returns 'ok' (a string) if OK is pressed
            if messagebox.showinfo(goodbye_title, goodbye_message):
                self.root.destroy()
        except Exception as e: # Fallback if messagebox itself has an issue
            print(f"Error during on_closing: {e}")
        else:
            print("Closed gracefully.")
        finally:
            print("Window close event handled.")
            self.root.destroy() # Ensure closure


if __name__ == '__main__':
    root = tk.Tk()
    app = DogActivityApp(root)
    root.mainloop()