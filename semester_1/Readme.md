# DAE Projects – General Overview

Welcome to the DAE Projects repository! This single README provides a concise summary of each subproject, explains their goals, and outlines usage or key concepts. Whether you’re here to study basic algorithmic logic, learn essential Unix commands, explore AI terminology, or run the semester’s final project—a Python-based dog activity recommender—you’ll find everything in one place.

---

## Table of Contents

1. [Logic 1 (Algorithmic Thinking)](#logic-1-algorithmic-thinking)  
2. [Prompt Engineering & AI Terminology](#prompt-engineering--ai-terminology)  
3. [Final Project: Dog Activity Recommender (Semester 1)](#final-project-dog-activity-recommender-semester-1)  
4. [Unix_1 – Basic Unix Command Line Guide](#unix_1–basic-unix-command-line-guide)  
5. [Unix_2 – Intermediate Unix Command Line Guide](#unix_2–intermediate-unix-command-line-guide)  
6. [How to Navigate This Repository](#how-to-navigate-this-repository)  
7. [Credits & Contact](#credits--contact)  

---

## Logic 1 (Algorithmic Thinking)

### Overview  
The **Logic 1** folder is dedicated to sharpening foundational problem-solving skills via Boolean logic, conditional statements, and flowchart design. By working through these exercises, you’ll learn how to translate real-world decisions into step-by-step algorithms.

### Key Contents  
- **Crafted Algorithms:**  
  - At least six steps per algorithm.  
  - Integration of Boolean expressions (`AND`, `OR`, `NOT`) and simple conditionals (`IF`, `ELSE`).  
- **Flowchart Visualizations:**  
  - Diagrams that mirror each algorithm’s structure.  
  - Usage of standard symbols:  
    - **Start/Stop**  
    - **Decision**  
    - **Process**  
    - **Input/Output**  
- **Boolean & Conditional Logic:**  
  - Clear “decision points” showing how conditions affect flow.  
  - Examples of nested conditions and decision trees.

### Purpose  
Build a strong base in logical reasoning, which is essential for any programming, software development, or system-design task.

---

## Prompt Engineering & AI Terminology

### Overview  
This document serves as a quick reference for key AI concepts and prompt engineering techniques used throughout various AI-driven projects. It’s especially helpful if you’re new to working with language or multimodal models.

### Core Sections  
1. **Tokenization & Data Utilization**  
   – Breaking input (text, images, etc.) into tokens so models can process them efficiently.  
2. **AI Hallucination Management**  
   – Identifying and minimizing incorrect or fabricated AI outputs.  
3. **Multimodal AI Task Execution**  
   – Strategies for designing tasks where the model handles text, images, or other media.  
4. **Prompt Design & Iteration**  
   – Crafting prompts to guide AI behavior, then refining them through testing.  
5. **Text & Image Generation Workflow**  
   – End-to-end process: data preparation → model interaction → output formatting.  
6. **Exported Interaction Documentation**  
   – Capturing logs or transcripts of user-AI conversations for auditing, debugging, or downstream integration.

---

## Final Project: Dog Activity Recommender (Semester 1)

### Overview  
The **Dog Activity Recommender** is the final project for Semester 1, synthesizing everything we’ve learned so far. By analyzing dog profiles and preferences, this Python/Tkinter app generates customized activity suggestions that keep pets healthy, engaged, and happy—applying algorithmic logic, UI design, and file I/O all in one place.

### Core Functionality  
- **Backend Logic (Python 3.13.3):**  
  - Implements recommendation algorithms based on your dog’s energy level, size, temperament, and activity preferences.  
- **Graphical Interface (Tkinter):**  
  - A user-friendly GUI with form fields, buttons, and a scrollable panel showing tailored suggestions.  
  - Supports both **light** and **dark** themes and includes hover effects on buttons.  
- **Image Support (Pillow):**  
  - Displays dog-related icons or photos alongside each recommended activity to make selections more engaging.  
- **Clipboard & Export Features:**  
  - Copy recommended activities to the clipboard.  
  - Export results into a plain `.txt` file for later reference.

### What We Study in Semester 1  
- **Algorithmic Thinking:** Translating real-world decision trees into Python code, as practiced in the Logic 1 exercises.  
- **UI Fundamentals:** Using Tkinter to build forms, buttons, and scrollable frames—covered in class modules on GUI design.  
- **File Handling & I/O:** Reading and writing `.txt` files to persist user data or export recommendations.  
- **Theme & Style Management:** Detecting OS themes (light vs. dark) and dynamically adjusting colors.  
- **External Libraries:** Integrating third-party packages (e.g., Pillow) for image loading and display.

### Technologies & Dependencies  
- **Python 3.13.3** (ensure you have this version installed)  
- **Tkinter:** Typically bundled with Python. If missing, install via your OS’s package manager (e.g., `sudo apt-get install python3-tk`).  
- **Pillow:** To install:  
  ```bash
  pip install pillow
  ```

### Usage  
1. **Clone or download** the repository.  
2. **Install dependencies:**  
   ```bash
   pip install pillow
   ```  
3. **Run the application:**  
   ```bash
   python doggy_v7.0.py
   ```  
4. **Answer the on-screen questions** about your dog’s profile.  
5. **View**, **copy**, or **export** the final personalized activity suggestions.

### Future Enhancements (Beyond Semester 1)  
- **Weather Integration:** Automatically adjust recommendations based on real-time weather data (indoor vs. outdoor suggestions).  
- **AI-Powered Adaptation:** Use simple machine learning to refine suggestions over time as the dog’s behavior changes.  
- **Expanded Questionnaire:** Collect more data points (breed-specific traits, dietary restrictions, etc.) for deeper personalization.  
- **API Integrations:** Fetch local dog-park locations or sitter services dynamically.

---

## Unix_1 – Basic Unix Command Line Guide

### Overview  
The **Unix_1** guide is designed for those just getting started with a Unix or Linux terminal. It covers essential commands and concepts to navigate directories, view files, and manage permissions.

### Major Topics  
1. **Common Commands**  
   - `ls`: List directory contents (e.g., `ls -l` for long format).  
   - `pwd`: Show the current working directory.  
   - `cat`: Display a file’s contents.  
   - `touch`: Create a new empty file.  
2. **Options & Arguments**  
   - Understanding flags (e.g., `-l`, `-a`) and how to supply filenames or directories as arguments.  
3. **Text Editors**  
   - **nano** (Beginner friendly):  
     - Save: `Ctrl + O`; Exit: `Ctrl + X`.  
   - **vi/vim** (Advanced users):  
     - Enter insert mode: `i`; Save & quit: `Esc`, then `:wq`.  
4. **File Permissions**  
   - Viewing with `ls -l` (e.g., `-rwxr--r--`).  
   - Changing via `chmod` (e.g., `chmod +x script.sh`).

### Purpose  
Build confidence in using a terminal to perform everyday tasks—creating, editing, and managing files and directories—before moving on to more advanced shell concepts.

---

## Unix_2 – Intermediate Unix Command Line Guide

### Overview  
Picking up where **Unix_1** left off, the **Unix_2** guide dives into more powerful commands, shell customization, and environment tweaks that make you a more efficient Unix user.

### Major Topics  
1. **Advanced Commands**  
   - `cp`: Copy files or directories (e.g., `cp file.txt backup/`).  
   - `mv`: Move or rename (e.g., `mv oldname.txt newname.txt`).  
   - `mkdir`: Create new directories.  
   - `rm`: Remove files or entire directories.  
   - `less`: Paginate through long files one screen at a time.  
2. **Arguments & Options**  
   - Combining flags and multiple arguments (e.g., `cp file1.txt file2.txt /destination/`).  
3. **Kernels & Shells**  
   - Identify your default shell (`echo $SHELL`).  
   - Switch shells (e.g., `zsh`).  
   - Use `ps -p $$` to see which shell process you’re in.  
4. **Environment Customization**  
   - **Aliases:** Create shortcuts such as `alias ll='ls -la'`.  
   - **PS1 Prompt:** Change your shell prompt (e.g., `export PS1="\[\e[32m\]\w \$ \[\e[0m\]"`).  
   - Persist changes by editing `~/.bashrc`, `~/.zshrc`, or other shell RC files.

### Purpose  
Learn how to streamline your workflow, automate repetitive tasks, and get comfortable with customizing your Unix environment for daily productivity.

---

## How to Navigate This Repository

Each of the sections above corresponds to a top-level folder. Here’s what you’ll see:

```
├── Logic 1/  
│   ├── algorithms.md  
│   └── flowcharts/  
│       ├── flowchart1.png  
│       ├── flowchart2.png  
│       └── …  
├── Prompt_Engineering/  
│   └── AI_Terminology_Overview.md  
├── Dog_Activity_Recommender/  
│   ├── doggy_v7.0.py  
│   ├── assets/  
│   │   └── (images, icons)  
│   ├── requirements.txt  
│   └── README.md  
├── Unix_1/  
│   └── Unix_1_Guide.md  
├── Unix_2/  
│   └── Unix_2_Guide.md  
└── README.md  ← (this file)
```

1. **Logic 1/** – Open `algorithms.md` for step-by-step algorithms and view the `flowcharts/` folder for visual diagrams.  
2. **Prompt_Engineering/** – Read `AI_Terminology_Overview.md` to learn about prompt design, tokenization, and more.  
3. **Dog_Activity_Recommender/** – See `README.md` inside for detailed installation and usage; run `doggy_v7.0.py` to launch the semester’s final project, the Dog Activity Recommender.  
4. **Unix_1/** – Open `Unix_1_Guide.md` to learn basic Unix commands and file management.  
5. **Unix_2/** – Open `Unix_2_Guide.md` to explore advanced commands, shell customization, and environmental tweaks.

---

## Credits & Contact

- **Logic 1** and **Prompt Engineering** documents created by Javier Napoles.  
- **Dog Activity Recommender** (Semester 1 final project) authored by Javier Napoles (Python 3.13.3, Tkinter, Pillow).  
- **Unix_1** and **Unix_2** guides authored by Javier Napoles.  

If you have questions, suggestions, or want to contribute to any subproject, please feel free to reach out:

- **Author:** Javier Napoles  
- **Email:** jnapfx@gmail.com  

We hope you find these resources helpful for learning algorithms, Unix, AI concepts, and building Python-based GUIs for a real-world application. Enjoy exploring the DAE Projects!

---

## Special Thanks

Kyley Komschlies

Kakra Detome

Abhinav Piratla

Devanshi Tandel
