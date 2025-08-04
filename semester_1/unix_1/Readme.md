# 🖥️ Unix_1 – Basic Unix Command Line Guide

This guide provides an introduction to essential Unix commands and concepts. It's perfect for beginners who want to get familiar with the command-line interface. You'll learn how to navigate the system, create and edit files, and manage file permissions.

---

## 📁 Commands

Learn how to perform common file and directory operations:

- `ls` – List directory contents  
  Example: `ls`

- `pwd` – Print the current working directory  
  Example: `pwd`

- `cat` – Display the contents of a file  
  Example: `cat notes.txt`

- `touch` – Create a new empty file  
  Example: `touch newfile.txt`

---

## ⚙️ Options

Options (or flags) modify the behavior of a command.  
Example: `ls -l`  
The `-l` option displays a long listing format, showing permissions, file size, and timestamps.

---

## 🧾 Arguments

Arguments tell a command what to act on.  
Example: `cat filename.txt`  
Here, `filename.txt` is the argument passed to `cat`, specifying the file to display.

---

## 📝 Text Editors

Use text editors to create and edit files directly in the terminal.

### Nano (Beginner Friendly)  
Command: `nano myfile.txt`  
- Save: `Ctrl + O`, then `Enter`  
- Exit: `Ctrl + X`

### Vi (Advanced Users)  
Command: `vi myfile.txt`  
- Enter insert mode: Press `i`  
- Save and exit: Press `Esc`, type `:wq`, and press `Enter`

---

## 🔐 Permissions

Every file in Unix has permissions that determine who can read, write, or execute it.

### Permission Types:  
- `r` – Read  
- `w` – Write  
- `x` – Execute

### Viewing Permissions  
Command: `ls -l`  
Example output:  
`-rwxr--r--  1 user  group  1234 Jun  5 10:00 script.sh`

### Changing Permissions  
Use the `chmod` command to modify permissions.  
Example: `chmod +x script.sh`  
This grants execute permission to the script.

---

## ✅ Summary

This guide gives you a foundation in:

- Using essential Unix commands  
- Modifying command behavior with options  
- Providing arguments to commands  
- Creating and editing files via terminal editors  
- Viewing and managing file permissions

Start practicing these to build confidence in the Unix environment.

---

*Created by Javier Napoles*